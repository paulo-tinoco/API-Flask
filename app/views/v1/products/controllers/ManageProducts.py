from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.models.Products import Products
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageProducts(MethodView):


    decorators = [authorize]

    def get(self):
        res = BaseResources(Products).get_all()
        return jsonify(res), res['status']

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=int)
        parser.add_argument('status')
        data = parser.parse_args()

        res = BaseResources(Products).post_data(data)
        return jsonify(res), res['status']

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=int)
        parser.add_argument('status')
        data = parser.parse_args()

        res = BaseResources(Products).update_data({'id': id}, data)
        return jsonify(res), res['status']
    
    def delete(self, id):
        res = BaseResources(Products).delete_data({'id': id})
        return jsonify(res), res['status']
