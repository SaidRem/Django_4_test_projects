# School Website

This is a Django project for a simple school website. The project manages teachers and students, allowing the following functionalities:
- Display a list of students and their teachers.
- Manage teachers and students with a many-to-many relationship.
- A script to populate the database with sample data for teachers and students from a JSON file.

## 📝 Features

- **Teacher Model**: Stores information about the teachers (name and subject).
- **Student Model**: Stores information about the students (name, class, and associated teachers).
- **Many-to-Many Relationship**: A student can have multiple teachers, and a teacher can have multiple students.
- **Data Loading**: A management command `loaddata.py` is included to load data from a JSON file into the database for teachers and students.
- **Simple User Interface**: A page to display the list of students with their respective teachers.

## 🛠 Technologies

- **Django** (v4.2) — Web framework used to develop the project.
- **PostgreSQL** — Database used for development.
- **Python** (v3.x) — Programming language used for backend development.

## 🚀 Installation

### Prerequisites:
- **Python 3.x** 
- **Django 4.2**
- **PostgreSQL**


### Steps to run the project:

**Clone the repository:**
    ```bash
    git clone https://github.com/your-username/school_website.git
    cd school_website
    ```

**Create and activate a virtual environment:**

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

**Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
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

   * Open `http://127.0.0.1:8000/` in your browser to view the school website.
   * Admin panel is available at `http://127.0.0.1:8000/admin/`.

---

## 💾 Management Command to Load Data

This project includes a management command to load teacher and student data from a JSON file. To populate your database with sample data:

1. Place your JSON data file (e.g., `students_and_teachers.json`) in the appropriate directory.

2. Run the command to load the data:

   ```bash
   python manage.py loaddata path/to/your/students_and_teachers.json
   ```

### Example JSON file (`students_and_teachers.json`):

```json
[
  {
    "model": "school.teacher",
    "pk": 1,
    "fields": {
      "name": "Карякин Владимир Владимирович",
      "subject": "Математика"
    }
  },
  {
    "model": "school.teacher",
    "pk": 2,
    "fields": {
      "name": "Наумкин Анатолий Андреевич",
      "subject": "Русский язык"
    }
  },
  {
    "model": "school.teacher",
    "pk": 3,
    "fields": {
      "name": "Филатова Елена Александровна",
      "subject": "Физика"
    }
  },
  {
    "model": "school.student",
    "pk": 1,
    "fields": {
      "name": "Бабаева Вера Ивановна",
      "teacher": 1,
      "group": "8А"
    }
  },
  {
    "model": "school.student",
    "pk": 2,
    "fields": {
      "name": "Погорелов Денис Витальевич",
      "teacher": 3,
      "group": "8А"
    }
  },
  {
    "model": "school.student",
    "pk": 3,
    "fields": {
      "name": "Осипов Иван Вячеславович",
      "teacher": 3,
      "group": "8Б"
    }
  }
]
```

This file will populate the database with sample teachers and students.

---

## 📂 Project Structure

```
school_website/
│
├── school/                     ← App for managing teachers and students
│   ├── migrations/             ← Database migrations
│   ├── models.py               ← Model definitions for teachers and students
│   ├── views.py                ← Views for listing teachers and students
│   ├── templates/              ← HTML templates for displaying students and teachers
│   ├── management/             ← Custom Django commands (like `loaddata.py`)
│   │   └── commands/           ← Contains the `loaddata.py` script
│   ├── static/                 ← Static files (CSS, JS)
│   └── urls.py                 ← URL routing for the school app
│
├── school_website/             ← Core project files
│   ├── settings.py             ← Django settings
│   ├── urls.py                 ← URL routing for the whole project
│   ├── wsgi.py                 ← WSGI configuration
│
├── manage.py                   ← Django's command line utility
├── requirements.txt            ← Python dependencies
└── README.md                   ← This file
```

---

## 📝 Usage

* **Viewing Teachers and Students**: On the homepage (`/`), all students will be displayed with their associated teachers.
* **Loading Data**: The management command `loaddata` can be used to populate the database with sample teacher and student data from a JSON file.

---

## 💡 Features

* View all teachers and students.
* Manage the many-to-many relationship between students and teachers.
* Load sample data from a JSON file using a management command.
* Access the admin panel to add, edit, or delete teachers and students.

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

1. The **`loaddata.py`** script helps load data from the JSON file into the `Teacher` and `Student` models.
2. For **production environments**, replace SQLite with a more robust database like PostgreSQL or MySQL by updating the `DATABASES` configuration in `settings.py`.
