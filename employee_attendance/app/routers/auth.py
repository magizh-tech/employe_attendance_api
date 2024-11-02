from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas

from .. import database, schemas, models, utils

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.TokenSchema)
def login(user_credentials:schemas.LoginRequestSchema,db: Session = Depends(database.get_db)):

    employee = db.query(models.Employee).filter(models.Employee.email == user_credentials.email).first()

    if not employee:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password,employee.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    

    access_token = oauth2.create_access_token(data ={"employee_id": employee.id})

    return {"access_token": access_token, "Token_type": "bearer"}


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: schemas.EmployeeCreateSchema, db: Session = Depends(database.get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Employee(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/aaa")
def rough(db: Session = Depends(database.get_db)):
    employe=4
    data=db.query(models.Employee).filter(models.Employee.id == employe).first()
    print(data.__dict__)
    print(data.attendance)
    return data