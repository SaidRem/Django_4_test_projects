Here is a `README.md` for your Django project, taking into account that you are using PostgreSQL as your database:


# News Website

This is a Django-based news website that allows users to view articles with associated tags, as well as manage these articles and tags through the Django admin interface. The project supports thematic sections, where each article can have several tags, one of which is marked as the **main tag**.

## 🛠 Technologies

- **Django** (v4.2) — Web framework used to develop the project.
- **PostgreSQL** — Database for storing article data.
- **Python** (v3.x) — Programming language used for backend development.
- **Bootstrap** — Frontend framework for responsive design.

## 📦 Setup

### Prerequisites:
- **Python 3.x**
- **PostgreSQL** — Make sure PostgreSQL is installed and running.
- **Django 4.2** — Web framework for the project.

### Steps to Run the Project:

**Clone the repository:**
```bash
    git clone https://github.com/your-username/news-website.git
    cd news-website
```

**Create and activate a virtual environment:**

For **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
```

For **Linux/Mac**:

```bash
python3 -m venv venv
source venv/bin/activate
```

**Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

**Set up PostgreSQL database:**

   * Log in to PostgreSQL and create the database:

     ```bash
     psql -U postgres
     CREATE DATABASE website_news;
     CREATE USER django_user WITH PASSWORD 'django_user';
     ALTER ROLE django_user SET client_encoding TO 'utf8';
     ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE django_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE website_news TO django_user;
     ```

   * Update the database settings in `settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'website_news',
             'USER': 'django_user',
             'PASSWORD': 'django_user',
             'HOST': 'localhost',
             'PORT': '5432'
         }
     }
     ```

**Apply migrations:**

   ```bash
   python manage.py migrate
   ```

**Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

**Run the development server:**

   ```bash
   python manage.py runserver
   ```

**Access the application:**

   * Open `http://127.0.0.1:8000/` in your browser to view the news website.
   * Admin panel is available at `http://127.0.0.1:8000/admin/`.

---

## 💾 Database Setup (PostgreSQL)

The project uses **PostgreSQL** as the database. The `DATABASES` settings in `settings.py` should match the configuration provided above.

Make sure your PostgreSQL database is up and running. If you are using a different database configuration, modify the `DATABASES` settings accordingly.

---

## 📂 Project Structure

```
news_website/
│
├── articles/                    ← App for managing articles and tags
│   ├── migrations/              ← Database migrations
│   ├── models.py                ← Model definitions for articles, tags, and scopes
│   ├── views.py                 ← Views for listing and displaying articles
│   ├── templates/               ← HTML templates for displaying articles
│   ├── management/              ← Custom Django commands (like loading articles from JSON)
│   │   └── commands/            ← Contains the `load_articles.py` script
│   ├── static/                  ← Static files (CSS, JS)
│   └── urls.py                  ← URL routing for the articles app
│
├── website_news/                ← Core project files
│   ├── settings.py              ← Django settings
│   ├── urls.py                  ← URL routing for the whole project
│   ├── wsgi.py                  ← WSGI configuration
│
├── manage.py                    ← Django's command line utility
├── requirements.txt             ← Python dependencies
└── README.md                    ← This file
```

---

## 📝 Features

* **Article Management**: Admin can add, edit, and delete articles with associated images and tags.
* **Tagging System**: Each article can have multiple tags, with one tag marked as the main tag.
* **Admin Panel**: Django's admin panel is used to manage articles and tags.
* **PostgreSQL**: PostgreSQL is used as the database for this project.
* **JSON Data Import**: Articles can be imported from a JSON file using the `load_articles` command.

---

## 💡 Features

* View all articles on the homepage (`/`).
* Each article displays its content along with its tags.
* Only one tag per article can be marked as the **main** tag.
* Articles can be tagged with multiple thematic sections (tags).

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

### 📌 Notes:

* The **`load_articles.py`** script helps load articles from a JSON file into the database, including their associated tags.
* For **production environments**, replace SQLite with PostgreSQL or MySQL in the `DATABASES` configuration in `settings.py`.
