💰 Expense Tracker API

A RESTful backend API built using FastAPI for managing user authentication and tracking daily expenses.
This project demonstrates backend development skills including API design, authentication, database handling, and deployment.

🚀 Features

User Registration & Login (JWT Authentication)

Add, View, Update & Delete Expenses

Secure API endpoints

Swagger API Documentation

Deployed using serverless architecture

🛠️ Tech Stack

Backend: FastAPI (Python)

Database: SQLite (local development)

ORM: SQLAlchemy

Authentication: JWT (JSON Web Tokens)

Deployment: Vercel (Serverless Functions)

API Docs: Swagger UI

📂 Project Structure
expense_tracker_api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── auth.py
│   │   └── expenses.py
│   ├── schemas/
│   ├── models/
│   └── database.py
├── api/
│   └── index.py
├── requirements.txt
├── vercel.json
└── README.md
▶️ Running Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/expense_tracker_api.git
cd expense_tracker_api
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the server
python -m uvicorn app.main:app --reload
5️⃣ Open API Docs
http://127.0.0.1:8000/docs
🌐 Deployed API

Base URL:
https://your-project-name.vercel.app

Swagger Docs:
https://your-project-name.vercel.app/docs

⚠️ Notes

SQLite is used for development/demo purposes

Vercel serverless functions are stateless

Recommended to use PostgreSQL for production

📌 Future Enhancements

PostgreSQL integration

Role-based access control

Expense analytics & charts

Dockerized deployment

CI/CD pipeline

👩‍💻 Author

Pravallika Malla
Backend Developer | Python | FastAPI

📌 This project is part of my backend portfolio.
