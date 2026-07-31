from fastapi import FastAPI

app = FastAPI(
    title="AuthCore API",
    version="1.0.0",
    description="Authentication Service for Project Titan"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "AuthCore",
        "version": "1.0.0"
    }