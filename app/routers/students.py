from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .. import models
from ..database import SessionLocal

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/students/", response_class=HTMLResponse)
async def read_students(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = db.query(models.Aluno).offset(skip).limit(limit).all()
    return templates.TemplateResponse("students.html", {"request": request, "students": students})
