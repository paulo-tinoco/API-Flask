from functools import wraps
from flask.globals import g
from flask_restful import reqparse
from werkzeug.security import check_password_hash
from app.models.Users import Users
from app.repositories.BaseResources import BaseResources
from app.exceptions import NotAuthorizedError


def authorize(f):
    @wraps(f)
    def decorated_function(**kws):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', location='headers', required=True)
            parser.add_argument('password', location='headers', type=str, required=True)
            data = parser.parse_args()

            user = BaseResources(Users).get_first({'email': data['email']})
            if user['status'] == 404:
                raise NotAuthorizedError()

            response = user['data'][0]
            if check_password_hash(response['password'], data['password']) == False:
                raise NotAuthorizedError()
        
            g.user = response

        except Exception as e:
            raise NotAuthorizedError()
        return f(**kws)
    return decorated_function
