from .BaseError import BaseError

class BadRequestError(BaseError):

    def __init__(self, message='Bad Request', payload=None):
        BaseError.__init__(self)
        self.status_code = 400
        self.message = message
        self.payload = payload

    def to_dict(self):
        self.error_tpl['error'].update(message=self.message, status_code=self.status_code)

        if self.payload is not None:
            self.error_tpl['error'].update({'payload': self.payload})

        return self.error_tpl
