from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/employees/{employee_id}/attendance/", response_model=schemas.Attendance)
def create_attendance(employee_id: int, attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.create_attendance(db=db, attendance=attendance, employee_id=employee_id)

@router.get("/employees/{employee_id}/attendance/", response_model=List[schemas.Attendance])
def read_attendance(employee_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_attendance(db=db, employee_id=employee_id, skip=skip, limit=limit)
