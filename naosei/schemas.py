from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    cellphone: Optional[str] = None
    email: Optional[str] = None
    username: str
    password: str
