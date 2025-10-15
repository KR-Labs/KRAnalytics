# Contributing to KRAnalytics

Thank you for your interest in contributing to KRAnalytics! This guide provides everything you need to know to contribute effectively to the project.

##  How to Contribute

There are many ways to contribute to KRAnalytics:

- ** Bug Reports**: Report issues you encounter
- ** Feature Requests**: Suggest new capabilities
- ** Documentation**: Improve guides and examples
- ** Code Contributions**: Implement features and fixes
- ** Sample Data**: Contribute datasets for examples
- ** Testing**: Add test coverage
- ** Examples**: Create tutorial notebooks

##  Getting Started

### 1. Set Up Development Environment

```bash
# Clone the repository
git clone https://github.com/KR-Labs/KRAnalytics.git
cd KRAnalytics

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
make install-dev
# Or: pip install -e ".[dev,ml,viz]"

# Install pre-commit hooks
pre-commit install
```

### 2. Verify Installation

```bash
# Run tests to ensure everything works
make test

# Check code formatting
make lint

# Verify package import
python -c "from kranalytics import __version__; print(f'v{__version__}')"
```

##  Development Workflow

### 1. Before You Start

1. **Check existing issues** to avoid duplicating work
2. **Open an issue** to discuss major changes
3. **Fork the repository** for your contributions
4. **Create a feature branch** from `main`

### 2. Making Changes

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Run tests and linting
make test
make lint

# Format code
make format

# Commit changes
git add .
git commit -m "Add: Your descriptive commit message"
```

### 3. Submitting Changes

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub with:
   - Clear description of changes
   - Reference to related issues
   - Testing instructions

##  Testing Guidelines

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
pytest tests/unit/test_data_utils.py -v

# Run specific test
pytest tests/unit/test_data_utils.py::test_load_sample_data -v
```

### Writing Tests

1. **Unit Tests**: Test individual functions
   ```python
   # tests/unit/test_data_utils.py
   def test_load_sample_data():
       df = load_sample_data('census_income_2022')
       assert df is not None
       assert len(df) > 0
   ```

2. **Integration Tests**: Test end-to-end workflows
   ```python
   # tests/integration/test_notebook_execution.py
   def test_notebook_runs_without_api_keys():
       # Test that notebooks work with sample data
       pass
   ```

3. **Sample Data Tests**: Ensure fallback mechanisms work
   ```python
   # tests/sample_data/test_fallback.py
   def test_fallback_when_no_api_key():
       # Test graceful degradation
       pass
   ```

##  Code Style Guidelines

### Python Code Style

We follow PEP 8 with some specific guidelines:

```python
# Use type hints
def load_data(api_key: str, year: int = 2022) -> pd.DataFrame:
    """
    Load data with type hints.
    
    Args:
        api_key: API authentication key
        year: Data year to retrieve
        
    Returns:
        DataFrame with loaded data
    """
    pass

# Use descriptive variable names
median_household_income = df['income'].median()
unemployment_rate_by_state = df.groupby('state')['unemployment'].mean()

# Follow docstring conventions
def complex_function(param1: str, param2: int) -> dict:
    """
    One-line summary of the function.
    
    Longer description if needed, explaining the purpose
    and any important details.
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param1 is invalid
        
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result)
        {'status': 'success'}
    """
    pass
```

### Notebook Guidelines

1. **Clear Structure**: Use consistent cell organization
2. **Documentation**: Include markdown cells explaining each step
3. **Reproducibility**: Use fixed random seeds
4. **Error Handling**: Graceful fallbacks for missing API keys

Example notebook structure:
```python
# Cell 1: Setup and imports
import pandas as pd
from kranalytics.data_utils import load_data_with_fallback

# Cell 2: Data loading with fallback
df = load_data_with_fallback(
    api_loader_func=load_census_data,
    dataset_name='census_income_2022',
    api_key_name='CENSUS_API_KEY'
)

# Cell 3: Analysis
# ... analysis code ...

# Cell 4: Visualization
# ... plotting code ...
```

##  Contributing Sample Data

Sample data ensures notebooks work without API keys:

