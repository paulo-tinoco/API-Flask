from flask.json import jsonify
from flask.views import MethodView
from flask_restful import reqparse
from werkzeug.security import generate_password_hash
from app.models.Users import Users
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageUsers(MethodView):

    decorators = [authorize]

    def get(self, id=None):
        base = BaseResources(Users)
        if id == None:
            res = base.get_all()
        else:
            res = base.get_first({'id': id})
        return jsonify(res), res['status']
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('role_id', required=True)
        parser.add_argument('status', required=False, default=1)
        data = parser.parse_args()

        data.update({'password': generate_password_hash(data['password'])})
        res = BaseResources(Users).post_data(data)
        return jsonify(res), res['status']

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('email', required=False)
        parser.add_argument('password', required=False)
        parser.add_argument('role_id', required=False)
        parser.add_argument('status', required=False)
        data = parser.parse_args()

        if data['password'] != None:
            data.update({'password': generate_password_hash(data['password'])})
        
        res = BaseResources(Users).update_data({'id': id}, data)
        return jsonify(res), res['status']
        