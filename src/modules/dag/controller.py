from src.modules.dag.entity import DagTemplate
from src.modules.dag.model import DagModel


class DagController:
    def __init__(self):
        pass

    def create_dag(self, dag: DagModel):
        dag = DagTemplate(**dag.dict())
        dag_template = dag.get_template()
        return {"dag_code": dag_template}
