from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class AttendanceBaseSchema(BaseModel):
    pass

class AttendanceCreateSchema(AttendanceBaseSchema):
    pass

class TokenDataSchema(BaseModel):
    id: Optional[str] = None

class AttendanceSchema(AttendanceBaseSchema):
    id: int
    employee_id: int
    start_day: datetime
    end_day: Optional[datetime]

    class Config:
        from_attributes = True

class EmployeeBaseSchema(BaseModel):
    name: str
    email: str
    department: str

class EmployeeCreateSchema(EmployeeBaseSchema):
    password: str
    
    class Config:
        from_attributes = True

class EmployeeSchema(EmployeeBaseSchema):
    id: int
    attendance: List[AttendanceSchema] = []

    class Config:
        from_attributes = True

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class LoginRequestSchema(BaseModel):
    email: str
    password: str

class BreakCreateSchema(BaseModel):
    start_break: datetime
    end_break: datetime
    reason: str

class BreakStartSchema(BaseModel):
    start_break: datetime
    reason: str

class BreakEndSchema(BaseModel):
    end_break: datetime

class DayStartSchema(BaseModel):
    start_day: datetime

class DayEndSchema(BaseModel):
    end_day: datetime
    work_done: str

class LeaveCreateSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    reason: str

class LeaveResponseSchema(BaseModel):
    id: int
    employee_id: int
    start_date: datetime
    end_date: datetime
    reason: str
    approved: bool

    class Config:
        from_attributes = True
