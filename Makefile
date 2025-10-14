.PHONY: install install-dev test lint format clean docs

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,ml,viz]"

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=kranalytics --cov-report=html

lint:
	flake8 src/kranalytics tests/
	mypy src/kranalytics

format:
	black src/kranalytics tests/ scripts/
	isort src/kranalytics tests/ scripts/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov/
	rm -rf dist/ build/ *.egg-info

docs:
	cd docs && make html
