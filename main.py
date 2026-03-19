from fastapi import FastAPI
from routes import users, jobs, skills

app = FastAPI()

@app.post('')
def home():
    return {'message': 'Informal worker platform'}

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(skills.router)