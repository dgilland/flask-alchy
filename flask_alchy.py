
__version__ = '0.2.0'

from flask.ext.sqlalchemy import SQLAlchemy

from alchy import make_declarative_base, Query, ManagerBase

class FlaskAlchy(SQLAlchemy, ManagerBase):
    def __init__(self, app=None, use_native_unicode=True, session_options=None, Model=None):
        if session_options is None:
            session_options = {}

        session_options.setdefault('query_cls', Query)

        self.Model = Model

        super(FlaskAlchy, self).__init__(app, use_native_unicode, session_options)

        self.Query = session_options['query_cls']

    def make_declarative_base(self):
        '''Override parent function with alchy's'''
        return make_declarative_base(self.session, Model=self.Model)

    def __getattr__(self, attr):
        '''Delegate all other attributes to self.session'''
        return getattr(self.session, attr)
