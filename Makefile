.PHONY: test lint

lint:
	python -m flake8 backend

test:
	pytest -q
