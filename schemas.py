from pydantic import BaseModel, ConfigDict
from typing import Optional 

class TaskAddSchema(BaseModel):
    name: str
    description: Optional[str] = None


class TaskSchema(TaskAddSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TasckIdSchema(BaseModel):
    ok: bool = True
    task_id: int