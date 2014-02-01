
# remove once alchy released to pypi
import sys; sys.path.append('../alchy')

from unittest import TestCase

from flask import Flask
from flask.ext.alchy import FlaskAlchy
from flask.ext.sqlalchemy import SQLAlchemy, BaseQuery

import alchy

class TestFlaskAlchy(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    def test_default_query_class(self):
        """Test that session options default to query_cls=alchy.Query"""
        db = FlaskAlchy(self.app)

        self.assertEquals(db.Query, alchy.Query)
        self.assertIsInstance(db.session.query(), alchy.Query)

    def test_override_query_class(self):
        """Test that session query class can be overridden"""
        db = FlaskAlchy(self.app, session_options={'query_cls': BaseQuery})

        self.assertEquals(db.Query, BaseQuery)
        self.assertIsInstance(db.session.query(), BaseQuery)

    def test_model_class(self):
        """Test that model class uses alchy.ModelBase"""
        db = FlaskAlchy(self.app)

        self.assertEquals(db.Model.__dict__['__init__'], alchy.model.ModelBase.__init__)
        self.assertIsInstance(db.Model.__dict__['query'], alchy.model.QueryProperty)

    def test_flask_alchy_subclasses(self):
        """Test that flask-alchy subclasses from flask-sqlalchemy and alchy"""
        self.assertTrue(issubclass(FlaskAlchy, (SQLAlchemy, alchy.ManagerBase)))

