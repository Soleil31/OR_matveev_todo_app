from pydantic import BaseModel
from typing import Optional


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class UpdateTitle(BaseModel):
    title: str


class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        from_attributes = True
