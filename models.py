from typing import Literal
from pydantic import BaseModel

from constants import TaskStatus


class AddTaskRequestParams(BaseModel):
    username: str
    taskName: str
    taskContent: str
    status: Literal[TaskStatus.DELAYED, TaskStatus.ON_PROGRESS, TaskStatus.PENDING, TaskStatus.DONE]


