from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    nic: str
    first_name: str
    second_name: str
    phone: str
    language: str