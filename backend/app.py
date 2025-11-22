from flask import Flask
from flask_cors import CORS

from api.api import api
from api.models import db
from api.config import Config


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    api.init_app(app)
    db.init_app(app)


app = create_app(Config)

# --- FIXED SECTION BELOW ---
if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible outside the container
    # port=5000 matches your docker-compose and pipeline settings
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
