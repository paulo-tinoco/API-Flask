from flask.blueprints import Blueprint
from .urls import load_routes


v1_users = Blueprint('v1_users', __name__)

load_routes(v1_users)
