from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///db.sqlite3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    guest_name = Column(String, nullable=False)
    guest_count = Column(Integer, nullable=False)
    reservation_date = Column(DateTime, nullable=False)
    reservation_time = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)

