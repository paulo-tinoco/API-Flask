from sqlalchemy import exc
from app.models import db


class BaseResources(object):

    def __init__(self, model):
        self.model = model

    def get_all(self, params={}):
        try:
            query = self.model.query.filter_by(**params).all()
            result = [row.serialize for row in query]
            status = 200 if len(result) > 0 else 404
            return {'result': 'sucess', 'data': result, 'status': status}
        except exc.SQLAlchemyError as error:
            return {'result': 'error', 'data': str(error.orig), 'status': 406}
        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
        finally:
            db.session.close()

    def get_first(self, params={}):
        try:
            query = self.model.query.filter_by(**params).first()
            status = 200 if query != None else 404
            return {'result': 'sucess', 'data': [query.serialize], 'status': status}
        except exc.SQLAlchemyError as error:
            return {'result': 'error', 'data': str(error.orig), 'status': 406}
        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
        finally:
            db.session.close()

    def post_data(self, params):
        try:
            query = self.model(**params)
            db.session.add(query)
            db.session.commit()
            return {'result': 'sucess', 'data': [query.serialize], 'status': 201}
        except exc.SQLAlchemyError as error:
            return {'result': 'error', 'data': str(error.orig), 'status': 406}
        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
        finally:
            db.session.close()

    def update_data(self, search, params):
        try:
            query = self.model.query.filter_by(
                **search).update({k: v for k, v in params.items() if v != None})
            db.session.commit()
            return {'result': 'sucess', 'data': 'data successfully updated', 'status': 200}
        except exc.SQLAlchemyError as error:
            return {'result': 'error', 'data': str(error.orig), 'status': 406}
        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
        finally:
            db.session.close()

    def delete_data(self, params):
        try:
            query = self.model.query.filter_by(**params).delete()
            db.session.commit()
            return {'result': 'sucess', 'data': 'data successfully deleted', 'status': 200}
        except exc.SQLAlchemyError as error:
            return {'result': 'error', 'data': str(error.orig), 'status': 406}
        except Exception as e:
            db.session.rollback()
            return {'response': str(e), 'status': 406}
        finally:
            db.session.close()
            