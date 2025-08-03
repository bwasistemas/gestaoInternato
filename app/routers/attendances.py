from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/attendances/", response_model=models.Frequencia)
def create_attendance(attendance: models.Frequencia, db: Session = Depends(get_db)):
    db_attendance = models.Frequencia(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@router.get("/attendances/", response_model=list[models.Frequencia])
def read_attendances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    attendances = db.query(models.Frequencia).offset(skip).limit(limit).all()
    return attendances
