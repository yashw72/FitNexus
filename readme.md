<div align="center">

```
███████╗██╗████████╗███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
██╔════╝██║╚══██╔══╝████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
█████╗  ██║   ██║   ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██╔══╝  ██║   ██║   ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
██║     ██║   ██║   ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

<h3>⚡ Gym Management System — Powered by Django & MySQL</h3>

<p>
  <img src="https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-5.x-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p>
  <b>FitNexus</b> is a full-stack gym management platform designed to simplify every aspect of daily gym operations —<br/>
  from managing members & trainers to tracking attendance, equipment, and plans. All in one place.
</p>

---

</div>

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [🚀 Getting Started](#-getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Virtual Environment](#2-set-up-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Configure the Database](#4-configure-the-database)
  - [5. Run Migrations](#5-run-migrations)
  - [6. Seed Sample Data](#6-seed-sample-data)
  - [7. Create Admin User](#7-create-admin-user)
  - [8. Launch the Server](#8-launch-the-server)
- [🔑 Authentication](#-authentication)
- [🗄️ Database Schema](#️-database-schema)
- [🔗 URL Routes](#-url-routes)
- [📊 ORM Query Reference](#-orm-query-reference)
- [🖥️ Screenshots](#️-screenshots)
- [🤝 Contributing](#-contributing)

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 🏠 **Dashboard** | Live stats — total members, trainers, equipment & today's attendance |
| 👥 **Members** | Add, search, view, and manage gym members with plan & trainer assignment |
| 🏋️ **Trainers** | Manage trainer profiles with specialties |
| 📋 **Membership Plans** | Define monthly/yearly pricing plans |
| 🔧 **Equipment** | Track inventory status — active, idle, or maintenance needed |
| 📅 **Attendance** | Daily check-in/check-out logging and filtering |
| 🔐 **Authentication** | Secure login/logout with role-based access (staff vs member) |
| 🛡️ **Admin Panel** | Full Django admin interface for superusers |

---

## 🛠️ Tech Stack

```
Backend   ──  Django 4.x (Python)
Database  ──  MySQL 8.0 via pymysql
Frontend  ──  Django Templates + Bootstrap 5 + HTML/CSS/JS
ORM       ──  Django ORM (auto-converts Python → SQL)
Auth      ──  Django built-in authentication system
Tools     ──  MySQL Workbench, pip, virtualenv
```

---

## 📁 Project Structure

```
FitNexus/
│
├── 📄 manage.py                        ← Django command runner
├── 📄 create_db.py                     ← Creates the MySQL database
├── 📄 seed_data.py                     ← Seeds plans, trainers, members
├── 📄 seed_equipment.py                ← Seeds equipment inventory
├── 📄 reseed_indian.py                 ← Seeds Indian member demo data
│
├── ⚙️  antigravity_project/            ← Project configuration
│   ├── __init__.py                     ← pymysql bridge setup
│   ├── settings.py                     ← Global settings (DB, apps, etc.)
│   ├── urls.py                         ← Root URL dispatcher
│   ├── wsgi.py                         ← Production deployment
│   └── asgi.py                         ← Async deployment
│
└── 🏋️  gym/                            ← Main application
    ├── models.py                       ← Database table definitions
    ├── views.py                        ← Business logic & queries
    ├── urls.py                         ← App URL routes
    ├── admin.py                        ← Admin panel registration
    ├── apps.py                         ← App configuration
    ├── migrations/                     ← Auto-generated SQL migrations
    └── templates/gym/
        ├── base.html                   ← Master layout (navbar + sidebar)
        ├── login.html                  ← Login page
        ├── home.html                   ← Dashboard
        ├── members.html                ← Members list
        ├── add_member.html             ← Add member form
        ├── trainers.html               ← Trainers list
        ├── add_trainer.html            ← Add trainer form
        ├── equipment.html              ← Equipment inventory
        ├── add_equipment.html          ← Add equipment form
        ├── attendance.html             ← Attendance tracker
        └── plans.html                  ← Membership plans
```

---

## ⚙️ Prerequisites

Make sure the following are installed on your system before proceeding:

- ✅ **Python 3.10+** — [Download](https://www.python.org/downloads/)
- ✅ **MySQL 8.0+** — [Download](https://dev.mysql.com/downloads/mysql/)
- ✅ **MySQL Workbench** *(optional but recommended)* — [Download](https://dev.mysql.com/downloads/workbench/)
- ✅ **pip** — comes bundled with Python
- ✅ **Git** — [Download](https://git-scm.com/)

---

## 🚀 Getting Started

Follow these steps exactly in order to get FitNexus running on your local machine.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fitnexus.git
cd fitnexus
```

---

### 2. Set Up Virtual Environment

Creating a virtual environment keeps your project dependencies isolated.

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> ✅ You should see `(venv)` at the start of your terminal prompt.

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install django pymysql
```

---

### 4. Configure the Database

#### Step 4a — Update MySQL credentials in `antigravity_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gym_db',          # ← Database name
        'USER': 'root',            # ← Your MySQL username
        'PASSWORD': 'YourPass',    # ← Your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Step 4b — Create the MySQL database:

```bash
python create_db.py
```

> ✅ This creates the `gym_db` database in MySQL. You only need to run this **once**.

---

### 5. Run Migrations

Migrations create all the required tables inside `gym_db`.

