import uuid
import pytest
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError


DATABASE_URL = "postgresql://postgres:111@localhost:5432/student"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    level = Column(String, nullable=False)
    education_form = Column(String, nullable=False)
    subject_id = Column(Integer, nullable=False)


@pytest.fixture(scope='module')
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    Base.metadata.create_all(engine)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def student_data():
    return {
        "name": f"Test Student {uuid.uuid4()}",
        "level": "Beginner",
        "education_form": "Group",
        "subject_id": 1
    }


# Тест добавления студента
def test_create_student(db_session, student_data):
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()

    retrieved_student = db_session.query(Student).filter_by(
        name=student_data["name"]).first()
    assert retrieved_student.name == student_data["name"]
    assert retrieved_student.level == student_data["level"]
    assert retrieved_student.education_form == student_data["education_form"]
    assert retrieved_student.subject_id == student_data["subject_id"]


# Тест изменения уровня студента
def test_update_student(db_session, student_data):
    initial_name = student_data['name']
    new_level = "Intermediate"

    # Создаем студента
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()

    # Изменение уровня студента
    student_to_update = db_session.query(Student).filter_by(
        name=initial_name).first()
    student_to_update.level = new_level
    db_session.commit()

    # Проверка обновления
    updated_student = db_session.query(Student).filter_by(
        name=initial_name).first()
    assert updated_student.level == new_level


# Тест удаления студента
def test_delete_student(db_session, student_data):
    initial_name = student_data['name']

    # Создание студента
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()

    # Удаление студента
    student_to_delete = db_session.query(Student).filter_by(
        name=initial_name).first()
    db_session.delete(student_to_delete)
    db_session.commit()

    # Проверка удаления
    deleted_student = db_session.query(Student).filter_by(
        name=initial_name).first()
    assert deleted_student is None
