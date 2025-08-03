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

@router.get("/specialties/", response_class=HTMLResponse)
async def read_specialties(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    specialties = db.query(models.Especialidade).offset(skip).limit(limit).all()
    return templates.TemplateResponse("specialties.html", {"request": request, "specialties": specialties})
