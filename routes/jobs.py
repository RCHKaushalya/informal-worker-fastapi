from fastapi import APIRouter
from database import db
from models import PostJob, Nic
from datetime import datetime

router = APIRouter()

@router.post('/post-job')
def post_job(new_job: PostJob):
    user_ref = db.collection('users').document(new_job.nic)
    user_doc = user_ref.get()
    
    if not user_doc.exists:
        return {'error': 'User not found'}
    
    user_data = user_doc.to_dict()
    
    job_ref = db.collection('jobs')
    job_ref.add({
        'posted_by': new_job.nic,
        'title': new_job.title,
        'description': new_job.description,
        'skills': new_job.skills,
        'district': user_data.get('district'),
        'ds': user_data.get('ds'),
        'status': 'open',
        'posted_at': datetime.utcnow()
    })

    return {'message': 'Job posted successfully'}

@router.post('/list-jobs')
def list_jobs(get_job: Nic):
    user_ref = db.collection('users').document(get_job.nic)
    user_doc = user_ref.get()

    if not user_doc.exists:
        return {'error': 'User not found'}
    
    user_data = user_doc.to_dict()

    jobs_ref = db.collection('jobs').where('ds', '==', user_data.get('ds'))
    jobs =  jobs_ref.stream()

    matched_job = []

    for job in jobs:
        job_data = job.to_dict()
        job_skills = job_data.get('skills')

        if set(user_data.get('skills')).intersection(set(job_skills)):
            matched_job.append(job_data)
    
    return {'jobs': matched_job}