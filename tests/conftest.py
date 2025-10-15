"""Pytest configuration and shared fixtures for KRAnalytics tests."""

import pytest
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).parent.parent
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks" / "examples"
DATA_DIR = PROJECT_ROOT / "data" / "sample_datasets"


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def notebooks_dir():
    """Return the notebooks directory."""
    return NOTEBOOKS_DIR


@pytest.fixture
def data_dir():
    """Return the data directory."""
    return DATA_DIR


@pytest.fixture
def notebook_files():
    """Return list of all notebook files in examples directory."""
    return list(NOTEBOOKS_DIR.glob("*.ipynb"))
