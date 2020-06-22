from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.models.Orders import Orders
from app.models.ProductOrder import ProductOrder
from app.models.Products import Products
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageProcutOrders(MethodView):

    decorators = [authorize]
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ticket_id', required=True, type=int)
        parser.add_argument('product_id', required=True, type=int)
        parser.add_argument('quantity', required=True, type=int)
        data = parser.parse_args()

        res = BaseResources(ProductOrder).post_data(data)
        return jsonify(res), res['status']
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('quantity', required=False, type=int)
        data = parser.parse_args()

        res = BaseResources(ProductOrder).update_data({'id': id}, data)
        return jsonify(res), res['status']
    
    def delete(self, id):
        res = BaseResources(ProductOrder).delete_data({'id': id})
        return jsonify(res), res['status']
    