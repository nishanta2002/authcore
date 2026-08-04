from fastapi import FastAPI
from app.schemas import UserRegister

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
    return{
        "messege":"User data recieved"
    }