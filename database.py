from curses import echo
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine=create_engine("postgresql://postgres:6nhydvn2M@localhost/item_db",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
