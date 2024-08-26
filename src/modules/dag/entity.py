from typing import Optional, List
from src.modules.task.model import BaseTask


class DagTemplate:
    def __init__(
        self,
        dag_id: str,
        tasks: List[BaseTask] = [],
        task_groups: list = [],
        description: Optional[str] = None,
        schedule=None,
        schedule_interval=None,
        start_date=None,
        end_date=None,
        default_args=None,
        concurrency=None,
        max_active_tasks=None,
        max_active_runs=None,
        max_consecutive_failed_dag_runs=None,
        dagrun_timeout=None,
        catchup=False,
        on_success_callback=None,
        on_failure_callback=None,
        params=None,
        is_paused_upon_creation=None,
    ):
        self.dag_id = dag_id
        self.description = description
        self.schedule = schedule
        self.schedule_interval = schedule_interval
        self.start_date = start_date
        self.end_date = end_date
        self.default_args = default_args
        self.concurrency = concurrency
        self.max_active_tasks = max_active_tasks
        self.max_active_runs = max_active_runs
        self.max_consecutive_failed_dag_runs = max_consecutive_failed_dag_runs
        self.dagrun_timeout = dagrun_timeout
        self.catchup = catchup
        self.on_success_callback = on_success_callback
        self.on_failure_callback = on_failure_callback
        self.params = params
        self.is_paused_upon_creation = is_paused_upon_creation
        self.tasks = tasks
        self.task_groups = task_groups

    def set_imports(self):
        operators = [task.get("operator") for task in self.tasks]
        operators = list(set(operators))
        imports = ""
        for operator in operators:
            if operator == "PythonOperator":
                imports += (
                    "from airflow.operators.python_operator import PythonOperator\n"
                )
            elif operator == "BashOperator":
                imports += "from airflow.operators.bash_operator import BashOperator\n"
            elif operator == "DummyOperator":
                imports += (
                    "from airflow.operators.dummy_operator import DummyOperator\n"
                )
            elif operator == "BranchPythonOperator":
                imports += "from airflow.operators.branch_operator import BranchPythonOperator\n"
            elif operator == "ShortCircuitOperator":
                imports += "from airflow.operators.short_circuit_operator import ShortCircuitOperator\n"
            elif operator == "EmailOperator":
                imports += (
                    "from airflow.operators.email_operator import EmailOperator\n"
                )
            elif operator == "SimpleHttpOperator":
                imports += (
                    "from airflow.operators.http_operator import SimpleHttpOperator\n"
                )
        return imports

    def set_functions_and_scripts(self):
        functions = ""
        for task in self.tasks:
            if task.get("function"):
                functions += task.get("function").replace("\t", "    ") + "\n"
        return functions

    def get_template(self):
        content = "from generics.dag_factory.factory import DagFactory\n"
        content += "from generics.dag_factory.models.task import TaskModel\n"
        content += self.set_imports()
        content += self.set_functions_and_scripts()
        content += "tasks = []\n"
        for task in self.tasks:
            content += (
                f"tasks.append(TaskModel(\n"
                + "**{\n"
                + f"\t'task_id': '{task.get('task_id')}',\n"
                + f"\t'task_group': '{task.get('task_group')}',\n"
                + f"\t'dependencies': {task.get('dependencies')},\n"
                + f"\t'operator': {task.get('operator')},\n"
                + f"\t'operator_args': {task.get('operator_args')},\n"
                + "}\n"
                + "))\n"
            ).replace("\t", "    ")
        content += (
            f"DagFactory(\n"
            + f"\t'{self.dag_id}',"
            + f"tasks,"
            + f"start_date={self.start_date},"
            + f"schedule_interval='{self.schedule_interval}',"
            + f"catchup={self.catchup}"
            + f").register_dag()"
        )
        return content
