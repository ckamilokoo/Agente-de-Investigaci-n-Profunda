# Archivo principal de FastAPI
# app/main.py
from fastapi import FastAPI
from app.routers import report_generation

app = FastAPI()

app.include_router(report_generation.router)