"""This module contains the routes for the dashboard module."""

from fastapi import APIRouter

router = APIRouter("/dashboard", tags=["dashboard"])


@router.get("/counter/dags")
async def get_dag_counter() -> dict:
    """Returns the number of DAGs in the database.

    Returns:
        dict: The number of DAGs in the database.
    """
    return {"dag_count": 1}


@router.get("/counter/templates")
async def get_task_counter() -> dict:
    """Returns the number of templates in the database.

    Returns:
        dict: The number of templates in the database.
    """
    return {"templates": 1}


@router.get("/counter/users")
async def get_user_counter() -> dict:
    """Returns the number of users in the database.

    Returns:
        dict: The number of users in the database.
    """
    return {"users": 1}


@router.get("/metrics/dags-status")
async def get_dag_failure() -> dict:
    """Returns the number of failed and successful DAGs.

    Returns:
        dict: The number of failed and successful DAGs.
    """
    return {"dags_failure": 1, "dags_success": 1}


@router.get("/metrics/dags-time")
async def get_dag_time() -> dict:
    """Returns the average DAG runtime.

    Returns:
        dict: The average DAG runtime.
    """
    return {
        "jan": 1,
        "feb": 1,
        "mar": 1,
        "apr": 1,
        "may": 1,
        "jun": 1,
        "jul": 1,
        "aug": 1,
        "sep": 1,
        "oct": 1,
        "nov": 1,
        "dec": 1,
    }
