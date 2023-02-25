from celery import Celery

app = Celery(
    "fedlearn",
    backend="rpc://",
    broker="pyamqp://myuser:mypassword@10.10.100.1:5672/myvhost",
    include=["fedlearn.tasks"],
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
app.conf.update(
    task_routes = {
        'fedlearn.tasks.train': {'queue': 'trainer1'},
        'fedlearn.tasks.train': {'queue': 'trainer2'},
        'fedlearn.tasks.rollup': {'queue': 'aggr1'},
    },
)
if __name__ == "__main__":
    app.start()