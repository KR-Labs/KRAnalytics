"""Tests for KRAnalytics tutorial notebooks."""

import json
from pathlib import Path
import pytest


def test_notebooks_exist(notebooks_dir):
    """Test that example notebooks exist."""
    notebooks = list(notebooks_dir.glob("*.ipynb"))
    assert len(notebooks) >= 5, "Should have at least 5 tutorial notebooks"


def test_notebook_structure(notebook_files):
    """Test that all notebooks have valid structure."""
    for nb_path in notebook_files:
        with open(nb_path, 'r') as f:
            nb = json.load(f)
        
        # Validate notebook structure
        assert 'cells' in nb, f"{nb_path.name}: Missing 'cells' key"
        assert 'metadata' in nb, f"{nb_path.name}: Missing 'metadata' key"
        assert isinstance(nb['cells'], list), f"{nb_path.name}: 'cells' should be a list"
        
        # Check for at least one markdown cell
        markdown_cells = [c for c in nb['cells'] if c.get('cell_type') == 'markdown']
        assert len(markdown_cells) > 0, f"{nb_path.name}: No markdown cells found"


def test_notebooks_no_errors(notebook_files):
    """Test that notebooks don't contain error outputs."""
    for nb_path in notebook_files:
        with open(nb_path, 'r') as f:
            nb = json.load(f)
        
        # Check for error outputs
        for i, cell in enumerate(nb.get('cells', [])):
            if cell.get('cell_type') == 'code':
                outputs = cell.get('outputs', [])
                for output in outputs:
                    assert output.get('output_type') != 'error', \
                        f"{nb_path.name} cell {i+1}: Contains error output"


def test_sample_data_exists(data_dir):
    """Test that sample datasets exist."""
    assert data_dir.exists(), "Sample datasets directory should exist"
    
    # Check for key sample files
    expected_files = [
        'census_income_2022.csv',
        'census_inequality_2022.csv',
        'bls_employment_national.csv',
        'fbi_crime_stats_sample.csv'
    ]
    
    for filename in expected_files:
        filepath = data_dir / filename
        assert filepath.exists(), f"Missing sample data file: {filename}"
