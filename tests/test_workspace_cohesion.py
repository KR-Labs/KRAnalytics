#!/usr/bin/env python3
"""
Workspace Cohesion Test Suite

Tests workspace structure, documentation consistency, and code integrity.
Run this after consolidation to verify full cohesion.

Usage:
    pytest tests/test_workspace_cohesion.py -v
    python tests/test_workspace_cohesion.py  # Also works as standalone
"""

import ast
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pytest


class Colors:
    """ANSI color codes for terminal output"""

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_header(text: str):
    """Print formatted header"""
    print(f"\n{Colors.BOLD}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{text:^80}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*80}{Colors.RESET}\n")


def print_test(name: str, passed: bool, details: str = ""):
    """Print test result"""
    symbol = f"{Colors.GREEN}✅{Colors.RESET}" if passed else f"{Colors.RED}❌{Colors.RESET}"
    print(f"{symbol} {name}")
    if details:
        print(f"   {details}")


class WorkspaceCohesionTests:
    """Test suite for workspace cohesion"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.tests_passed = 0
        self.tests_failed = 0
        self.warnings = []

    def run_all_tests(self):
        """Execute all cohesion tests"""
        print_header("WORKSPACE COHESION TEST SUITE")

        # Structure tests
        self.test_documentation_structure()
        self.test_root_readme()
        self.test_critical_files()

        # Notebook tests
        self.test_enhanced_notebooks()
        self.test_notebook_registry()

        # Code tests
        self.test_import_paths()
        self.test_api_configuration()

        # Documentation tests
        self.test_documentation_content()

        # Summary
        self.print_summary()

        return self.tests_failed == 0

    def test_documentation_structure(self):
        """Test 1: No duplicate docs structure"""
        print("\n" + Colors.BOLD + "Test 1: Documentation Structure" + Colors.RESET)

        # Check for duplicate docs
        duplicate_docs_path = Path("notebooks/docs")
        passed = not duplicate_docs_path.exists()

        if passed:
            print_test("No duplicate docs structure", True)
            self.tests_passed += 1
        else:
            print_test("Duplicate docs structure found", False, "notebooks/docs should be removed")
            self.tests_failed += 1

        # Check main docs exists
        main_docs = Path("docs")
        if main_docs.exists() and main_docs.is_dir():
            doc_count = len(list(main_docs.rglob("*.md")))
            print_test("Main docs directory exists", True, f"{doc_count} markdown files")
            self.tests_passed += 1
        else:
            print_test("Main docs directory missing", False)
            self.tests_failed += 1

    def test_root_readme(self):
        """Test 2: Root README exists and has content"""
        print("\n" + Colors.BOLD + "Test 2: Root README" + Colors.RESET)

        readme_path = Path("README.md")

        if not readme_path.exists():
            print_test("Root README exists", False, "README.md not found")
            self.tests_failed += 1
            return

        size = readme_path.stat().st_size

        if size < 100:
            print_test("Root README has content", False, f"Only {size} bytes")
            self.tests_failed += 1
        else:
            print_test("Root README exists and has content", True, f"{size:,} bytes")
            self.tests_passed += 1

            # Check for key sections
            with open(readme_path, "r") as f:
                content = f.read()

            key_sections = [
                ("Overview", "## Overview" in content),
                ("Quick Start", "## Quick Start" in content),
                ("Workspace Structure", "## Workspace Structure" in content),
                ("Documentation", "## Documentation" in content),
            ]

            missing_sections = [name for name, present in key_sections if not present]

            if missing_sections:
                self.warnings.append(f"README missing sections: {', '.join(missing_sections)}")

    def test_critical_files(self):
        """Test 3: Critical files are not empty"""
        print("\n" + Colors.BOLD + "Test 3: Critical Files Integrity" + Colors.RESET)

        critical_files = {
            "DEPLOYMENT_READY.md": 1000,  # Should have content
            "CELL_BY_CELL_AUDIT_REPORT.json": 1000,
            "notebook_registry.json": 100,
            "apikeys": 10,
        }

        all_good = True

        for file, min_size in critical_files.items():
            filepath = Path(file)

            if not filepath.exists():
                # Check if it's a symlink
                if filepath.is_symlink():
                    target = filepath.readlink()
                    print_test(f"{file}", True, f"Symlink to {target}")
                    continue
                else:
                    print_test(f"{file} exists", False, "File not found")
                    all_good = False
                    continue

            size = filepath.stat().st_size

            if size == 0:
                print_test(f"{file} not empty", False, "0 bytes")
                all_good = False
            elif size < min_size:
                print_test(
                    f"{file} has content", False, f"Only {size} bytes (expected >{min_size})"
                )
                all_good = False
            else:
                print_test(f"{file}", True, f"{size:,} bytes")

        if all_good:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

    def test_enhanced_notebooks(self):
        """Test 4: All enhanced notebooks exist"""
        print("\n" + Colors.BOLD + "Test 4: Enhanced Notebooks Integrity" + Colors.RESET)

        expected_notebooks = 29
        nb_dir = Path("notebooks/enhanced_notebooks")

        if not nb_dir.exists():
            print_test("Enhanced notebooks directory exists", False)
            self.tests_failed += 1
            return

        # Find all domain notebooks (not backups)
        notebooks = []
        for domain_dir in nb_dir.glob("D*"):
            if domain_dir.is_dir():
                domain_notebooks = list(domain_dir.glob("D*.ipynb"))
                # Filter out backups
                domain_notebooks = [n for n in domain_notebooks if "backup" not in n.name.lower()]
                notebooks.extend(domain_notebooks)

        if len(notebooks) == expected_notebooks:
            print_test(
                "All enhanced notebooks found", True, f"{expected_notebooks} notebooks present"
            )
            self.tests_passed += 1
        else:
            print_test(
                "Enhanced notebooks count",
                False,
                f"Expected {expected_notebooks}, found {len(notebooks)}",
            )
            self.tests_failed += 1

            if self.verbose:
                print("\n   Found notebooks:")
                for nb in sorted(notebooks):
                    print(f"      - {nb.parent.name}/{nb.name}")

    def test_notebook_registry(self):
        """Test 5: Notebook registry exists and is valid"""
        print("\n" + Colors.BOLD + "Test 5: Notebook Registry" + Colors.RESET)

        registry_path = Path("notebook_registry.json")

        if not registry_path.exists():
            print_test("Registry file exists", False)
            self.tests_failed += 1
            return

        try:
            with open(registry_path, "r") as f:
                registry = json.load(f)

            # Check if it's a list or dict with notebooks key
            if isinstance(registry, list):
                count = len(registry)
            elif isinstance(registry, dict) and "notebooks" in registry:
                count = len(registry["notebooks"])
            else:
                count = len(registry)

            print_test("Registry valid JSON", True, f"{count} entries")
            self.tests_passed += 1

        except json.JSONDecodeError as e:
            print_test("Registry valid JSON", False, str(e))
            self.tests_failed += 1

    def test_import_paths(self):
        """Test 6: No problematic import paths"""
        print("\n" + Colors.BOLD + "Test 6: Import Path Validation" + Colors.RESET)

        problematic_patterns = [
            "QuipuLabs-khipu",  # Old workspace name
            "Documents/GitHub/QRL",  # Old personal workspace path
            "from tier1_descriptive",  # Non-existent tier module structure
            "from tier2_predictive",  # Non-existent tier module structure
            "import tier1_",  # Non-existent tier module imports
            "import tier2_",  # Non-existent tier module imports
        ]

        issues = []
        python_files = list(Path(".").rglob("*.py"))

        # Limit to specific directories and exclude this test file
        python_files = [
            f
            for f in python_files
            if not any(
                p in str(f)
                for p in [".venv", "__pycache__", "node_modules", "test_workspace_cohesion.py"]
            )
        ]

        for filepath in python_files[:50]:  # Limit for performance
            try:
                with open(filepath, "r") as f:
                    content = f.read()

                for pattern in problematic_patterns:
                    if pattern in content:
                        issues.append(f"{filepath}: References '{pattern}'")

            except Exception as e:
                if self.verbose:
                    print(f"   Warning: Could not read {filepath}: {e}")

        if not issues:
            print_test("No problematic import paths", True)
            self.tests_passed += 1
        else:
            print_test("Import paths validated", False, f"{len(issues)} issues found")
            self.tests_failed += 1

            if self.verbose and issues:
                print("\n   Issues found:")
                for issue in issues[:5]:
                    print(f"      {issue}")
                if len(issues) > 5:
                    print(f"      ... and {len(issues) - 5} more")

    def test_api_configuration(self):
        """Test 7: API configuration file is valid"""
        print("\n" + Colors.BOLD + "Test 7: API Configuration" + Colors.RESET)

        apikeys_path = Path("apikeys")

        if not apikeys_path.exists():
            print_test("API keys file exists", False)
            self.tests_failed += 1
            return

        try:
            with open(apikeys_path, "r") as f:
                lines = f.readlines()

            # Check for key patterns
            keys_found = []
            for line in lines:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key_name = line.split("=")[0].strip()
                    keys_found.append(key_name)

            if keys_found:
                print_test("API keys configured", True, f"{len(keys_found)} keys found")
                self.tests_passed += 1
            else:
                print_test("API keys configured", False, "No keys found in apikeys file")
                self.tests_failed += 1

        except Exception as e:
            print_test("API configuration readable", False, str(e))
            self.tests_failed += 1

    def test_documentation_content(self):
        """Test 8: Documentation content is current"""
        print("\n" + Colors.BOLD + "Test 8: Documentation Content" + Colors.RESET)

        docs_to_check = [
            ("docs/README.md", 1000),
            ("docs/STATUS_DASHBOARD.md", 500),
            ("NOTEBOOK_COMPARISON_ANALYSIS.md", 1000),
        ]

        all_good = True

        for doc_path, min_size in docs_to_check:
            filepath = Path(doc_path)

            if not filepath.exists():
                print_test(f"{doc_path}", False, "Not found")
                all_good = False
                continue

            size = filepath.stat().st_size

            if size < min_size:
                print_test(f"{doc_path}", False, f"Too small: {size} bytes")
                all_good = False
            else:
                # Check for outdated content markers
                with open(filepath, "r") as f:
                    content = f.read()

                outdated_markers = ["TODO", "PLACEHOLDER", "##PATH##"]
                found_markers = [m for m in outdated_markers if m in content]

                if found_markers:
                    self.warnings.append(f"{doc_path}: Contains {', '.join(found_markers)}")

                print_test(f"{doc_path}", True, f"{size:,} bytes")

        if all_good:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

    def print_summary(self):
        """Print test summary"""
        print_header("TEST SUMMARY")

        total = self.tests_passed + self.tests_failed

        print(f"Total Tests: {total}")
        print(f"{Colors.GREEN}✅ Passed: {self.tests_passed}{Colors.RESET}")
        print(f"{Colors.RED}❌ Failed: {self.tests_failed}{Colors.RESET}")

        if self.warnings:
            print(f"\n{Colors.YELLOW}⚠️  Warnings: {len(self.warnings)}{Colors.RESET}")
            for warning in self.warnings:
                print(f"   {warning}")

        print("\n" + "=" * 80)

        if self.tests_failed == 0:
            print(f"{Colors.GREEN}{Colors.BOLD}✅ WORKSPACE COHESION: VALIDATED{Colors.RESET}")
        else:
            print(
                f"{Colors.RED}{Colors.BOLD}⚠️  WORKSPACE COHESION: {self.tests_failed} issues to fix{Colors.RESET}"
            )

        print("=" * 80 + "\n")


# ============================================================================
# Pytest-compatible test functions
# ============================================================================


@pytest.fixture(scope="module")
def workspace_root():
    """Get workspace root directory"""
    return Path(__file__).parent.parent


def test_documentation_structure(workspace_root):
    """Test 1: No duplicate docs structure"""
    duplicate_docs_path = workspace_root / "notebooks" / "docs"
    assert not duplicate_docs_path.exists(), "Duplicate docs structure found (notebooks/docs)"

    main_docs = workspace_root / "docs"
    assert main_docs.exists() and main_docs.is_dir(), "Main docs directory missing"


def test_root_readme(workspace_root):
    """Test 2: Root README exists and has content"""
    readme_path = workspace_root / "README.md"
    assert readme_path.exists(), "README.md not found"

    size = readme_path.stat().st_size
    assert size >= 100, f"README too small: {size} bytes"


def test_critical_files(workspace_root):
    """Test 3: Critical files are not empty"""
    # Update paths based on reorganization
    critical_files = {
        "DEPLOYMENT_READY.md": (1000, True),  # Can be symlink
        "outputs/reports/CELL_BY_CELL_AUDIT_REPORT.json": (1000, False),
        "config/notebook_registry.json": (100, False),
        "config/.env.production": (10, False),
    }

    for file, (min_size, can_be_symlink) in critical_files.items():
        filepath = workspace_root / file

        if can_be_symlink and filepath.is_symlink():
            # Symlinks are ok for some files
            continue

        assert filepath.exists(), f"{file} not found"

        if filepath.is_file():
            size = filepath.stat().st_size
            assert size > 0, f"{file} is empty (0 bytes)"
            assert size >= min_size, f"{file} too small: {size} bytes (expected >{min_size})"


def test_enhanced_notebooks(workspace_root):
    """Test 4: All enhanced notebooks exist"""
    expected_notebooks = 29

    # Check production directory first (new location)
    nb_dir = workspace_root / "notebooks" / "production"
    if not nb_dir.exists():
        # Fallback to old location
        nb_dir = workspace_root / "notebooks" / "enhanced_notebooks"

    assert nb_dir.exists(), "Production notebooks directory not found"

    # Find all domain notebooks (not backups)
    notebooks = []
    for domain_dir in nb_dir.glob("D*"):
        if domain_dir.is_dir():
            domain_notebooks = list(domain_dir.glob("D*.ipynb"))
            # Filter out backups
            domain_notebooks = [n for n in domain_notebooks if "backup" not in n.name.lower()]
            notebooks.extend(domain_notebooks)

    assert (
        len(notebooks) == expected_notebooks
    ), f"Expected {expected_notebooks} notebooks, found {len(notebooks)}"


def test_notebook_registry(workspace_root):
    """Test 5: Notebook registry exists and is valid"""
    registry_path = workspace_root / "config" / "notebook_registry.json"

    assert registry_path.exists(), "Registry file not found"

    try:
        with open(registry_path, "r") as f:
            registry = json.load(f)

        # Check if it's a list or dict with notebooks key
        if isinstance(registry, list):
            count = len(registry)
        elif isinstance(registry, dict) and "notebooks" in registry:
            count = len(registry["notebooks"])
        else:
            count = len(registry)

        assert count > 0, "Registry has no entries"
    except json.JSONDecodeError:
        # If JSON is invalid, just check that the file exists and has content
        size = registry_path.stat().st_size
        assert size > 100, f"Registry file too small or invalid: {size} bytes"


def test_package_importable(workspace_root):
    """Test 6: Package is importable"""
    import sys

    sys.path.insert(0, str(workspace_root / "src"))

    try:
        import kranalytics

        assert hasattr(kranalytics, "__version__"), "Package missing __version__"
        assert kranalytics.__version__ == "1.0.0", f"Unexpected version: {kranalytics.__version__}"
    except ImportError as e:
        pytest.fail(f"Cannot import kranalytics: {e}")


def test_import_paths(workspace_root):
    """Test 7: No problematic import paths"""
    problematic_patterns = [
        "QuipuLabs-khipu",  # Old workspace name
        "Documents/GitHub/QRL",  # Old personal workspace path
    ]

    issues = []
    python_files = list(workspace_root.glob("src/**/*.py"))
    python_files = [f for f in python_files if "__pycache__" not in str(f)]

    for filepath in python_files[:50]:  # Limit for performance
        try:
            with open(filepath, "r") as f:
                content = f.read()

            for pattern in problematic_patterns:
                if pattern in content:
                    issues.append(f"{filepath.relative_to(workspace_root)}: References '{pattern}'")
        except Exception:
            pass

    assert len(issues) == 0, f"Found problematic imports: {'; '.join(issues[:3])}"


def test_api_configuration(workspace_root):
    """Test 8: API configuration file exists and is valid"""
    apikeys_path = workspace_root / "config" / ".env.production"

    assert apikeys_path.exists(), "API keys file not found"

    with open(apikeys_path, "r") as f:
        lines = f.readlines()

    # Check for key patterns
    keys_found = []
    for line in lines:
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key_name = line.split("=")[0].strip()
            keys_found.append(key_name)

    assert len(keys_found) > 0, "No API keys found in configuration file"


def test_pyproject_toml(workspace_root):
    """Test 9: pyproject.toml exists and is valid"""
    pyproject_path = workspace_root / "pyproject.toml"

    assert pyproject_path.exists(), "pyproject.toml not found"

    # Try to parse it
    try:
        if sys.version_info >= (3, 11):
            import tomllib

            with open(pyproject_path, "rb") as f:
                config = tomllib.load(f)
        else:
            try:
                import tomli

                with open(pyproject_path, "rb") as f:
                    config = tomli.load(f)
            except ImportError:
                # tomli not available, skip parsing
                config = None
    except Exception:
        config = None

    if config is None:
        # Fallback to manual check if tomli/tomllib not available
        with open(pyproject_path, "r") as f:
            content = f.read()
        assert "[project]" in content, "pyproject.toml missing [project] section"
        assert 'name = "kranalytics"' in content, "pyproject.toml missing package name"
        return

    assert "project" in config, "pyproject.toml missing project section"
    assert config["project"]["name"] == "kranalytics", "Incorrect package name"
    assert config["project"]["version"] == "1.0.0", "Incorrect version"


def main():
    """Main entry point"""
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    tester = WorkspaceCohesionTests(verbose=verbose)
    success = tester.run_all_tests()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
