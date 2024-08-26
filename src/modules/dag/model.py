from pydantic import BaseModel
from src.modules.task.model import BaseTask
from typing import List, Optional


class DagModel(BaseModel):
    dag_id: str
    description: Optional[str] = None
    schedule: Optional[str] = None
    schedule_interval: Optional[str] = None
    start_date: Optional[str] = None
    tasks: List[BaseTask] = []
