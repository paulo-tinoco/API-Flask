class BaseError(Exception):

	error_tpl = {
		'error': {
			'status_code': 0,
			'message': ''
		}
	}

	def __init__(self, message=0, status_code=''):
		Exception.__init__(self)
		self.message = message
		self.status_code = status_code

	def to_dict(self):
		self.error_tpl['error'].update(message=self.message, status_code=self.status_code)

		return self.error_tpl