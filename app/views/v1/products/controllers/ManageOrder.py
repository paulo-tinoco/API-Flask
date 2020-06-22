from flask.globals import g
from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from app.models.Orders import Orders
from app.models.ProductOrder import ProductOrder
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageOrders(MethodView):

    decorators = [authorize]

    def get(self, id):
        res_order = BaseResources(Orders).get_first({'id': id})

        result = {'status': 404}
        if res_order['status'] == 200:
            res_products = BaseResources(
                ProductOrder).get_all({'ticket_id': id})
            result = {
                'status': res_order['status'],
                'user_id': res_order['user_id'],
                'created_at': res_order['created_at'],
                'updated_at': res_order['updated_at'],
                'products': res_products['data']
            }

        return jsonify(result), res_order['status']

    def post(self):
        res = BaseResources(Orders).post_data({'user_id': g.user['id']})
        return jsonify(res), res['status']

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('status')
        data = parser.parse_args()

        res = BaseResources(Orders).update_data({'id': id}, data)
        return jsonify(res), res['status']

    def delete(self, id):
        res_order = BaseResources(Orders).get_first({'id': id})
        if res_order['status'] == 200:
            result = res_order['data'][0]
            res_products = BaseResources(ProductOrder).get_all({'ticket_id': result['id']})
            for row in res_products['data']:
                BaseResources(ProductOrder).delete_data({'id': row['id']})
        
        res_order = BaseResources(Orders).delete_data({'id': id})
        return jsonify(res_order), res_order['status']
    