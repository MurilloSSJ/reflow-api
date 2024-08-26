"""This module contains the routes for the dag module."""

from fastapi import APIRouter
from src.modules.dag.model import DagModel
from src.modules.dag.controller import DagController

router = APIRouter(prefix="/dag", tags=["dags"])

controller = DagController()


@router.get("")
async def list_dags():
    """Returns the list of DAGs in the database."""
    return {"dag_count": 1}


@router.get("/{id}")
async def get_dag(id: str):
    """Returns the DAG with the given ID."""
    return {"templates": 1}


@router.delete("/{id}")
async def delete_dag():
    """Returns the number of failed and successful DAGs."""
    return {"dags_failure": 1, "dags_success": 1}


@router.post("")
async def create_dag(dag: DagModel):
    """Returns the average DAG runtime."""
    return controller.create_dag(dag)
