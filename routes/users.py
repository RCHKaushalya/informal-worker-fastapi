from fastapi import APIRouter
from database import db

router = APIRouter()

@router.post("/register")
def register_user(user: dict):

    nic = user["nic"]

    doc_ref = db.collection("users").document(nic)

    if doc_ref.get().exists:
        return {"error": "User already exists"}

    doc_ref.set(user)

    return {"message": "User registered"}