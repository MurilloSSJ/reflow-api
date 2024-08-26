from src.main import app
from fastapi.testclient import TestClient
from src.modules.dag.tests.mocks.examples import (
    get_dag_dto_example,
    get_dag_with_task_groups,
)

client = TestClient(app)


def test_create_sample_dag():
    response = client.post("/api/dag", json=get_dag_dto_example())
    assert response.status_code == 200
    assert response.json() == {
        "dag_code": "@dag(\n    dag_id='test_dag',\n)\ndef test_dag():\n    pass\ntest_dag()"
    }


def test_create_dag_with_task_group():
    response = client.post("/api/dag", json=get_dag_with_task_groups())
    assert response.status_code == 200
    dag_code = (
        "@dag(\n\tdag_id='test_dag',\n)\ndef test_dag():\n\tpass\ntest_dag()".replace(
            "\t", "    "
        )
    )
    task_group_code = "\t@task_group(task_group_id='test_task_group')\n\tdef test_task_group():\n\t\tpass\n".replace(
        "\t", "    "
    )
    assert response.json() == {
        "dag_code": f"{dag_code.replace('pass', task_group_code)}"
    }


def test_create_dag_with_tasks():
    response = client.post("/api/dag", json=get_dag_with_tasks())
    assert response.status_code == 200
    dag_code = (
        "@dag(\n\tdag_id='test_dag',\n)\ndef test_dag():\n\tpass\ntest_dag()".replace(
            "\t", "    "
        )
    )
    task_code = "\t@task(task_id='test_task')\n\tdef test_task():\n\t\tpass\n".replace(
        "\t", "    "
    )
    assert response.json() == {"dag_code": f"{dag_code.replace('pass', task_code)}"}
