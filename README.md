# 🔐 Simple Role-Based JWT Authentication (Django REST Framework)

This project is a **simple authentication system** built with **Django REST Framework**.  
It uses **JWT (JSON Web Tokens)** for authentication and supports **role-based access control**.  
API testing and verification are done using **Postman**.

---

## 📌 Features

- ✅ User Registration (with role assignment)
- ✅ JWT Authentication (Login & Token Refresh)
- ✅ Role-Based Access (Admin, User, etc.)
- ✅ Secured API Endpoints
- ✅ Postman Collection for Testing

---

## 🛠️ Tech Stack

- **Backend:** Django REST Framework  
- **Authentication:** JWT (via `djangorestframework-simplejwt`)  
- **Database:** SQLite (default, easy setup)  
- **Testing:** Postman  

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <REPO_URL>
cd simple-role-based-auth
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Migrations
```bash
python manage.py migrate
```
### 5. Create Superuser
```bash
python manage.py createsuperuser
```
### 6. Run Server
```bash
python manage.py runserver
```

API runs at: http://127.0.0.1:8000/

**🔐 Authentication (JWT)**

1. Register User

POST /api/register/
```bash
{
  "username": "testuser",
  "password": "password123",
  "role": "user"
}
```
2. Login

POST /api/token/
```bash
{
  "username": "testuser",
  "password": "password123"
}

```
Response:
```bash
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```
3. Access Protected Endpoint

Send request with Authorization header:
```bash
Authorization: Bearer <access_token>
```
4. Refresh Token

POST /api/token/refresh/
```bash
{
  "refresh": "<refresh_token>"
}
```

**👥 Role-Based Access Example**

Admin Role → Can manage users, view all data.

User Role → Can only access their own profile.

Example Protected Endpoint:

GET /api/admin/dashboard/ → Admin only

GET /api/user/profile/ → User only

If a user without permission tries → 403 Forbidden

**🧪 Testing with Postman**

Import the provided Postman Collection (📁 postman_collection.json).

Test endpoints:

Register

Login

Access Protected Routes with JWT

**📬 Contact**

LinkedIn: Abenezer Sileshi

Gmail: abinesilew@gmail.com

Telegram: @Aben14i
