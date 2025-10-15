#!/usr/bin/env python3
"""
Notebook Standardization Script
================================

Systematically updates all tutorial notebooks to match the standard template:
- Replaces old imports with kranalytics package imports
- Adds execution tracking
- Standardizes data loading patterns
- Ensures consistent section structure
- Maintains notebook-specific content

Usage:
    python standardize_notebooks.py
    python standardize_notebooks.py --notebook 01_Income_Analysis_Tutorial.ipynb
    python standardize_notebooks.py --dry-run  # Preview changes without applying

Author: KRAnalytics Team
Date: 2025
"""

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class NotebookStandardizer:
    """Standardize notebooks to match template format."""

    def __init__(self, notebooks_dir: str = "notebooks/examples"):
        self.root_dir = Path(__file__).parent.parent
        self.notebooks_dir = self.root_dir / notebooks_dir
        self.template_path = self.root_dir / "templates" / "KRAnalytics_Notebook_Template.ipynb"
        self.backup_dir = self.root_dir / "backups" / f"notebooks_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    def backup_notebook(self, notebook_path: Path):
        """Create backup of original notebook."""
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = self.backup_dir / notebook_path.name
        shutil.copy2(notebook_path, backup_path)
        print(f"   💾 Backup saved: {backup_path}")

    def get_standard_imports_cell(self) -> Dict:
        """Get standard imports cell from template."""
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "# SETUP & IMPORTS\n",
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "\n",
                "# Standard libraries\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import warnings\n",
                "warnings.filterwarnings('ignore')\n",
                "\n",
                "# Visualization libraries\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import plotly.express as px\n",
                "import plotly.graph_objects as go\n",
                "\n",
                "# Statistical and ML libraries\n",
                "from sklearn.model_selection import train_test_split\n",
                "from sklearn.linear_model import LinearRegression\n",
                "from sklearn.ensemble import RandomForestRegressor\n",
                "from sklearn.metrics import r2_score, mean_absolute_error\n",
                "from scipy import stats\n",
                "import statsmodels.api as sm\n",
                "\n",
                "# KRAnalytics utilities\n",
                "from kranalytics import data_utils\n",
                "from kranalytics.khipu_analytics.execution_tracking import setup_notebook_tracking\n",
                "\n",
                "print(\"✅ All libraries imported successfully\")\n",
                "print(\"📦 KRAnalytics utilities loaded\")\n"
            ]
        }

    def get_execution_tracking_cell(self, domain: str, tier: str) -> Dict:
        """Get execution tracking cell."""
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "# EXECUTION TRACKING\n",
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "\n",
                f"notebook_name = \"{domain}\"\n",
                f"analytics_tier = \"{tier}\"\n",
                "\n",
                "# Initialize tracking\n",
                "tracker = setup_notebook_tracking(notebook_name, analytics_tier)\n",
                "tracker.start_section(\"setup\")\n",
                "\n",
                "print(f\"🎯 Notebook: {notebook_name}\")\n",
                "print(f\"📊 Analytics Tier: {analytics_tier}\")\n",
                "print(\"⏱️  Execution tracking enabled\")\n"
            ]
        }

    def get_data_loading_cell(self, data_source: str = "Census ACS") -> Dict:
        """Get standardized data loading cell."""
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "# DATA LOADING\n",
                "# ═══════════════════════════════════════════════════════════════════════════\n",
                "\n",
                "tracker.start_section(\"data_loading\")\n",
                "\n",
                "# Load data using kranalytics data utilities\n",
                "# This provides automatic fallback: API → Sample Data → Synthetic\n",
                f"data = data_utils.load_data(\"{data_source}\", fallback=True)\n",
                "\n",
                "if data is not None:\n",
                "    print(f\"✅ Data loaded successfully: {len(data)} records\")\n",
                "    print(f\"📋 Columns: {list(data.columns)}\")\n",
                "    display(data.head())\n",
                "else:\n",
                "    print(\"⚠️  Data loading failed - check API keys and configuration\")\n",
                "\n",
                "tracker.end_section(\"data_loading\")\n"
            ]
        }

    def extract_notebook_metadata(self, notebook_path: Path) -> Dict:
        """Extract metadata from existing notebook header."""
        try:
            with open(notebook_path, "r", encoding="utf-8") as f:
                nb_data = json.load(f)
            
            cells = nb_data.get("cells", [])
            if cells and cells[0].get("cell_type") == "markdown":
                header = "".join(cells[0].get("source", []))
                
                # Extract domain, tier, etc.
                metadata = {
                    "domain": "Unknown",
                    "tier": "1-3",
                    "title": notebook_path.stem.replace("_", " ").title()
                }
                
                for line in header.split("\n"):
                    if "Domain" in line and ":" in line:
                        metadata["domain"] = line.split(":", 1)[1].strip()
                    elif "Tier" in line and ":" in line:
                        metadata["tier"] = line.split(":", 1)[1].strip().split()[0]
                    elif line.startswith("# "):
                        metadata["title"] = line[2:].strip()
                
                return metadata
                
        except Exception as e:
            print(f"   ⚠️  Could not extract metadata: {e}")
        
        return {
            "domain": "Unknown",
            "tier": "1-3",
            "title": notebook_path.stem.replace("_", " ").title()
        }

    def standardize_notebook(self, notebook_path: Path, dry_run: bool = False) -> Dict:
        """Standardize a single notebook."""
        print(f"\n{'='*80}")
        print(f"📝 Processing: {notebook_path.name}")
        print(f"{'='*80}")

        result = {
            "notebook": notebook_path.name,
            "status": "UNKNOWN",
            "changes": [],
            "errors": []
        }

        try:
            # Load notebook
            with open(notebook_path, "r", encoding="utf-8") as f:
                nb_data = json.load(f)
            
            cells = nb_data.get("cells", [])
            original_cell_count = len(cells)
            
            # Extract metadata
            metadata = self.extract_notebook_metadata(notebook_path)
            print(f"   📊 Domain: {metadata['domain']}")
            print(f"   🎯 Tier: {metadata['tier']}")
            
            # Identify cells to modify
            new_cells = []
            
            # Keep header (first markdown cell)
            if cells and cells[0].get("cell_type") == "markdown":
                new_cells.append(cells[0])
                cells = cells[1:]
            
            # Find and replace imports cell
            imports_replaced = False
            for i, cell in enumerate(cells):
                if cell.get("cell_type") == "code":
                    source = "".join(cell.get("source", []))
                    if "import" in source and not imports_replaced:
                        # Replace with standard imports
                        new_cells.append(self.get_standard_imports_cell())
                        result["changes"].append("Replaced imports cell with standard template")
                        imports_replaced = True
                        
                        # Skip any subsequent import cells
                        continue
            
            # Add execution tracking if not present
            has_tracking = any("setup_notebook_tracking" in "".join(c.get("source", [])) 
                             for c in cells if c.get("cell_type") == "code")
            
            if not has_tracking:
                new_cells.append(self.get_execution_tracking_cell(
                    metadata["domain"], 
                    metadata["tier"]
                ))
                result["changes"].append("Added execution tracking cell")
            
            # Process remaining cells
            skip_next = False
            for i, cell in enumerate(cells):
                if skip_next:
                    skip_next = False
                    continue
                    
                source = "".join(cell.get("source", []))
                
                # Skip old import cells
                if cell.get("cell_type") == "code" and i < 5:
                    if "import" in source and "from" in source:
                        continue
                    if "API" in source and "key" in source.lower():
                        continue
                
                # Replace data loading patterns
                if "load_api_key" in source or "requests.get" in source:
                    if not any("data_utils.load_data" in "".join(c.get("source", [])) 
                             for c in new_cells):
                        new_cells.append(self.get_data_loading_cell(metadata.get("data_source", "Census ACS")))
                        result["changes"].append("Added standardized data loading cell")
                    skip_next = True
                    continue
                
                # Keep other cells
                new_cells.append(cell)
            
            # Update notebook
            nb_data["cells"] = new_cells
            
            if not dry_run:
                # Backup original
                self.backup_notebook(notebook_path)
                
                # Write updated notebook
                with open(notebook_path, "w", encoding="utf-8") as f:
                    json.dump(nb_data, f, indent=1, ensure_ascii=False)
                
                print(f"   ✅ Updated successfully")
                print(f"   📝 Cells: {original_cell_count} → {len(new_cells)}")
                result["status"] = "SUCCESS"
            else:
                print(f"   🔍 [DRY RUN] Would update: {original_cell_count} → {len(new_cells)} cells")
                result["status"] = "DRY_RUN"
            
            if result["changes"]:
                print(f"   🔄 Changes:")
                for change in result["changes"]:
                    print(f"      - {change}")
            
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
            result["status"] = "ERROR"
            result["errors"].append(str(e))
        
        return result

    def standardize_all(self, specific_notebook: Optional[str] = None, dry_run: bool = False) -> List[Dict]:
        """Standardize all notebooks."""
        if specific_notebook:
            notebooks = [self.notebooks_dir / specific_notebook]
        else:
            notebooks = list(self.notebooks_dir.glob("*.ipynb"))
            notebooks = [nb for nb in sorted(notebooks) if not nb.name.startswith(".")]

        if not notebooks:
            print("❌ No notebooks found!")
            return []

        print(f"\n╔══════════════════════════════════════════════════════════════════════════╗")
        print(f"║         KRAnalytics Notebook Standardization Tool                       ║")
        print(f"╚══════════════════════════════════════════════════════════════════════════╝")
        
        if dry_run:
            print("\n🔍 DRY RUN MODE - No changes will be made")
        
        print(f"\n📚 Processing {len(notebooks)} notebook(s)")

        results = []
        for nb in notebooks:
            result = self.standardize_notebook(nb, dry_run)
            results.append(result)

        return results

    def generate_report(self, results: List[Dict], output_file: str = "STANDARDIZATION_REPORT.md") -> str:
        """Generate standardization report."""
        total = len(results)
        success = sum(1 for r in results if r["status"] == "SUCCESS")
        errors = sum(1 for r in results if r["status"] == "ERROR")
        dry_run = sum(1 for r in results if r["status"] == "DRY_RUN")

        report = f"""# Notebook Standardization Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Total Notebooks:** {total}  

## Results Summary

- ✅ Successfully Updated: {success}
- 🔍 Dry Run: {dry_run}
- ❌ Errors: {errors}

---

## Changes Applied

"""

        for r in results:
            report += f"\n### {r['notebook']}\n\n"
            report += f"**Status:** {r['status']}  \n\n"
            
            if r['changes']:
                report += "**Changes:**\n"
                for change in r['changes']:
                    report += f"- {change}\n"
                report += "\n"
            
            if r['errors']:
                report += "**Errors:**\n"
                for error in r['errors']:
                    report += f"- {error}\n"
                report += "\n"

        report += "---\n\n"
        report += "## Next Steps\n\n"
        report += "1. **Review Changes:** Open each updated notebook and verify changes\n"
        report += "2. **Test Execution:** Run each notebook to ensure it executes correctly\n"
        report += "3. **Validate:** Re-run validation script to confirm all issues resolved\n"
        report += "4. **Update Documentation:** Update examples README with any changes\n\n"

        # Save report
        output_path = self.root_dir / output_file
        output_path.write_text(report)
        print(f"\n📄 Report saved to: {output_file}")

        return report


