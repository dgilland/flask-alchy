
from unittest import TestCase

from sqlalchemy import Column, types
from sqlalchemy.ext.declarative import declarative_base

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

        self.assertEquals(db.Query, alchy.QueryModel)
        self.assertIsInstance(db.session.query(), alchy.QueryModel)

    def test_override_query_class(self):
        """Test that session query class can be overridden"""
        db = FlaskAlchy(self.app, session_options={'query_cls': BaseQuery})

        self.assertEquals(db.Query, BaseQuery)
        self.assertIsInstance(db.session.query(), BaseQuery)

    def test_model_class(self):
        """Test that model class uses alchy.ModelBase"""
        db = FlaskAlchy(self.app)

        self.assertEquals(db.Model.__dict__['__init__'], alchy.model.ModelBase.__init__)
        self.assertIsInstance(db.Model.__dict__['query'], alchy.query.QueryProperty)

    def test_override_model_class(self):
        """Test that base model class can be overridden with custom class"""
        class MyModelBase(object):
            def testing(self):
                return 'testing'

        Model = declarative_base(cls=MyModelBase)

        class Foo(Model):
            __tablename__ = 'foo'
            _id = Column(types.Integer(), primary_key=True)
            name = Column(types.String())

        db = FlaskAlchy(self.app, Model=Model)

        self.assertTrue(issubclass(db.Model, MyModelBase), 'db.Model should be a subclass of MyModelBase')

        db.create_all()

        self.assertEquals(db.session.query(Foo).all(), Foo.query.all(), 'Model classes should have a query property')

        record = Foo(name='Name')

        self.assertEquals(record.testing(), 'testing')

    def test_flask_alchy_subclasses(self):
        """Test that flask-alchy subclasses from flask-sqlalchemy and alchy"""
        self.assertTrue(issubclass(FlaskAlchy, (SQLAlchemy, alchy.ManagerMixin)))

