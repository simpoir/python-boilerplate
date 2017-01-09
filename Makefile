help:


test:
	python3-coverage run --source=src setup.py test
	python3-coverage report

.venv:
	virtualenv -p python3 .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python setup.py develop

.PHONY=run
run: .venv
	.venv/bin/hellopy

.phony=coverage
coverage: .venv
	.venv/bin/coverage html -d .htmlcov
	xdg-open .htmlcov/index.html

.phony=lint
lint: .venv
	coala

.PHONY=clean
clean:
	rm -rf .eggs
	rm -rf .coverage
	rm -rf .htmlcov
	rm -rf .venv
