from enum import Enum


class TaskStatus(str, Enum):
    DELAYED = 'DELAYED'
    ON_PROGRESS = 'ON_PROGRESS'
    PENDING = 'PENDING'
    DONE = 'DONE'