def main():
    parser = argparse.ArgumentParser(description="Standardize KRAnalytics tutorial notebooks")
    parser.add_argument("--notebook", type=str, help="Standardize specific notebook")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--output", type=str, default="STANDARDIZATION_REPORT.md", help="Output report filename")

    args = parser.parse_args()

    standardizer = NotebookStandardizer()
    results = standardizer.standardize_all(
        specific_notebook=args.notebook,
        dry_run=args.dry_run
    )

    print("\n" + "=" * 80)
    print("📊 STANDARDIZATION SUMMARY")
    print("=" * 80)

    total = len(results)
    success = sum(1 for r in results if r["status"] == "SUCCESS")
    errors = sum(1 for r in results if r["status"] == "ERROR")
    dry_run = sum(1 for r in results if r["status"] == "DRY_RUN")

    print(f"\nTotal Notebooks: {total}")
    print(f"  ✅ Success: {success}")
    if dry_run > 0:
        print(f"  🔍 Dry Run: {dry_run}")
    if errors > 0:
        print(f"  ❌ Errors: {errors}")

    # Generate report
    standardizer.generate_report(results, args.output)

    print("\n✅ Standardization complete!")
    
    if not args.dry_run:
        print(f"💾 Backups saved to: {standardizer.backup_dir}")


if __name__ == "__main__":
    main()
