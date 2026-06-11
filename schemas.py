from pydantic import BaseModel

# this file ensures the data structure (their data types).

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    class Config: 
        from_attributes = True
    