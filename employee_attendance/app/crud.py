from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, utils

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
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

