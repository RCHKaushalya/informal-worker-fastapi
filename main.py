from fastapi import FastAPI
from routes import users, jobs, skills

app = FastAPI()

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(skills.router)