from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get('/skills')
def load_skills():
    skill_ref = db.collection('skills')
    skill_stream = skill_ref.stream()

    skills = []

    for skill in skill_stream:
        skill_data = skill.to_dict()
        skills.append(skill_data)
    
    return {'skills': skills}