from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.configurations import DBConfigurations

Base = declarative_base()

engine = create_engine(
    DBConfigurations.sql_alchemy_db_url,
    encoding="utf-8",
    pool_recycle=3600,
    echo=False,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()
