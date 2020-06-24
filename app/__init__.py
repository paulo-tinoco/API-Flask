import importlib
import os
from flask import Flask
from flask.json import jsonify
from flask_migrate import Migrate
from app.exceptions import *
from app.models import db

def create_app():

    app = Flask(__name__)
    
    # Loading environment settings
    environ = {
        'dev': 'app.settings.DevelopmentConfig',
        'prod': 'app.settings.ProductionConfig'
    }

    conf = environ.get(os.environ.get('FLASK_ENV', default='dev'))
    app.config.from_object(conf)

    # Starting database
    db.init_app(app)
    
    # Starting migration system
    Migrate(app=app, db=db)

    # Registering error handler
    @app.errorhandler(BadRequestError)
    @app.errorhandler(NotFoundError)
    @app.errorhandler(NotAuthorizedError)
    @app.errorhandler(MethodNotAllowedError)
    def handle_error(error):
        return jsonify(error.to_dict()), getattr(error, 'status_code', 1)

    @app.errorhandler(400)
    def custom_handle_error_400(error):
        return jsonify(BadRequestError('Bad Request', error.data['message']).to_dict()), error.code

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(NotFoundError().to_dict()), error.code

    @app.errorhandler(405)
    def not_method(error):
        return jsonify(MethodNotAllowedError().to_dict()), error.code

    # Registering modules automatically
    mod = importlib.import_module('.'.join(conf.split('.')[:-1]))
    env = getattr(mod, conf.split('.')[-1:][0])

    for module in env.MODULES:
        for version in range(1, env.VERSIONS + 1):
            try:
                package = importlib.import_module('app.views.v{}'.format(version))
                app.register_blueprint(
                    getattr(package, 'v{}_{}'.format(version, module)),
                    url_prefix='/api/v{}/{}'.format(version, module)
                )
            except Exception as e:
                print(str(e))

    return app
