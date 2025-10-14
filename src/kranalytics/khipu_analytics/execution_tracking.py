#!/usr/bin/env python3
"""
Execution Tracking Module for Khipu Analytics Suite

Provides comprehensive execution metadata tracking, provenance logging,
and reproducibility support for all notebooks in the 29-domain Analytics Model Matrix.

Features:
- Unique execution ID generation
- Environment metadata capture (Python version, platform, packages)
- Timestamp tracking (start, end, duration)
- Random seed management for reproducibility
- Execution log persistence (JSON format)
- Integration with notebook registry

Author: Khipu Analytics Suite
Date: 2025-10-13
Version: 1.0
"""

import hashlib
import json
import os
import platform
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def setup_notebook_tracking(
    notebook_name: str,
    version: str = "v1.0",
    seed: int = 42,
    save_log: bool = True,
    advanced_analytics: bool = False,
) -> Dict[str, Any]:
    """
    Initialize execution tracking for a notebook.

    Args:
        notebook_name: Name of the notebook being executed
        version: Notebook version string
        seed: Random seed for reproducibility (default: 42)
        save_log: Whether to save execution log to disk
        advanced_analytics: Whether notebook uses Tier 4-6 advanced methods

    Returns:
        Dictionary with execution metadata

    Example:
        >>> metadata = setup_notebook_tracking(
        ...     notebook_name="Tier2_Income_Prediction_ACS.ipynb",
        ...     version="v1.0",
        ...     seed=42,
        ...     save_log=True
        ... )
        >>> print(metadata['execution_id'])
        'exec_20251013_143022_a3f7d9'
    """
    # Generate unique execution ID
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_hash = hashlib.md5(f"{notebook_name}{timestamp}".encode()).hexdigest()[:6]
    execution_id = f"exec_{timestamp}_{unique_hash}"

    # Set random seeds for reproducibility
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import random

        random.seed(seed)
    except ImportError:
        pass

    # Capture environment metadata
    metadata = {
        "execution_id": execution_id,
        "notebook_name": notebook_name,
        "version": version,
        "start_time": datetime.now().isoformat(),
        "seed": seed,
        "advanced_analytics": advanced_analytics,
        "environment": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "platform_system": platform.system(),
            "platform_release": platform.release(),
            "processor": platform.processor(),
            "machine": platform.machine(),
        },
        "workspace": {"cwd": str(Path.cwd()), "home": str(Path.home())},
        "packages": _get_installed_packages(),
    }

    # Save execution log if requested
    if save_log:
        log_dir = Path.cwd().parent.parent / "logs" / "execution"
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"{execution_id}.json"

        try:
            with open(log_file, "w") as f:
                json.dump(metadata, f, indent=2)
            metadata["log_file"] = str(log_file)
        except Exception as e:
            print(f"⚠️  Warning: Could not save execution log: {e}")
            metadata["log_file"] = None

    return metadata


def finalize_notebook_tracking(
    metadata: Dict[str, Any],
    results: Optional[Dict[str, Any]] = None,
    errors: Optional[list] = None,
) -> Dict[str, Any]:
    """
    Finalize execution tracking with results and timing.

    Args:
        metadata: Execution metadata from setup_notebook_tracking()
        results: Dictionary of execution results (models, metrics, etc.)
        errors: List of errors encountered during execution

    Returns:
        Complete execution metadata with timing and results

    Example:
        >>> metadata = finalize_notebook_tracking(
        ...     metadata,
        ...     results={'best_model': 'RandomForest', 'r2_score': 0.89},
        ...     errors=[]
        ... )
    """
    end_time = datetime.now()
    start_time = datetime.fromisoformat(metadata["start_time"])
    duration = (end_time - start_time).total_seconds()

    metadata["end_time"] = end_time.isoformat()
    metadata["duration_seconds"] = duration
    metadata["duration_formatted"] = _format_duration(duration)
    metadata["status"] = "success" if not errors else "completed_with_errors"

    if results:
        metadata["results"] = results

    if errors:
        metadata["errors"] = errors
        metadata["error_count"] = len(errors)
    else:
        metadata["error_count"] = 0

    # Update log file if it exists
    if metadata.get("log_file"):
        try:
            with open(metadata["log_file"], "w") as f:
                json.dump(metadata, f, indent=2)
        except Exception as e:
            print(f"⚠️  Warning: Could not update execution log: {e}")

    return metadata


