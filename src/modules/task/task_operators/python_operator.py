from src.modules.task.task_operators.base_operator import BaseOperator


class PythonTaskOperator(BaseOperator):
    def __init__(self, python_code: str, **kwargs):
        super().__init__(**kwargs)
        self.python_code = python_code
        self.operator = "PythonOperator"

    def get_template(self, tabulation: int = 4):
        return "\tabulation@task\n" + "\tabulationdef {task_id}():\n"
