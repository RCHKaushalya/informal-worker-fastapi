from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models import User, Skill
from schemas import UserCreate
from db import get_db

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.nic == user.nic).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="NIC already registered")

    db_user = User(
        nic=user.nic,
        first_name=user.first_name,
        second_name=user.second_name,
        phone=user.phone,
        language = user.language
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "id": db_user.nic,
        "name": db_user.first_name,
        "phone": db_user.phone,
        "language": db_user.language
    }