from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models,oauth2
from ..database import get_db

router = APIRouter(tags=['Attendance'])

@router.post("/employees/{employee_id}/attendance/", response_model=schemas.AttendanceSchema)
def mark_attendance(employee_id: int, attendance: schemas.AttendanceCreateSchema, db: Session = Depends(get_db)):
    return crud.create_attendance(db=db, attendance=attendance, employee_id=employee_id)

@router.get("/employees/{employee_id}/attendance/", response_model=List[schemas.AttendanceSchema])
def read_attendance(employee_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_attendance(db=db, employee_id=employee_id, skip=skip, limit=limit)


@router.get("/employees/attendance/start_day/",response_model=schemas.DayStartSchema)
def start_day(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    return crud.start_day(db=db, employee_id=current_user.id)

