from sqlalchemy.orm import Session
from . import models, schemas, utils




def create_break(db: Session, break_: schemas.BreakStart, employee_id: int):

    db_break = models.Break(**break_.dict(), employee_id=employee_id)
    db.add(db_break)
    db.commit()
    db.refresh(db_break)
    return db_break

