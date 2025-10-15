#!/bin/bash
# cleanup_for_github.sh
# Automated cleanup script to prepare KRAnalytics for public GitHub upload

set -e  # Exit on error

echo "🧹 KRAnalytics Repository Cleanup Script"
echo "=========================================="
echo ""

# Navigate to repository root
cd "$(dirname "$0")"

echo "📍 Current directory: $(pwd)"
echo ""

# Confirm before proceeding
read -p "⚠️  This will remove internal files. Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "❌ Cleanup cancelled."
    exit 1
fi

echo ""
echo "🗑️  Removing internal status reports..."

# Remove status report markdown files
rm -f ACHIEVING_100_PERCENT_PASS.md
rm -f API_ERRORS_RESOLVED.md
rm -f CELL_BY_CELL_AUDIT_REPORT.md
rm -f FINAL_VALIDATION_REPORT.md
rm -f KERNEL_SETUP_COMPLETE.md
rm -f NAMING_CONVENTIONS_UPDATED.md
rm -f NOTEBOOK_07_UPDATE_COMPLETE.md
rm -f NOTEBOOK_AUDIT_COMPLETE.md
rm -f NOTEBOOK_QUICK_REFERENCE.md
rm -f NOTEBOOK_STANDARDIZATION_PLAN.md
rm -f NOTEBOOK_UPDATE_GUIDE.md
rm -f NOTEBOOK_VALIDATION_REPORT.md
rm -f PARTIAL_COMPLIANCE_FIXES_COMPLETE.md
rm -f PUBLIC_REPO_MIGRATION_COMPLETE.md
rm -f READY_FOR_GITHUB.md
rm -f REFACTORING_COMPLETE.md
rm -f SAMPLE_DATA_COMPLETE.md
rm -f SESSION_SUMMARY.md
rm -f STANDARDIZATION_COMPLETE.md
rm -f STANDARDIZATION_REPORT.md
rm -f UPLOAD_READINESS_REPORT.md

echo "✅ Status reports removed"

echo ""
echo "🗑️  Removing backups directory..."
rm -rf backups/
echo "✅ Backups directory removed"

echo ""
echo "🗑️  Removing .DS_Store files..."
find . -name ".DS_Store" -type f -delete
echo "✅ .DS_Store files removed"

echo ""
echo "🗑️  Removing empty config directory..."
if [ -d "config" ] && [ -z "$(ls -A config)" ]; then
    rm -rf config/
    echo "✅ Empty config directory removed"
else
    echo "ℹ️  Config directory kept (not empty or doesn't exist)"
fi

echo ""
echo "🔍 Checking for sensitive files..."

# Check for potential API keys or credentials
if grep -r "api[_-]key\|API[_-]KEY\|secret\|password" --include="*.py" --include="*.ipynb" --include="*.json" . 2>/dev/null | grep -v ".git" | grep -v ".venv" | grep -v "# " | head -5; then
    echo "⚠️  WARNING: Potential sensitive data found! Review before uploading."
else
    echo "✅ No obvious sensitive data patterns found"
fi

echo ""
echo "📊 Repository structure after cleanup:"
echo "--------------------------------------"
tree -L 2 -I '__pycache__|*.pyc|.git|.venv|.ipynb_checkpoints' 2>/dev/null || find . -maxdepth 2 -not -path '*/\.*' -type d

echo ""
echo "📋 Files kept in root:"
ls -1 | grep -E '\.(md|txt|toml|py|yaml)$|^Makefile$|^LICENSE$'

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Review CLEANUP_FOR_GITHUB.md for full checklist"
echo "   2. Verify .gitignore is correct"
echo "   3. Run: make test"
echo "   4. Run: pip install -e ."
echo "   5. Review README.md for public audience"
echo "   6. Commit changes: git add -A && git commit -m 'Prepare for public release'"
echo "   7. Push to GitHub"
echo ""
echo "🚀 Repository is ready for public upload!"
