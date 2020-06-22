from .BaseError import BaseError

class MethodNotAllowedError(BaseError):

    def __init__(self, message='Method not allowed'):
        BaseError.__init__(self)
        self.status_code = 405
        self.message = message

    def to_dict(self):
        self.error_tpl['error'].update(message=self.message, status_code=self.status_code)
        return self.error_tpl
