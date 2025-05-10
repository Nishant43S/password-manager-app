from flask import Flask, render_template, request, redirect, make_response, url_for, session, jsonify
from pyrebase_config import auth as login_auth, db
import datetime
import re
from firewall import *

app = Flask(__name__)
app.secret_key = 'Davkag19o2g9y1ph0'  



# List of blocked IPs
BLOCKED_IPS = ['192.168.0.100', '10.0.0.50']

# Blocked request patterns (e.g., SQL injection attempts, malicious scripts)
BLOCKED_PATTERNS = [r"SELECT.*FROM", r"DROP.*TABLE", r"<script.*>"]

# Function to check if IP is blocked
def is_ip_blocked(ip):
    return ip in BLOCKED_IPS

# Function to check if request contains any blocked patterns
def is_request_malicious(req_data):
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, req_data, re.IGNORECASE):
            return True
    return False

# Middleware to intercept incoming requests and apply firewall checks
@app.before_request
def firewall_check():
    # Get client IP
    client_ip = request.remote_addr

    # Block IPs if they are in the blocked list
    if is_ip_blocked(client_ip):
        return jsonify({"message": "403 Forbidden: Your IP is blocked."}), 403

    # Check for any malicious patterns in the URL or request data
    if is_request_malicious(request.url) or is_request_malicious(str(request.form)):
        return jsonify({"message": "403 Forbidden: Malicious request detected."}), 403

def sanitize_email(email):
    return email.replace('.', '_')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_auth.create_user_with_email_and_password(email=email, password=password)
            # Clear cookies and redirect to login
            resp = make_response(redirect(url_for('login')))
            resp.set_cookie('email', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            resp.set_cookie('token', '', expires=0)
            session.pop('user', None)
            return resp
        except Exception as e:
            return render_template('register.html', error_msg="Email already exists")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Auto-login using cookies
    if request.method == 'GET':
        email = request.cookies.get('email')
        password = request.cookies.get('password')
        if email and password:
            try:
                user = login_auth.sign_in_with_email_and_password(email=email, password=password)
                session['user'] = email
                resp = make_response(redirect(url_for('dashboard', user_ID=email)))
                resp.set_cookie('token', user['idToken'], max_age=30*24*60*60)
                return resp
            except:
                return render_template('login.html', error_msg="Session expired or invalid credentials")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = login_auth.sign_in_with_email_and_password(email=email, password=password)
            session['user'] = email
            session['password'] = password
            resp = make_response(redirect(url_for('dashboard', user_ID=email)))
            resp.set_cookie('email', email, max_age=30*24*60*60)
            resp.set_cookie('password', password, max_age=30*24*60*60)
            resp.set_cookie('token', user['idToken'], max_age=30*24*60*60)
            return resp
        except:
            return render_template('login.html', error_msg="Invalid Credentials")
    
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'], defaults={"user_ID":None})
@app.route('/dashboard/<user_ID>', methods=['GET', 'POST'])
def dashboard(user_ID):
    try:
        email = session.get('user')
        token = request.cookies.get('token')

        if not email or not token:
            return redirect(url_for('login'))

        user_key = sanitize_email(email)

        if request.method == 'POST':
            data = {
                "application": request.form['application'],
                "username": request.form['username'],
                "password": request.form['password']
            }
            db.child(user_key).push(data, token=token)

        entries = db.child(user_key).get(token=token).val() or {}
        return render_template('dashboard.html', entries=entries, email=email)

    except Exception as e:
        print("Dashboard error:", e)
        return redirect(url_for('login'))



@app.route('/edit/<key>', methods=['POST'])
def edit_entry(key):
    email = request.cookies.get('email')
    token = request.cookies.get('token')
    if not email or not token:
        return redirect('/login')

    user_key = sanitize_email(email)
    updated_data = {
        "application": request.form['application'],
        "username": request.form['username'],
        "password": request.form['password']
    }
    db.child(user_key).child(key).update(updated_data, token=token)
    return redirect(url_for('dashboard',user_ID=request.cookies.get('email')))

@app.route('/delete/<key>')
def delete_entry(key):
    email = request.cookies.get('email')
    token = request.cookies.get('token')
    if not email or not token:
        return redirect('/login')
    user_key = sanitize_email(email)
    db.child(user_key).child(key).remove(token=token)
    return redirect(url_for('dashboard',user_ID=request.cookies.get('email')))

@app.route('/logout')
def logout():
    session.pop('user', None)
    resp = make_response(redirect(url_for('home')))
    resp.delete_cookie('email')
    resp.delete_cookie('password')
    resp.delete_cookie('token')
    return resp

# Optional route for "Already have an account" button from register page
@app.route('/redirect_to_dashboard')
def redirect_to_dashboard():
    if 'user' in session:
        return redirect(url_for('dashboard',user_ID=request.cookies.get('email')))
    else:
        return redirect(url_for('login'))

# about page
@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))

    email = session.get('user')
    token = request.cookies.get('token')

    if request.method == 'POST':
        form_email = request.form.get('email')
        confirm1 = request.form.get('confirm1')
        confirm2 = request.form.get('confirm2')
        confirm3 = request.form.get('confirm3')

        if email == form_email and confirm1 and confirm2 and confirm3:
            try:
                user_key = sanitize_email(email)
                # Delete user's data from Firebase Database
                db.child(user_key).remove(token=token)
                # Delete user account
                user = login_auth.sign_in_with_email_and_password(email, request.cookies.get('password'))
                login_auth.delete_user_account(user['idToken'])
                # Clear session and cookies
                session.pop('user', None)
                resp = make_response(redirect(url_for('home')))
                resp.delete_cookie('email')
                resp.delete_cookie('password')
                resp.delete_cookie('token')
                return resp
            except Exception as e:
                print("Account deletion error:", e)
                return render_template('profile.html', error_msg="Failed to delete account.",)
        else:
            return render_template('profile.html', email=session['user'],user_password=request.cookies.get('password') , warning=True)

    return render_template('profile.html',user_password=request.cookies.get('password'), email=session['user'])




# run app
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
    run_server()



