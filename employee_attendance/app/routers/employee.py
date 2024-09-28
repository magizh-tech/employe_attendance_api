from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas, models,oauth2
from ..database import get_db

router = APIRouter()



@router.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    db_employee = crud.get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    employees = crud.get_employees(db=db, skip=skip, limit=limit)
    return employees
