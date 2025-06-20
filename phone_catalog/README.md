# Phone Catalog

The **Phone Catalog** project is a web application for displaying a phone catalog with sorting capabilities and detailed product information.

---

## 📋 Description

Phone Catalog allows users to browse a phone catalog with filtering by various parameters. The application includes features such as:

* Viewing a list of phones  
* Sorting by name and price  
* A detailed product page  

---

## 🛠 Technologies  

* **Django** 4.2 — for web application development.  
* **Bootstrap** — for convenient and responsive layout.  
* **PostgreSQL** — for data storage (or another DBMS of your choice).  

---

## 🚀 Installation  

1. Clone the repository:  

   ```bash  
   git clone https://github.com/saidrem/phone_catalog.git  
   cd phone_catalog  
   ```  

2. Create and activate a virtual environment:  

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

3. Install dependencies:  

   ```bash  
   pip install -r requirements.txt  
   ```  

4. Apply migrations:  

   ```bash  
   python manage.py migrate  
   ```  

5. Create a superuser:  

   ```bash  
   python manage.py createsuperuser  
   ```  

6. Run the server:  

   ```bash  
   python manage.py runserver  
   ```  

7. Visit `http://127.0.0.1:8000/` to view the website.  

---

## 🖥 Admin Panel  

To access the Django admin panel, use the URL:  
`http://127.0.0.1:8000/admin/`  

---

## 📂 Project Structure  

```
phone_catalog/  
│  
├── phone_catalog/            ← Main project directory  
│   ├── settings.py           ← Project settings  
│   ├── urls.py               ← URL routing  
│   └── ...  
│  
├── phones/                   ← "Phones" app  
│   ├── management/           ← Scripts  
│   ├── migrations/           ← Database migrations  
│   ├── models.py             ← Data models  
│   ├── views.py              ← Views  
│   ├── templates/            ← HTML templates  
│   └── static/               ← Static files (CSS, JS)  
│  
├── manage.py                 ← Main project management script  
├── requirements.txt          ← Project dependencies  
└── README.md                 ← This file  
```

---

## ⚙️ Static Files Setup  

Static files (CSS, JavaScript) are placed in the `static/` directory. For production, static files must be collected using the command:  

```bash  
python manage.py collectstatic  
```  

---

## 📝 Running the Data Import Script  

To import phone data from a CSV file into the **Phone** model, follow these steps.  

### 1. Preparing the CSV File  

Prepare a CSV file with phone data, for example:  

```csv  
id;name;image;price;release_date;lte_exists  
1;Samsung Galaxy Edge 2;https://example.com/image.jpg;73000;2016-12-12;True  
2;Iphone X;https://example.com/image2.jpg;80000;2017-06-01;True  
3;Nokia 8;https://example.com/image3.jpg;20000;2013-01-20;False  
```  

### 2. Running the Script  

To import the data, use the Django `manage.py` command to run the custom script. Execute the following command in the terminal:  

```bash  
python manage.py import_phones path/to/your/file.csv  
```  

**Example:**  

```bash  
python manage.py import_phones /home/user/data/phones.csv  
```  

### 3. What the Script Does:  

* The script reads data from the specified CSV file.  
* For each phone (based on its `id`), it either **updates** an existing database record or **creates** a new one if the phone is not found.  
* The script also **generates a slug** for each phone based on its name.  
* All actions are logged, and results can be seen in the console or logs if logging is configured.  

### 4. Notes:  

* Ensure that the **Phone** model has all required fields (`id`, `name`, `price`, `release_date`, `lte_exists`, `slug`).  
* For proper script execution, configure logging if necessary.  

---

### 💡 Example Console Output:  

```
Created: Samsung Galaxy Edge 2  
Updated: Iphone X  
Created: Nokia 8  
```  

---

## 📝 License  

This project is licensed under the MIT License.  
