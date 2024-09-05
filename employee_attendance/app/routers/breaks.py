from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import break_crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/employees/{employee_id}/breaks/start", response_model=schemas)
def start_break(employee_id: int, break_: schemas.BreakStart, db: Session = Depends(get_db)):
    return break_crud.create_break(db=db, break_=break_, employee_id=employee_id)

@router.post("/employees/{employee_id}/breaks/end", response_model=schemas)
def end_break(employee_id: int, break_: schemas.BreakCreate, db: Session = Depends(get_db)):
    return break_crud.create_break(db=db, break_=break_, employee_id=employee_id)