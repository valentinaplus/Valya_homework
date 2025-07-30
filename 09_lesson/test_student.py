from sqlalchemy import text


def test_add_student(session, student_model):
    student = student_model(first_name="Иван", last_name="Иванов",
                            email="ivan@example.com")
    session.add(student)
    session.commit()

    result = session.execute(text("SELECT * FROM public.student")).fetchall()
    assert len(result) > 0

    found = session.query(student_model).filter_by(
        email="ivan@example.com").first()
    assert found is not None
    assert found.first_name == "Иван"


def test_update_student(session, student_model):
    student = student_model(first_name="Мария", last_name="Петрова",
                            email="maria@example.com")
    session.add(student)
    session.commit()

    student.last_name = "Смирнова"
    session.commit()

    updated = session.query(student_model).filter_by(
        email="maria@example.com").first()
    assert updated.last_name == "Смирнова"


def test_delete_student(session, student_model):
    student = student_model(first_name="Алексей", last_name="Сидоров",
                            email="alex@example.com")
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(student_model).filter_by(
        email="alex@example.com").first()
    assert deleted is None
