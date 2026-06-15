from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Create tables in PostgreSQL (if not exists)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post('/tasks/', response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)    
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get('/tasks/', response_model= List[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@app.get('/tasks/{task_id}', response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail= 'Invalid task id provided.')
    
    return task


@app.put('/tasks/{task_id}', response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task_queryset = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task_queryset:
        raise HTTPException(status_code=404, detail= 'Task Not Found.')
    
    for key, value in task.model_dump().items():
        setattr(task_queryset, key, value)

    db.commit()
    db.refresh(task_queryset)
    return task_queryset

@app.delete('/tasks/{task_id}', response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail= 'Task Not Found.')

    db.delete(task)
    db.commit()
    return task
