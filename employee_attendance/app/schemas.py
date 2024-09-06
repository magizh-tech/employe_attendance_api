from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class AttendanceBase(BaseModel):
    # date: datetime
    # status: str
    pass

class AttendanceCreate(AttendanceBase):
    pass


class TokenData(BaseModel):
    id: Optional[str] = None



class Attendance(AttendanceBase):
    id: int
    employee_id: int
    start_day: datetime
    end_day: Optional[datetime]

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

class LoginRequest(BaseModel):
    email: str
    password: str


class BreakStart(BaseModel):
    start_break: datetime
    reason: str

class BreakEnd(BaseModel):
    end_break: datetime
    

class DayStart(BaseModel):
    start_day: datetime

class DayEnd(BaseModel):
    end_day: datetime
    work_done: str


class LeaveCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    reason: str

class LeaveResponse(BaseModel):
    id: int
    employee_id: int
    start_date: datetime
    end_date: datetime
    reason: str
    approved: bool

    class Config:
        orm_mode = True
