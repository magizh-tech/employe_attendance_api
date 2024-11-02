from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, utils

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreateSchema):
    hashed_password = utils.hash(employee.password)
    employee.password = hashed_password
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_attendance(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == employee_id).offset(skip).limit(limit).all()

def start_day(db: Session, employee_id: int):
    attendance=models.Attendance(employee_id=employee_id, start_day=datetime.utcnow())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


def create_leave(db: Session, leave: schemas.LeaveCreateSchema, employee_id: int):
    db_leave = models.Leave(
        employee_id=employee_id,
        start_date=leave.start_date,
        end_date=leave.end_date,
        reason=leave.reason,
        approved=False
    )
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave

def get_employee_leaves(db: Session, employee_id: int):
    return db.query(models.Leave).filter(models.Leave.employee_id == employee_id).all()

def approve_leave(db: Session, leave_id: int):
    db_leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
    if db_leave:
        db_leave.approved = True
        db.commit()
        db.refresh(db_leave)
    return db_leave
