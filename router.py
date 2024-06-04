from fastapi import APIRouter, Depends
from typing import Annotated

from schemas import TaskAddSchema, TaskSchema, TasckIdSchema
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks"
)

@router.post('')
async def add_tasks(
    task: Annotated[TaskAddSchema , Depends()],

):
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task id": task_id}


@router.get('')
async def get_tasks():
     tasks = await TaskRepository.get_all()
     return tasks
