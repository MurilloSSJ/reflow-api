def get_dag_dto_example():
    return {"dag_id": "test_dag", "tasks": [], "task_groups": []}


def get_dag_with_task_groups():
    return {
        "dag_id": "test_dag",
        "tasks": [],
        "task_groups": [
            {
                "task_group_id": "test_task_group",
                "tasks": [],
                "task_groups": [],
            }
        ],
    }


def get_dag_with_tasks():
    return {
        "dag_id": "test_dag",
        "tasks": [
            {
                "task_id": "test_task",
            }
        ],
        "task_groups": [],
    }
