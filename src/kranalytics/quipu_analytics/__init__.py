"""
Quipu Analytics Suite - Core Utilities Package

Provides shared utilities for the 29-domain Analytics Model Matrix framework.
"""

from .execution_tracking import (
    finalize_notebook_tracking,
    get_execution_summary,
    list_recent_executions,
    quick_track,
    setup_notebook_tracking,
)

__version__ = "1.0.0"
__all__ = [
    "setup_notebook_tracking",
    "finalize_notebook_tracking",
    "get_execution_summary",
    "list_recent_executions",
    "quick_track",
]
