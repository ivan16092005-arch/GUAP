from database import SessionLocal
from models import Appointment

def test_create_appointment():
    db = SessionLocal()

    appointment = Appointment(
        name="Тестовый клиент",
        service="Замена шин",
        date="01.07.2026"
    )

    db.add(appointment)
    db.commit()

    result = db.query(Appointment).filter(
        Appointment.name == "Тестовый клиент"
    ).first()

    assert result is not None