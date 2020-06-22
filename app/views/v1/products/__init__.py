from flask.blueprints import Blueprint
from .urls import load_routes


v1_products = Blueprint('v1_products', __name__)

load_routes(v1_products)
