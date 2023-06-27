.PHONY: install pypi

install:
	@pip install -e .

pypi:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
