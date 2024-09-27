from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    department = Column(String)

    attendance = relationship("Attendance")

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date= Column(DateTime, default=datetime.utcnow)
    type= Column(String)
    employee = relationship("Employee", back_populates="attendance")
    # breaks = relationship("Break", back_populates="attendance")
# 
class Break(Base):
    __tablename__ = "breaks"

    id = Column(Integer, primary_key=True, index=True)
    attendance_id = Column(Integer, ForeignKey("attendances.id"))
    start_break = Column(DateTime)  # When the employee starts a break
    end_break = Column(DateTime)  # When the employee ends a break
    reason = Column(String)
    word_done_so_far=Column(String)
    # 
    start_acknowledged_by=Column(Integer, ForeignKey("employees.id"))
    end_acknowledged_by=Column(Integer, ForeignKey("employees.id"))
    start_location=Column(String)
    end_location=Column(String)

    # attendance = relationship("Attendance", back_populates="breaks")


class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    start_date = Column(DateTime)  
    end_date = Column(DateTime)    
    reason = Column(String)        
    status=Column(String) #applied, approved, rejected


    # employee = relationship("Employee", back_populates="leaves")
