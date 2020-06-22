from .controllers import *


def load_routes(module):
    module.add_url_rule('/', view_func=ManageUsers.as_view('ManageUsers'), methods=['GET', 'POST'])
    module.add_url_rule('/<int:id>', view_func=ManageUsers.as_view('ManageUsersID'), methods=['GET', 'PUT'])
    module.add_url_rule('/roles', view_func=ManageRoles.as_view('ManageRoles'), methods=['GET'])
    