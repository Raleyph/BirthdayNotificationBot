from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def commit(session: Session):
    try:
        session.commit()
    except SQLAlchemyError:
        return False
    else:
        return True
