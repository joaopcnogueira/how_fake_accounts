.PHONY: install pypi

install:
	@pip install -e .

pypi:
	@rm -rf dist
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
