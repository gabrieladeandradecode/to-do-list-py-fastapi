from pydantic import BaseModel

# This file ensures the Data Structure.

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    class Config: 
        from_attributes = True
    