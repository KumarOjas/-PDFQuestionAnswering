# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db  # Make sure this exists
from .routes import router  # Make sure this exists

# Create a FastAPI instance
app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3001",  # Adjust this to your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()  # Ensure this function is defined in database.py

app.include_router(router)  # Ensure the router is defined in routes.py

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF Question Answering API!"}
