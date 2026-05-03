from sqlmodel import SQLModel, create_engine, Session
from config import DATABASE_URL
from models import Job, Thumbnail

engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def create_tables():
    SQLModel.metadata.create_all(engine)

# database session management
def get_session():
    with Session(engine) as session:
        yield session