```bash
python manage.py makemigrations
python manage.py migrate
```

> ✅ You should now see tables like `gym_member`, `gym_trainer`, `gym_equipment`, etc. in MySQL Workbench.

---

### 6. Seed Sample Data

Populate the database with starter data for testing:

```bash
# Insert membership plans, trainers, and a sample member
python seed_data.py

# (Optional) Insert equipment inventory
python seed_equipment.py

# (Optional) Insert Indian-name demo members
python reseed_indian.py
```

---

### 7. Create Admin User

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
```
Username: admin
Email: admin@fitnexus.com
Password: ••••••••
Password (again): ••••••••
```

> ✅ Only users with `is_staff = True` can add/delete trainers and equipment.

---

### 8. Launch the Server

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://localhost:8000/        ← Main app
http://localhost:8000/admin/  ← Django Admin panel
```

> 🎉 **FitNexus is now running!**

---

## 🔑 Authentication

FitNexus uses Django's built-in authentication system.

| Route | Description |
|-------|-------------|
| `/login/` | Login page |
| `/logout/` | Logout and redirect to login |
| `/admin/` | Django superuser admin panel |

- All views are protected with `@login_required` — unauthenticated users are redirected to `/login/`
- Admins (staff users) have full CRUD access; regular users have read-only or restricted access

---

## 🗄️ Database Schema

Five core tables power FitNexus:

```
┌─────────────────────┐       ┌──────────────────────┐
│   gym_membershipplan│       │     gym_trainer        │
├─────────────────────┤       ├──────────────────────┤
│ id (PK)             │       │ id (PK)               │
│ name                │       │ first_name            │
│ duration_months     │       │ last_name             │
│ price               │       │ specialty             │
└────────┬────────────┘       └──────────┬────────────┘
         │                               │
         └──────────────┬────────────────┘
                        ▼
              ┌─────────────────────┐
              │     gym_member       │
              ├─────────────────────┤
              │ id (PK)             │
              │ first_name          │
              │ last_name           │
              │ email (unique)      │
              │ phone               │
              │ join_date           │
              │ plan_id (FK)  ──────┘
              │ assigned_trainer_id(FK)
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   gym_attendance     │
              ├─────────────────────┤
              │ id (PK)             │
              │ member_id (FK)      │
              │ date                │
              │ check_in            │
              │ check_out           │
              └─────────────────────┘

              ┌─────────────────────┐
              │   gym_equipment      │
              ├─────────────────────┤
              │ id (PK)             │
              │ name                │
              │ quantity            │
              │ status              │
              │ purchase_date       │
              └─────────────────────┘
```

---

## 🔗 URL Routes

| URL | View Function | Page |
|-----|---------------|------|
| `/` | `home` | Dashboard with live stats |
| `/members/` | `member_list` | Browse & search members |
| `/add-member/` | `add_member` | Add a new member |
| `/trainers/` | `trainers_list` | Browse trainers |
| `/add-trainer/` | `add_trainer` | Add a new trainer |
| `/equipment/` | `equipment_list` | Equipment inventory |
| `/add-equipment/` | `add_equipment` | Add equipment |
| `/attendance/` | `attendance_list` | Attendance records |
| `/plans/` | `plans_list` | Membership plans |
| `/login/` | `login_view` | Login page |
| `/logout/` | `logout_view` | Logout |
| `/admin/` | Django Admin | Superuser panel |

---

## 📊 ORM Query Reference

Django ORM automatically translates Python into SQL. Here's a quick reference:

| Python ORM | Equivalent SQL |
|---|---|
| `Member.objects.all()` | `SELECT * FROM gym_member;` |
| `Member.objects.count()` | `SELECT COUNT(*) FROM gym_member;` |
| `Member.objects.filter(email='x@y.com')` | `SELECT * FROM gym_member WHERE email='x@y.com';` |
| `Member.objects.create(first_name='Ali')` | `INSERT INTO gym_member (first_name) VALUES ('Ali');` |
| `member.save()` | `UPDATE gym_member SET ... WHERE id=...;` |
| `member.delete()` | `DELETE FROM gym_member WHERE id=...;` |
| `Member.objects.select_related('plan')` | `SELECT ... FROM gym_member JOIN gym_membershipplan ON ...` |
| `Member.objects.filter(Q(first_name__icontains='a'))` | `WHERE first_name LIKE '%a%'` |

---

## 🖥️ How a Page Request Works

```
🌐 Browser visits: http://localhost:8000/members/
        │
        ▼
📄 antigravity_project/urls.py
   → Catches all '' paths → routes to gym.urls
        │
        ▼
📄 gym/urls.py
   → path('members/', views.member_list)
        │
        ▼
🧠 gym/views.py → member_list()
   → Queries MySQL via ORM
   → Builds context dictionary
        │
        ▼
🖼️  gym/templates/gym/members.html
   → Django renders HTML with data
        │
        ▼
✅ Browser displays the page
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

```bash
# 1. Fork the repository on GitHub

# 2. Create a new feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes and commit
git add .
git commit -m "feat: add your feature description"

# 4. Push your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request on GitHub
```

Please follow clean code practices and include comments where relevant.

---

<div align="center">

**Built with 💪 for gym owners who mean business.**

<sub>FitNexus — Where Fitness Meets Technology</sub>

</div>