def _get_installed_packages() -> Dict[str, str]:
    """Get versions of key installed packages."""
    packages = {}

    package_list = [
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "scikit-learn",
        "scipy",
        "statsmodels",
        "joblib",
        "requests",
        "nbformat",
        "pyarrow",
        # Advanced packages
        "dowhy",
        "causalml",
        "fairlearn",
        "nashpy",
        "mesa",
        "pymc3",
        "hmmlearn",
    ]

    for package in package_list:
        try:
            if package == "scikit-learn":
                import sklearn

                packages[package] = sklearn.__version__
            else:
                mod = __import__(package)
                packages[package] = getattr(mod, "__version__", "unknown")
        except ImportError:
            packages[package] = "not_installed"

    return packages


def _format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    else:
        hours = seconds / 3600
        return f"{hours:.1f} hours"


def get_execution_summary(
    execution_id: str, log_dir: Optional[Path] = None
) -> Optional[Dict[str, Any]]:
    """
    Retrieve execution summary from log file.

    Args:
        execution_id: Execution ID to retrieve
        log_dir: Directory containing execution logs (optional)

    Returns:
        Execution metadata dictionary or None if not found
    """
    if log_dir is None:
        log_dir = Path.cwd().parent.parent / "logs" / "execution"

    log_file = log_dir / f"{execution_id}.json"

    if not log_file.exists():
        print(f"❌ Execution log not found: {log_file}")
        return None

    try:
        with open(log_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading execution log: {e}")
        return None


def list_recent_executions(limit: int = 10, log_dir: Optional[Path] = None) -> list:
    """
    List recent notebook executions.

    Args:
        limit: Maximum number of executions to return
        log_dir: Directory containing execution logs (optional)

    Returns:
        List of execution metadata dictionaries
    """
    if log_dir is None:
        log_dir = Path.cwd().parent.parent / "logs" / "execution"

    if not log_dir.exists():
        print(f"ℹ️  No execution logs found in {log_dir}")
        return []

    log_files = sorted(log_dir.glob("exec_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)

    executions = []
    for log_file in log_files[:limit]:
        try:
            with open(log_file, "r") as f:
                executions.append(json.load(f))
        except Exception as e:
            print(f"⚠️  Error reading {log_file.name}: {e}")

    return executions


# Convenience function for quick setup
def quick_track(notebook_name: str, **kwargs) -> Dict[str, Any]:
    """Quick setup with sensible defaults."""
    return setup_notebook_tracking(notebook_name, **kwargs)


if __name__ == "__main__":
    # Example usage
    print("🔬 Execution Tracking Module - Test")
    print("=" * 60)

    # Test tracking setup
    metadata = setup_notebook_tracking(
        notebook_name="Test_Notebook.ipynb", version="v1.0", seed=42, save_log=True
    )

    print(f"✅ Execution ID: {metadata['execution_id']}")
    print(f"📅 Start Time: {metadata['start_time']}")
    print(f"🐍 Python: {metadata['environment']['python_version']}")
    print(f"💻 Platform: {metadata['environment']['platform']}")
    print(f"📦 Packages tracked: {len(metadata['packages'])}")

    # Simulate some work
    import time

    time.sleep(1)

    # Finalize tracking
    metadata = finalize_notebook_tracking(metadata, results={"test_metric": 0.95}, errors=[])

    print(f"\n✅ Execution complete")
    print(f"⏱️  Duration: {metadata['duration_formatted']}")
    print(f"📄 Log file: {metadata.get('log_file', 'N/A')}")
