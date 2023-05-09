from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'sqlite:///square_amano.db'  # Use an SQLite database for simplicity

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
