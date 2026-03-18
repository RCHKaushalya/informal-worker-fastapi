from pydantic import BaseModel

class SkillUpdate(BaseModel):
    nic: str
    skills: list[str]

class RegisterUser(BaseModel):
    nic: str
    name: str
    district: str
    ds: str

class AreaUpdate(BaseModel):
    nic: str
    district: str
    ds: str

class PostJob(BaseModel):
    nic:str
    title: str
    description: str
    skills: list[str]

class ListJobs(BaseModel):
    nic: str