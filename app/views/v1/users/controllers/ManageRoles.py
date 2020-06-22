from flask.json import jsonify
from flask.views import MethodView
from app.models.Roles import Roles
from app.repositories.BaseResources import BaseResources
from app.repositories.Security import authorize


class ManageRoles(MethodView):

    decorators = [authorize]

    def get(self):
        res = BaseResources(Roles).get_all()
        return jsonify(res), res['status']
        