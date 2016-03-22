"""
flask-alchy
===========

Flask extension for alchy (The declarative companion to SQLAlchemy).

Documentation: https://github.com/dgilland/flask-alchy
"""

from setuptools import setup

setup(
    name='Flask-Alchy',
    version='0.5.0',
    url='https://github.com/dgilland/flask-alchy',
    license='MIT',
    author='Derrick Gilland',
    author_email='dgilland@gmail.com',
    description='Flask extension for alchy',
    long_description=__doc__,
    py_modules=['flask_alchy'],
    install_requires=[
        'alchy>=2.2.0',
        'Flask-SQLAlchemy>=2.1.0'
    ],
    test_suite='test_flask_alchy',
    keywords='flask alchy sqlalchemy databases',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Flask',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
