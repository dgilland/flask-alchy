.PHONY: build clean install test release

##
# Variables
##

ENV_NAME = env
ENV_ACT = . env/bin/activate;
PIP = $(ENV_NAME)/bin/pip


##
# Targets
##

build: clean install

clean:
	rm -rf $(ENV_NAME)
	rm -rf .tox
	rm -rf .coverage
	find . -name \*.pyc -type f -delete
	find . -depth -name __pycache__ -type d -exec rm -rf {} \;
	rm -rf dist *.egg* build

install:
	rm -rf $(ENV_NAME)
	virtualenv --no-site-packages $(ENV_NAME)
	$(PIP) install -r requirements.txt

test:
	$(ENV_ACT) py.test --doctest-modules -v -s test_flask_alchy.py

release:
	$(ENV_ACT) python setup.py sdist bdist_wheel
	$(ENV_ACT) twine upload dist/*
	rm -rf dist *.egg* build