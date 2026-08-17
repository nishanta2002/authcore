from fastapi import FastAPI, Depends, HTTPException
from app.schemas import UserRegister
from app.db.database import get_db
from app.db.models import User
from app.security import hash_password
from sqlalchemy.orm import Session
from sqlalchemy import select

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
def register(user: UserRegister, db: Session = Depends(get_db)):
    result = db.execute(
        select(User).where(User.email == user.email)
    )
    exisiting_user = result.scalar_one_or_none
    if exisiting_user:
        raise HTTPException(
            status_code=400,
            detail="Message : Email is already Registered"
        )
    new_user = User(
        name = user.name,
        email = user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    print("USER SAVED:", new_user.id)

    return{
        "message":"Registration request received",
        "name" : user.name,
        "email": user.email
    }
