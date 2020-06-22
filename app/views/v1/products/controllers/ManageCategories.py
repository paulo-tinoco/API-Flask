from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.models.Categories import Categories
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageCaregories(MethodView):

    decorators = [authorize]

    def get(self):
        res = BaseResources(Categories).get_all()
        return jsonify(res), res['status']

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('product_id', type=int)
        parser.add_argument('status')
        data = parser.parse_args()

        res = BaseResources(Categories).post_data(data)
        return jsonify(res), res['status']

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('product_id', type=int)
        parser.add_argument('status')
        data = parser.parse_args()

        res = BaseResources(Categories).update_data({'id': id}, data)
        return jsonify(res), res['status']

    def delete(self, id):
        res = BaseResources(Categories).delete_data({'id': id})
        return jsonify(res), res['status']
