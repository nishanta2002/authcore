from fastapi import FastAPI
from app.schemas import UserRegister
from app.db.database import engine, SessionLocal
from app.db.models import User
from app.security import hash_password

app = FastAPI(
    title="AuthCore API",
    version="1.0.0",
    description="Authentication Service for Project Titan",
    contact= {
                "name": "Titan Labs"
            }
)

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "AuthCore",
        "version": "1.0.0",
        
    }
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AuthCore",
        "version": "1.0.0"
    }
@app.post("/register")
def register(user: UserRegister):
    db = SessionLocal()
    new_user = User(
        name = user.name,
        email = user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    print("USER SAVED:", new_user.id)

    return{
        "messege":"Registration request received",
        "name" : user.name,
        "email": user.email
    }
