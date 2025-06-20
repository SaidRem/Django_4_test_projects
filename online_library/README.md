# Online Library

The **Online Library** project is a web application built using Django to manage a collection of books. Users can view the list of books, filter them by publication date, and navigate through the catalog. The library allows for easy viewing of individual books and their details.

---

## 📋 Description

This project serves as an online catalog where users can:

* View all books.
* View books by specific publication dates.
* Navigate between previous and next books based on their publication date.
* Filter and paginate books.

---

## 🛠 Technologies

* **Django** (v4.2) — Web framework for developing the project.
* **PostgreSQL** — Database for storing book data.
* **Bootstrap** — For responsive and mobile-friendly layout.
* **Python** (v3.x) — Programming language for the backend.

---

## 🚀 Installation

### Prerequisites:

* **Python 3.x**
* **PostgreSQL** — Install and configure PostgreSQL (ensure the database is running).
* **Django 4.2** — Web framework for the project.

### Steps to run the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saidrem/online_library.git
   cd online_library
   ```

2. **Create and activate a virtual environment:**

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For Linux/Mac:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL:**

   * Create a database and user in PostgreSQL:

     ```bash
     psql -U postgres
     CREATE DATABASE online_library;
     CREATE USER online_user WITH PASSWORD 'your_password';
     ALTER ROLE online_user SET client_encoding TO 'utf8';
     ALTER ROLE online_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE online_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE online_library TO online_user;
     ```

   * Edit the `settings.py` in your Django project to configure PostgreSQL as the database:

     In `online_library/settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'online_library',
             'USER': 'online_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   * Open `http://127.0.0.1:8000/` in your browser to view the online library.
   * Admin panel is available at `http://127.0.0.1:8000/admin/`.

---

## 🖥 Admin Panel

To access the admin panel:

* Go to `http://127.0.0.1:8000/admin/` and login using the superuser credentials created in the previous step.

---

## 📂 Project Structure

```
online_library/
│
├── online_library/             ← Core project files
│   ├── settings.py            ← Django project settings
│   ├── urls.py                ← URL routing
│   └── wsgi.py                ← WSGI configuration
│
├── book/                       ← App for managing books
│   ├── management/             ← Project scripts
│   ├── migrations/             ← Database migrations
│   ├── models.py               ← Model definitions for books
│   ├── views.py                ← Views for listing and filtering books
│   ├── templates/              ← HTML templates for displaying books
│   ├── static/                 ← Static files (CSS, JS)
│   ├── converters.py           ← Custom date converter for URL
│   └── urls.py                 ← URL routing for the book app
│
├── manage.py                   ← Django's command line utility
├── requirements.txt            ← Python dependencies
└── README.md                   ← This file
```

---

## 📝 Usage

* **Viewing Books**: On the homepage (`/books/`), all books will be displayed.
* **Filter by Date**: You can view books by specific publication dates using URLs in the format `/books/YYYY-MM-DD/`.
* **Navigation**: Links to previous and next dates allow you to navigate through the catalog.

---

## 💡 Features

* View all books in the library.
* Paginate through books.
* Navigate between books on specific dates.
* Access the admin panel to add, edit, or delete books.

---

## 💬 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

---

## 📜 License

This project is licensed under the MIT License.

---
