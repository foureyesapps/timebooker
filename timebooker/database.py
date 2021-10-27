from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import get_settings

settings = get_settings()


if settings.sqlalchemy_database_url.startswith("postgres://"):
    settings.sqlalchemy_database_url = settings.sqlalchemy_database_url.replace(
        "postgres://", "postgresql://", 1)

engine = create_engine(settings.sqlalchemy_database_url,
                       pool_size=3, max_overflow=0, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
