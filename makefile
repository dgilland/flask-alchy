.PHONY: build test release

build:
	rm -rf env
	virtualenv env --python=python2.7
	env/bin/pip install -r requirements.txt

test:
	. env/bin/activate; py.test --doctest-modules -v -s test_flask_alchy.py

release:
	python setup.py sdist upload
	rm -r dist
	rm -r *.egg*