.PHONY: install install-dev migrate run test lint format clean docs help

help:
	@echo "Available commands:"
	@echo "install      - Install production dependencies"
	@echo "install-dev  - Install development dependencies"
	@echo "migrate      - Run database migrations"
	@echo "run         - Run development server"
	@echo "test        - Run tests"
	@echo "lint        - Run code linting"
	@echo "format      - Format code"
	@echo "clean       - Clean up temporary files"
	@echo "docs        - Generate documentation"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

test:
	pytest

lint:
	flake8 .
	mypy .
	bandit -r .

format:
	black .
	isort .

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +

docs:
	cd docs && make html
