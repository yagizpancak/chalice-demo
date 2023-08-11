from http import HTTPStatus

from chalice import Blueprint

from driver import DatabaseClient
from models import AddTaskRequestParams

task_routes = Blueprint(__name__)


@task_routes.route(
    '/add_task',
    methods=["POST"],
    cors=True
)
def add_task():
    data = task_routes.current_app.current_request.json_body
    request = AddTaskRequestParams(**data)

    db = DatabaseClient()
    mongoRes = db.tasks.insert_one({"user":"a"})
    return {"status": "1", "username": request.username}, HTTPStatus.OK
