.PHONY: all clean test package release examples

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

examples:
	PYTHONPATH=. python examples/simple_task.py
	PYTHONPATH=. python examples/wait_until_done_task.py
	PYTHONPATH=. python examples/exception_caught.py
	#PYTHONPATH=. python examples/redis_brpop_task.py > /tmp/&
