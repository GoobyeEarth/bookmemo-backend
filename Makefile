flake:
	flake8 ./

flake-format:
	pyformat -r -i ./
	flake8 ./

test:
	python manage.py test

