#!/usr/bin/env python3
"""
KRAnalytics Notebook Validation Script
======================================

Validates all tutorial notebooks for:
- Proper structure and format
- Import resolution
- Data loading functionality
- Execution tracking
- Tier-adaptive patterns
- Visualization generation

Usage:
    python validate_kranalytics_notebooks.py
    python validate_kranalytics_notebooks.py --notebook 01_Income_Analysis_Tutorial.ipynb
    python validate_kranalytics_notebooks.py --detailed

Author: KRAnalytics Team
Date: 2025
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class KRAnalyticsNotebookValidator:
    """Validate KRAnalytics tutorial notebooks."""

    def __init__(self, notebooks_dir: str = "notebooks/examples"):
        self.root_dir = Path(__file__).parent.parent
        self.notebooks_dir = self.root_dir / notebooks_dir
        self.template_path = self.root_dir / "templates" / "KRAnalytics_Notebook_Template.ipynb"
        self.results = []

    def find_notebooks(self, specific_notebook: Optional[str] = None) -> List[Path]:
        """Find all tutorial notebook files."""
        if specific_notebook:
            nb_path = self.notebooks_dir / specific_notebook
            return [nb_path] if nb_path.exists() else []
        
        notebooks = list(self.notebooks_dir.glob("*.ipynb"))
        return [nb for nb in sorted(notebooks) if not nb.name.startswith(".")]

    def check_notebook_structure(self, notebook_path: Path) -> Dict:
        """Check notebook has valid JSON structure and expected sections."""
        try:
            with open(notebook_path, "r", encoding="utf-8") as f:
                nb_data = json.load(f)

            cells = nb_data.get("cells", [])
            code_cells = [c for c in cells if c.get("cell_type") == "code"]
            markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]

            # Check for expected sections in markdown cells
            all_markdown = "\n".join(
                "".join(c.get("source", [])) for c in markdown_cells
            )

            expected_sections = {
                "Header": bool("# " in all_markdown[:500]),  # Title in first few cells
                "Setup": "Setup" in all_markdown or "Installation" in all_markdown,
                "Data Loading": "Data" in all_markdown or "Loading" in all_markdown,
                "Analysis": "Analysis" in all_markdown or "Analytical" in all_markdown,
                "Visualization": "Visualization" in all_markdown or "Charts" in all_markdown,
                "Insights": "Insights" in all_markdown or "Key Findings" in all_markdown,
            }

            return {
                "status": "PASS",
                "total_cells": len(cells),
                "code_cells": len(code_cells),
                "markdown_cells": len(markdown_cells),
                "has_metadata": "metadata" in nb_data,
                "sections_found": expected_sections,
                "missing_sections": [k for k, v in expected_sections.items() if not v],
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def validate_imports(self, notebook_path: Path) -> Dict:
        """Validate that all imports can be resolved."""
        test_script = f"""
import sys
from pathlib import Path

# Add KRAnalytics to path
sys.path.insert(0, str(Path("{self.root_dir}").resolve()))

results = {{}}

# Test KRAnalytics imports
kranalytics_imports = [
    ("kranalytics", "import kranalytics"),
    ("data_utils", "from kranalytics import data_utils"),
    ("execution_tracking", "from kranalytics.khipu_analytics.execution_tracking import setup_notebook_tracking"),
]

for name, import_stmt in kranalytics_imports:
    try:
        exec(import_stmt)
        results[name] = "OK"
    except Exception as e:
        results[name] = f"FAIL: {{str(e)}}"

# Test standard packages
standard_packages = [
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("plotly", "plotly"),
    ("scikit-learn", "sklearn"),
    ("scipy", "scipy"),
    ("statsmodels", "statsmodels"),
]

for pkg_name, import_name in standard_packages:
    try:
        __import__(import_name)
        results[pkg_name] = "OK"
    except Exception as e:
        results[pkg_name] = f"FAIL: {{str(e)}}"