### 1. Creating Sample Data

```python
# scripts/create_sample_data.py
def create_census_sample():
    """Create sample Census data"""
    # Load from API
    df = load_census_data(api_key=api_key, year=2022)
    
    # Sample and anonymize
    df_sample = df.sample(n=1000, random_state=42)
    
    # Save
    df_sample.to_csv('data/sample_datasets/census_income_2022.csv', index=False)
```

### 2. Sample Data Guidelines

- **Size**: Keep files under 10MB
- **Coverage**: Include diverse geographic areas
- **Privacy**: Only public, aggregated data
- **Documentation**: Include data source and methodology

### 3. Required Files

```
data/sample_datasets/
 dataset_name.csv          # The sample data
 dataset_name_metadata.json # Metadata about the sample
 README.md                 # Documentation
```

##  Documentation Contributions

### 1. Types of Documentation

- **API Reference**: Function and class documentation
- **Tutorials**: Step-by-step guides
- **How-to Guides**: Task-oriented instructions
- **Explanations**: Conceptual background

### 2. Documentation Style

```markdown
# Clear Headers

Use descriptive headers that explain what the section covers.

## Code Examples

Always include working code examples:

```python
# This should run without modification
from kranalytics import load_sample_data
df = load_sample_data('census_income_2022')
print(f"Loaded {len(df)} records")
```

## Screenshots

Include screenshots for visual processes, but ensure they don't become outdated quickly.
```

##  Bug Reports

### Good Bug Report Template

```markdown
**Description**
Clear description of the issue

**To Reproduce**
1. Step 1
2. Step 2
3. Error occurs

**Expected Behavior**
What should happen

**Environment**
- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.9.7]
- KRAnalytics: [e.g., 1.0.0]

**Additional Context**
Any other relevant information
```

##  Feature Requests

### Feature Request Template

```markdown
**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should this work?

**Alternatives Considered**
What other approaches did you consider?

**Additional Context**
Examples, mockups, etc.
```

##  Priority Areas

We especially welcome contributions in these areas:

### High Priority
- **Bug fixes** in core functionality
- **Documentation improvements**
- **Test coverage** expansion
- **Sample data** for more domains

### Medium Priority  
- **New data source integrations**
- **Additional visualization types**
- **Performance optimizations**
- **Tutorial notebooks**

### Future Enhancements
- **Dashboard capabilities**
- **Cloud deployment guides**
- **Advanced ML pipelines**
- **Real-time data integration**

##  Recognition

Contributors are recognized in several ways:

- **CONTRIBUTORS.md**: All contributors listed
- **Release Notes**: Major contributions highlighted
- **GitHub**: Contributor badges and stats
- **Documentation**: Author credits on major contributions

##  Getting Help

### Community Channels

- **GitHub Issues**: Technical problems and bugs
- **GitHub Discussions**: Questions and community discussion
- **Email**: info@krlabs.dev for private matters

### Maintainer Response Time

- **Critical bugs**: 24-48 hours
- **Feature requests**: 1-2 weeks
- **Documentation**: 3-5 days
- **General questions**: 2-3 days

##  Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please read and follow it in all interactions.

### Summary

- **Be respectful** and inclusive
- **Be collaborative** and helpful
- **Be patient** with newcomers
- **Be constructive** in feedback

##  Pull Request Checklist

Before submitting a pull request:

- [ ] **Tests pass**: `make test`
- [ ] **Code formatted**: `make format`
- [ ] **Linting passes**: `make lint`
- [ ] **Documentation updated** if needed
- [ ] **CHANGELOG.md updated** for user-facing changes
- [ ] **Sample data provided** for new features if applicable
- [ ] **Commit messages** are descriptive

##  Thank You

Thank you for contributing to KRAnalytics! Your efforts help make socioeconomic data analysis more accessible to researchers, policymakers, and communities worldwide.

---

**Questions?** Reach out via [GitHub Discussions](https://github.com/KR-Labs/KRAnalytics/discussions) or email info@krlabs.dev.

**Last Updated:** October 14, 2025  
**Version:** v1.0.0