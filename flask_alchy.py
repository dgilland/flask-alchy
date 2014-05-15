"""Integrate alchy with Flask SQLAlchemy
"""

__version__ = '0.4.0'
__author__ = 'Derrick Gilland <dgilland@gmail.com>'


from flask_sqlalchemy import SQLAlchemy

from alchy import make_declarative_base, QueryModel, ManagerMixin


class Alchy(SQLAlchemy, ManagerMixin):
    """Flask extension that integrates alchy with Flask-SQLAlchemy."""
    def __init__(self,
                 app=None,
                 use_native_unicode=True,
                 session_options=None,
                 Model=None):
        if session_options is None:
            session_options = {}

        session_options.setdefault('query_cls', QueryModel)

        self.Model = Model

        super(Alchy, self).__init__(
            app, use_native_unicode, session_options)

        self.Query = session_options['query_cls']

    def make_declarative_base(self):
        """Override parent function with alchy's"""
        return make_declarative_base(self.session, Model=self.Model)

    def __getattr__(self, attr):
        """Delegate all other attributes to self.session"""
        return getattr(self.session, attr)
