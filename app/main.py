from fastapi import FastAPI
from app.database.db import Base, engine
from app.routers import auth, expenses

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])