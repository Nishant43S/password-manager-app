# 🔐 Password Manager Web App

A secure and user-friendly **Password Manager** built using **HTML, CSS, JavaScript, Python (Flask), Bootstrap 5, and Firebase**. This app allows users to register or log in and manage their sensitive credentials safely and efficiently. Data is securely stored in Firebase Realtime Database, and the app is protected with a firewall for enhanced security.

🚀 **Live Demo**: [password manager](https://password-manager-r7dm.onrender.com/)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5  
- **Backend**: Python with Flask  
- **Database**: Firebase Realtime Database  
- **Authentication**: Firebase Authentication (Email/Password)  
- **Hosting**: Render  
- **Security**: Firebase Rules, HTTPS, Firewall protection

---

## ✨ Features

- 🔐 **User Authentication**
  - Register with email and password
  - Login with existing credentials
  - Session management using secure cookies

- 🧰 **Credential Management**
  - Add new credentials (website, username, password)
  - Edit existing credentials
  - Delete credentials securely
  - Search functionality for quick access
  - Clean UI with vertical display using `<hr>` separators

- 🗂️ **Account Settings**
  - Delete your account and all associated data

- 🛡️ **Security**
  - Protected with HTTPS and backend firewall rules
  - Firebase Authentication and Realtime Database Rules
  - Credentials stored per-user, ensuring complete data isolation

---

## 🧪 How It Works

1. **Register/Login**
   - Users must first register or log in using their email and password.
   - On successful authentication, a user session is created.

2. **Dashboard Access**
   - after login, users are redirected to the Dashboard.
   - Users can:
     - Add credentials (with fields for website, username, password)
     - Edit or delete existing credentials
     - View all saved credentials, neatly organized

3. **Data Storage**
   - All data is stored under the user's email node in Firebase.
   - Only authenticated users can read/write their own data.

4. **Account Deletion**
   - Users can permanently delete their account and all saved credentials.

---

## 🔐 Security Practices

- Secure routes with authentication guards
- Firebase rules restrict database access by user
- Credentials are never shared or exposed
- HTTPS communication on Render
- App is protected by a backend firewall to prevent unauthorized access

---


## run in local

install requirements
```bash
pip install -r requirements.txt
```



run locally
```bash
python app.py
```

## screenshots

![Screenshot 2025-05-13 122027](https://github.com/user-attachments/assets/e9edcbe2-7aba-47a1-a235-cb61f3ce7d85)





![Screenshot 2025-05-13 122140](https://github.com/user-attachments/assets/7ebb910c-a995-4b23-b1fd-897c774b1665)



![Screenshot 2025-05-13 122237](https://github.com/user-attachments/assets/721c4843-7209-45d8-8acd-02c6d75886d9)




![Screenshot 2025-05-13 122353](https://github.com/user-attachments/assets/42d730f2-b7d4-4efe-9fa9-8453d3204713)



![Screenshot 2025-05-13 122437](https://github.com/user-attachments/assets/19a6c8b2-f5fa-4a5d-b497-ace7e0caf64f)

















```

