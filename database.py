from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# A URL do banco de dados é lida da variável de ambiente DATABASE_URL.
# Se não estiver definida, usa um padrão para um arquivo 'escola.db' no diretório raiz.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./escola.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} # check_same_thread é necessário apenas para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
