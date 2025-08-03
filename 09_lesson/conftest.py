import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


DATABASE_URL = "postgresql://postgres:111@localhost:5432/student"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()
    session.query(Student).delete()
    session.commit()
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def student_model():
    return Student
