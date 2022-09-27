from curses import echo
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine=create_engine(f"postgresql://postgres:{str(os.getenv('POSTGRESQL_PASSWORD'))}@localhost/item_db",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
