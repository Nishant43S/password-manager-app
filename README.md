# 🔐 Password Manager Web App

A secure and user-friendly **Password Manager** built using **HTML, CSS, JavaScript, Python (Flask), Bootstrap 5, and Firebase**. This app allows users to register or log in and manage their sensitive credentials safely and efficiently. Data is securely stored in Firebase Realtime Database, and the app is protected with a firewall for enhanced security.

🚀 **Live Demo**: [https://password-manager-r7dm.onrender.com/](https://password-manager-r7dm.onrender.com/)

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
   - Upon login, users are redirected to the Dashboard.
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

## 📷 Screenshots

| Login/Register | Dashboard | Add/Edit Credential |
|----------------|-----------|---------------------|
| ![login](https://via.placeholder.com/300x180?text=Login+Page) | ![dashboard](https://via.placeholder.com/300x180?text=Dashboard) | ![add](https://via.placeholder.com/300x180?text=Add+Credential) |

---

## 🚀 Try It Live

👉 **Live App**: [https://password-manager-r7dm.onrender.com/](https://password-manager-r7dm.onrender.com/)

> 📝 *Note: If you encounter a slight delay when opening the app, it's due to Render's free-tier cold start.*

---

## 📁 Project Structure

