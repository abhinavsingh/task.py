.PHONY: all clean test package release

all: clean test

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	nosetests -v --with-coverage --cover-package=task --cover-erase --cover-html --nocapture tests

package:
	python setup.py sdist

release:
	python setup.py sdist register upload
