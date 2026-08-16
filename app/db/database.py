from sqlalchemy import create_engine
from app.db.models import User, Base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:notrealpassword@localhost:5432/authcore"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

with engine.connect() as connection:
    print("Database connection successful!")

