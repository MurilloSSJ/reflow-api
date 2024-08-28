from src.modules.dag.entity import DagTemplate
from src.modules.dag.model import DagModel
from io import BytesIO


class DagController:
    def __init__(self):
        pass

    def create_dag(self, dag: DagModel):
        dag = DagTemplate(**dag.dict())
        dag_template = dag.get_template()
        file_data = BytesIO()
        file_data.write(dag_template.encode("utf-8"))
        file_data.seek(0)
        return file_data
