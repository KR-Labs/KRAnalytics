"""
KRAnalytics: Open-Source Socioeconomic Data Science Framework

A comprehensive analytics framework for socioeconomic data science,
providing tools for analysis across domains including income inequality,
labor markets, housing, health outcomes, and education.

Author: Brandon Deloatch
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Brandon Deloatch"
__email__ = "bcdelo@krlabs.dev"
__license__ = "MIT"

# Core imports
from . import data_utils
from . import khipu_analytics

# Version info
version_info = tuple(map(int, __version__.split('.')))

__all__ = [
    "__version__",
    "__author__", 
    "__email__",
    "__license__",
    "version_info",
    "data_utils",
    "khipu_analytics"
]