from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..import schemas, models, crud
from ..database import get_db



router = APIRouter(tags=['Leave Management'])

@router.post("/leave/{employee_id}/leaves/", response_model=schemas.LeaveResponseSchema)
def apply_for_leave(employee_id: int, leave: schemas.LeaveCreateSchema, db: Session = Depends(get_db)):
    return crud.create_leave(db, leave, employee_id)

@router.get("/employees/{employee_id}/leaves/", response_model=list[schemas.LeaveResponseSchema])
def get_leaves(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_employee_leaves(db, employee_id)

@router.put("/leaves/{leave_id}/approve", response_model=schemas.LeaveResponseSchema)
def approve_leave(leave_id: int, db: Session = Depends(get_db)):
    leave = crud.approve_leave(db, leave_id)
    if leave is None:
        raise HTTPException(status_code=404, detail="Leave not found")
    return leave
