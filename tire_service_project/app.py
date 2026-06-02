from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import Base, engine, SessionLocal
from models import Appointment

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    db = SessionLocal()

    appointments = db.query(Appointment).all()

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "appointments": appointments
        }
    )


@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):
    return templates.TemplateResponse(
        "add.html",
        {
            "request": request
        }
    )


@app.post("/add")
def add_appointment(
    name: str = Form(...),
    service: str = Form(...),
    date: str = Form(...)
):
    db = SessionLocal()

    appointment = Appointment(
        name=name,
        service=service,
        date=date
    )

    db.add(appointment)
    db.commit()

    return RedirectResponse("/", status_code=303)


@app.get("/delete/{appointment_id}")
def delete_appointment(appointment_id: int):

    db = SessionLocal()

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if appointment:
        db.delete(appointment)
        db.commit()

    return RedirectResponse("/", status_code=303)