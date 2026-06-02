from database import SessionLocal
from models import Appointment

def test_get_appointments():
    db = SessionLocal()

    appointments = db.query(Appointment).all()

    assert isinstance(appointments, list)