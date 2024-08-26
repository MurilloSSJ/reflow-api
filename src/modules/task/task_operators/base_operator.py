from typing import Iterable, Union, Optional
from datetime import timedelta


class BaseOperator:
    def __init__(
        self,
        task_id: str,
        owner: str = None,
        email: str | Iterable[str] = None,
        email_on_retry: bool = False,
        email_on_failure: bool = False,
        retries: int = None,
        retry_delay: Union[timedelta, float] = None,
        execution_timeout: timedelta = None,
        max_active_tis_per_dag: int = None,
        max_active_tis_per_dagrun: int = None,
    ):
        self.task_id = task_id
        self.owner = owner
        self.email = email
        self.email_on_retry = email_on_retry
        self.email_on_failure = email_on_failure
        self.retries = retries
        self.retry_delay = retry_delay
        self.execution_timeout = execution_timeout
        self.max_active_tis_per_dag = max_active_tis_per_dag
        self.max_active_tis_per_dagrun = max_active_tis_per_dagrun
