from flask import Flask
from schedules import run_scheduler
from routes.execution_history import execution_history_blueprint
from routes.error_log import error_log_blueprint

app = Flask(__name__)

app.register_blueprint(execution_history_blueprint)
app.register_blueprint(error_log_blueprint)

if __name__  == '__main__':
    import threading
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    app.run(debug=True)
