# KRAnalytics Test Suite

This directory contains tests for the KRAnalytics framework.

## Test Structure

- `conftest.py` - Pytest configuration and fixtures
- `test_notebooks.py` - Notebook validation tests
- `test_utils.py` - Utility function tests (future)
- `test_data.py` - Data loading tests (future)

## Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_notebooks.py

# Run with coverage
pytest tests/ --cov=notebooks --cov-report=html

# Run with verbose output
pytest tests/ -v
```

## Test Requirements

Tests require the following packages:
- pytest
- pytest-cov
- nbformat
- jupyter

Install with:
```bash
pip install pytest pytest-cov nbformat jupyter
```