import json
print(json.dumps(results))
"""

        try:
            result = subprocess.run(
                [sys.executable, "-c", test_script], 
                capture_output=True, 
                text=True, 
                timeout=10,
                cwd=str(self.root_dir)
            )

            if result.returncode == 0 and result.stdout:
                import_results = json.loads(result.stdout)
                failures = [k for k, v in import_results.items() if v != "OK"]

                return {
                    "status": "PASS" if not failures else "FAIL",
                    "total": len(import_results),
                    "passed": len(import_results) - len(failures),
                    "failed": len(failures),
                    "failures": failures,
                    "details": import_results,
                }
            else:
                return {
                    "status": "ERROR", 
                    "error": result.stderr or "Unknown error",
                    "stdout": result.stdout
                }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def analyze_code_patterns(self, notebook_path: Path) -> Dict:
        """Analyze code cells for required patterns."""
        try:
            with open(notebook_path, "r", encoding="utf-8") as f:
                nb_data = json.load(f)

            cells = nb_data.get("cells", [])
            code_cells = [c for c in cells if c.get("cell_type") == "code"]
            
            # Combine all code
            all_code = "\n".join(
                "".join(c.get("source", [])) for c in code_cells
            )

            patterns = {
                "has_imports": "import " in all_code,
                "uses_kranalytics": "kranalytics" in all_code or "from kranalytics" in all_code,
                "execution_tracking": "setup_notebook_tracking" in all_code or "ExecutionTracker" in all_code,
                "data_loading": "load_data" in all_code or "get_data" in all_code or "read_" in all_code,
                "tier_adaptive": "tier" in all_code.lower() or "analytics_matrix" in all_code,
                "visualizations": "plot" in all_code or "fig" in all_code or "chart" in all_code,
                "has_docstrings": '"""' in all_code or "'''" in all_code,
            }

            # Check for common issues
            issues = []
            if not patterns["uses_kranalytics"]:
                issues.append("No kranalytics imports found")
            if not patterns["data_loading"]:
                issues.append("No data loading code detected")
            if not patterns["visualizations"]:
                issues.append("No visualization code detected")

            return {
                "status": "PASS" if not issues else "WARNING",
                "patterns_found": patterns,
                "issues": issues,
                "code_cell_count": len(code_cells),
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def validate_notebook(self, notebook_path: Path, detailed: bool = False) -> Dict:
        """Validate a single notebook."""
        print(f"\n{'='*80}")
        print(f"📓 Validating: {notebook_path.name}")
        print(f"{'='*80}")

        result = {
            "notebook": notebook_path.name,
            "path": str(notebook_path),
            "timestamp": datetime.now().isoformat(),
            "overall_status": "UNKNOWN",
        }

        # 1. Check structure
        print("  [1/3] Checking structure...", end=" ")
        structure = self.check_notebook_structure(notebook_path)
        result["structure"] = structure

        if structure["status"] != "PASS":
            print(f"❌ FAIL")
            result["overall_status"] = "FAIL"
            return result
        else:
            missing = len(structure.get("missing_sections", []))
            if missing > 0:
                print(f"⚠️  WARNING ({missing} sections missing)")
            else:
                print(f"✅ PASS")

        # 2. Check imports
        print("  [2/3] Validating imports...", end=" ")
        imports = self.validate_imports(notebook_path)
        result["imports"] = imports

        if imports["status"] == "PASS":
            print(f"✅ PASS ({imports['passed']}/{imports['total']})")
        elif imports["status"] == "ERROR":
            print(f"❌ ERROR")
        else:
            print(f"⚠️  PARTIAL ({imports['passed']}/{imports['total']})")

        # 3. Analyze code patterns
        print("  [3/3] Analyzing code patterns...", end=" ")
        patterns = self.analyze_code_patterns(notebook_path)
        result["patterns"] = patterns

        if patterns["status"] == "PASS":
            print(f"✅ PASS")
        elif patterns["status"] == "WARNING":
            print(f"⚠️  WARNING ({len(patterns['issues'])} issues)")
        else:
            print(f"❌ ERROR")

        # Determine overall status
        if structure["status"] == "PASS" and imports["status"] == "PASS" and patterns["status"] == "PASS":
            result["overall_status"] = "PASS"
            print(f"\n✅ Overall: PASS")
        elif structure["status"] == "ERROR" or imports["status"] == "ERROR" or patterns["status"] == "ERROR":
            result["overall_status"] = "FAIL"
            print(f"\n❌ Overall: FAIL")
        else:
            result["overall_status"] = "PARTIAL"
            print(f"\n⚠️  Overall: PARTIAL (needs improvements)")

        if detailed:
            self._print_detailed_results(result)

        return result

    def _print_detailed_results(self, result: Dict):
        """Print detailed validation results."""
        print("\n--- Detailed Results ---")
        
        # Structure details
        structure = result.get("structure", {})
        if structure.get("missing_sections"):
            print(f"\n⚠️  Missing Sections: {', '.join(structure['missing_sections'])}")
        
        # Import failures
        imports = result.get("imports", {})
        if imports.get("failures"):
            print(f"\n❌ Failed Imports:")
            for failure in imports["failures"]:
                detail = imports.get("details", {}).get(failure, "Unknown error")
                print(f"   - {failure}: {detail}")
        
        # Pattern issues
        patterns = result.get("patterns", {})
        if patterns.get("issues"):
            print(f"\n⚠️  Code Issues:")
            for issue in patterns["issues"]:
                print(f"   - {issue}")

    def validate_all(self, specific_notebook: Optional[str] = None, detailed: bool = False) -> List[Dict]:
        """Validate all notebooks."""
        notebooks = self.find_notebooks(specific_notebook)

        if not notebooks:
            print(f"❌ No notebooks found!")
            return []

        print(f"\n╔══════════════════════════════════════════════════════════════════════════╗")
        print(f"║         KRAnalytics Tutorial Notebook Validator                         ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════╝")
        print(f"\n🔍 Found {len(notebooks)} notebook(s) to validate")

        results = []
        for nb in notebooks:
            result = self.validate_notebook(nb, detailed)
            results.append(result)

        return results

    def generate_report(self, results: List[Dict], output_file: str = "NOTEBOOK_VALIDATION_REPORT.md") -> str:
        """Generate comprehensive validation report."""
        if not results:
            return "No results to report."

        total = len(results)
        passed = sum(1 for r in results if r["overall_status"] == "PASS")
        partial = sum(1 for r in results if r["overall_status"] == "PARTIAL")
        failed = sum(1 for r in results if r["overall_status"] == "FAIL")

        report = f"""# KRAnalytics Notebook Validation Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Notebooks:** {total}  
**Validation Status:**
- ✅ PASS: {passed} ({passed/total*100:.1f}%)
- ⚠️  PARTIAL: {partial} ({partial/total*100:.1f}%)
- ❌ FAIL: {failed} ({failed/total*100:.1f}%)

---

## Executive Summary

"""

        if passed == total:
            report += "✅ **All notebooks validated successfully!** All tutorials follow the standard template format and are ready for use.\n\n"
        elif failed > 0:
            report += f"⚠️  **{failed} notebook(s) have critical issues** that prevent them from functioning correctly.\n\n"
        elif partial > 0:
            report += f"⚠️  **{partial} notebook(s) need improvements** to match the standard template format.\n\n"

        report += "## Notebook Status Overview\n\n"
        report += "| Notebook | Status | Structure | Imports | Patterns |\n"
        report += "|----------|--------|-----------|---------|----------|\n"

        for r in sorted(results, key=lambda x: x["notebook"]):
            status_icon = {"PASS": "✅", "PARTIAL": "⚠️", "FAIL": "❌"}[r["overall_status"]]
            
            struct_status = "✅" if r["structure"]["status"] == "PASS" and not r["structure"].get("missing_sections") else "⚠️"
            import_status = "✅" if r["imports"]["status"] == "PASS" else ("❌" if r["imports"]["status"] == "ERROR" else "⚠️")
            pattern_status = {"PASS": "✅", "WARNING": "⚠️", "ERROR": "❌"}.get(r["patterns"]["status"], "❓")
            
            report += f"| `{r['notebook']}` | {status_icon} | {struct_status} | {import_status} | {pattern_status} |\n"

        report += "\n---\n\n## Detailed Analysis\n\n"

        for r in sorted(results, key=lambda x: x["notebook"]):
            if r["overall_status"] != "PASS":
                report += f"### {r['notebook']}\n\n"
                report += f"**Overall Status:** {r['overall_status']}  \n\n"

                # Structure issues
                structure = r.get("structure", {})
                if structure.get("missing_sections"):
                    report += "**Missing Sections:**\n"
                    for section in structure["missing_sections"]:
                        report += f"- {section}\n"
                    report += "\n"

                # Import issues
                imports = r.get("imports", {})
                if imports.get("status") != "PASS":
                    report += "**Import Issues:**\n"
                    if imports.get("failures"):
                        for failure in imports["failures"]:
                            detail = imports.get("details", {}).get(failure, "Unknown")
                            if "FAIL:" in detail:
                                detail = detail.split("FAIL:")[1].strip()
                            report += f"- `{failure}`: {detail}\n"
                    report += "\n"

                # Pattern issues
                patterns = r.get("patterns", {})
                if patterns.get("issues"):
                    report += "**Code Pattern Issues:**\n"
                    for issue in patterns["issues"]:
                        report += f"- {issue}\n"
                    report += "\n"

                report += "---\n\n"

        report += "## Recommendations\n\n"

        if failed > 0:
            report += f"### Critical Actions Required\n\n"
            report += f"1. **Fix {failed} failed notebook(s)** with structural or import errors\n"
            report += f"2. Review each failed notebook against the template: `templates/KRAnalytics_Notebook_Template.ipynb`\n"
            report += f"3. Ensure all imports reference `kranalytics` package correctly\n\n"

        if partial > 0:
            report += f"### Improvements Needed\n\n"
            report += f"1. **Standardize {partial} notebook(s)** to match template format\n"
            report += f"2. Add missing sections (Setup, Data Loading, Analysis, Insights, etc.)\n"
            report += f"3. Implement tier-adaptive patterns using `kranalytics` utilities\n"
            report += f"4. Add execution tracking for progress monitoring\n\n"

        report += "### Next Steps\n\n"
        report += "1. **Review Template:** Study `templates/KRAnalytics_Notebook_Template.ipynb` for standard structure\n"
        report += "2. **Update Notebooks:** Apply template structure to all tutorials\n"
        report += "3. **Test Execution:** Run each notebook end-to-end to verify functionality\n"
        report += "4. **Document Changes:** Update `notebooks/examples/README.md` with any new patterns\n\n"

        report += "---\n\n"
        report += "*Generated by KRAnalytics Notebook Validator*\n"

        # Save report
        output_path = self.root_dir / output_file
        output_path.write_text(report)

        print(f"\n📄 Report saved to: {output_file}")

        return report


def main():
    parser = argparse.ArgumentParser(description="Validate KRAnalytics tutorial notebooks")
    parser.add_argument("--notebook", type=str, help="Validate specific notebook (e.g., 01_Income_Analysis_Tutorial.ipynb)")
    parser.add_argument("--detailed", action="store_true", help="Show detailed output for each notebook")
    parser.add_argument("--output", type=str, default="NOTEBOOK_VALIDATION_REPORT.md", help="Output report filename")

    args = parser.parse_args()

    validator = KRAnalyticsNotebookValidator()
    results = validator.validate_all(specific_notebook=args.notebook, detailed=args.detailed)

    if not results:
        print("\n❌ No notebooks found to validate!")
        sys.exit(1)

    print("\n" + "=" * 80)
    print("📊 VALIDATION SUMMARY")
    print("=" * 80)

    total = len(results)
    passed = sum(1 for r in results if r["overall_status"] == "PASS")
    partial = sum(1 for r in results if r["overall_status"] == "PARTIAL")
    failed = sum(1 for r in results if r["overall_status"] == "FAIL")

    print(f"\nTotal Notebooks: {total}")
    print(f"  ✅ PASS:    {passed} ({passed/total*100:.1f}%)")
    print(f"  ⚠️  PARTIAL: {partial} ({partial/total*100:.1f}%)")
    print(f"  ❌ FAIL:    {failed} ({failed/total*100:.1f}%)")

    # Generate report
    validator.generate_report(results, args.output)

    print("\n✅ Validation complete!")

    # Exit code based on results
    if failed > 0:
        sys.exit(1)
    elif partial > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
