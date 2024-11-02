from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import break_crud, schemas, models
from ..database import get_db

router = APIRouter(tags=['Breaks'])

@router.post("/employees/{employee_id}/breaks/start")
def start_break(employee_id: int, breaka: dict, db: Session = Depends(get_db)):
    return break_crud.create_break(db=db, break_=breaka, employee_id=employee_id)

@router.post("/employees/{employee_id}/breaks/end")
def end_break(employee_id: int, break_: schemas.BreakCreateSchema, db: Session = Depends(get_db)):
    return break_crud.create_break(db=db, break_=break_, employee_id=employee_id)