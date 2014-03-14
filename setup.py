"""
flask-alchy
-----

Flask extension for alchy (the SQLAlchemy enhancement library).

Documentation: https://github.com/dgilland/flask-alchy
"""

from setuptools import setup

setup(
    name='flask-alchy',
    version='0.2.1',
    url='https://github.com/dgilland/flask-alchy',
    license='MIT',
    author='Derrick Gilland',
    author_email='dgilland@gmail.com',
    description='Flask extension for alchy',
    long_description=__doc__,
    py_modules=['flask_alchy'],
    install_requires=[
        'alchy>=0.7.0',
        'Flask-SQLAlchemy>=1.0'
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
