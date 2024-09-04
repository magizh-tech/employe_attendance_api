from pydantic import BaseModel
from datetime import datetime
from typing import List

class AttendanceBase(BaseModel):
    date: datetime
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str

class EmployeeCreate(EmployeeBase):
    password: str
    pass

class Employee(EmployeeBase):
    id: int
    attendance: List[Attendance] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token:str
    Token_type: str
