from fastapi import APIRouter
from database import db
from models import SkillUpdate, RegisterUser, AreaUpdate, Nic

router = APIRouter()

@router.post("/register")
def register_user(user: RegisterUser):

    nic = user.nic

    doc_ref = db.collection("users").document(nic)

    if doc_ref.get().exists:
        return {"error": "User already exists"}

    doc_ref.set(user.dict())

    return {"message": "User registered"}

@router.post('/update_skills')
def update_skills(update: SkillUpdate):
    user = db.collection('users').document(update.nic)
    doc = user.get()

    if not doc.exists:
        return {'error': 'User not found'}
    
    existing_skills = doc.to_dict().get('skills', [])
    new_skills = list(set(existing_skills + update.skills))
    
    user.update({'skills': new_skills})
    return {'message': 'skills updated successfully'}

@router.post('/update_area')
def update_area(update: AreaUpdate):
    user = db.collection('users').document(update.nic)
    doc = user.get()

    if not doc.exists:
        return {'error': 'User not found'}
    
    user.update({'district': update.district})
    user.update({'ds': update.ds})

    return {'message': 'Area updated successfully'}

@router.post('/user_skills')
def get_user_skills(user: Nic):
    user_ref = db.collection('users').document(user.nic)
    user_doc = user_ref.get()

    if not user_doc.exists:
        return {'error': 'User not found'}

    skills = user_doc.to_dict().get('skills', [])
    return {'skills': skills}