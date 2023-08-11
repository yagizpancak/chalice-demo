from chalice import Chalice

from task.routes import task_routes


app = Chalice(app_name='demo-project')

app.register_blueprint(task_routes)
