from fastapi import APIRouter, Depends
from typing import Annotated

from schemas import STask, STaskAdd, STaskId 
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

@router.post('')
async def add_task(
    task : Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"OK": True, "task_id": task_id}




@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}