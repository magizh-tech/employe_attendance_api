from fastapi import FastAPI
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routers import employee, attendance,auth
from fastapi import FastAPI
from .routers import leave_management

models.Base.metadata.create_all(bind=engine)
# metadata is the table that contains the database, engine is the connection
# metadata means data about the database

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your frontend origin
    "http://127.0.0.1:5173",  # Alternative frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(employee.router)
app.include_router(attendance.router)
app.include_router(auth.router)
app.include_router(leave_management.router)

