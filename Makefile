flake:
	flake8 ./

flake-format:
	pyformat -r -i ./

test:
	python manage.py test

