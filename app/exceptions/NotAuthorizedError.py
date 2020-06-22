from .BaseError import BaseError

class NotAuthorizedError(BaseError):

    def __init__(self, message='Unauthorized'):
        BaseError.__init__(self)
        self.status_code = 401
        self.message = message

    def to_dict(self):
        self.error_tpl['error'].update(message=self.message, status_code=self.status_code)
        return self.error_tpl
