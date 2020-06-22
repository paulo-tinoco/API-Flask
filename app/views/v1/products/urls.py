from .controllers import *


def load_routes(module):
    module.add_url_rule('/', view_func=ManageProducts.as_view('ManageProducts'), methods=['GET', 'POST'])
    module.add_url_rule('/<int:id>', view_func=ManageProducts.as_view('ManageProductID'), methods=['PUT', 'DELETE'])
    module.add_url_rule('/category', view_func=ManageCaregories.as_view('ManageCaregories'), methods=['GET', 'POST'])
    module.add_url_rule('/category/<int:id>', view_func=ManageCaregories.as_view('ManageCaregoryID'), methods=['PUT', 'DELETE'])
    module.add_url_rule('/order', view_func=ManageOrders.as_view('ManageOrders'), methods=['POST'])
    module.add_url_rule('/order/<int:id>', view_func=ManageOrders.as_view('ManageOrderID'), methods=['GET', 'PUT', 'DELETE'])
