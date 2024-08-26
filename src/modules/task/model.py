from pydantic import BaseModel
from typing import Optional, List
from datetime import timedelta
from enum import Enum


class TriggerRule(str, Enum):
    ALL_SUCCESS = "all_success"
    ALL_FAILED = "all_failed"
    ALL_DONE = "all_done"
    ALL_SKIPPED = "all_skipped"
    ONE_SUCCESS = "one_success"
    ONE_DONE = "one_done"
    ONE_FAILED = "one_failed"
    NONE_FAILED = "none_failed"
    NONE_FAILED_MIN_ONE_SUCCESS = "none_failed_min_one_success"
    NONE_SKIPPED = "none_skipped"
    ALWAYS = "always"


class OperatorsChoice(str, Enum):
    BashOperator = "BashOperator"
    PythonOperator = "PythonOperator"
    DummyOperator = "DummyOperator"
    BranchPythonOperator = "BranchPythonOperator"
    ShortCircuitOperator = "ShortCircuitOperator"
    EmailOperator = "EmailOperator"
    SimpleHttpOperator = "SimpleHttpOperator"


class BaseTask(BaseModel):
    task_id: str
    task_group: Optional[str] = None
    dependencies: Optional[List[str]] = []
    operator: OperatorsChoice
    operator_args: dict = {}
    function: Optional[str] = None
    script: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
