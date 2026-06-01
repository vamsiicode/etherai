import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

DB_TYPE = os.getenv('DB_TYPE', 'sqlite').lower()

if DB_TYPE == 'postgres':
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'inventory')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

    SQLALCHEMY_DATABASE_URL = (
        f'postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, future=True)
else:
    SQLITE_PATH = os.getenv('SQLITE_PATH', 'sqlite:///./dev.db')
    SQLALCHEMY_DATABASE_URL = SQLITE_PATH
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={'check_same_thread': False},
        echo=False,
        future=True,
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
