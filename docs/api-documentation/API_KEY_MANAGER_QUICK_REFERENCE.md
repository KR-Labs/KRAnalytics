# API Key Manager - Quick Reference Guide

**Version:** 1.0.0
**Date:** October 8, 2025
**Status:** ✅ PRODUCTION READY

---

## For Notebook Developers

### Basic Usage (Use This Pattern)

```python
# ═══════════════════════════════════════════════════════════════════════════
# API AUTHENTICATION
# ═══════════════════════════════════════════════════════════════════════════

import sys
from pathlib import Path

# Add project root to path
project_root = Path.cwd().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# Load API keys using centralized manager
from tools.api_key_manager import load_api_key

# Required APIs (will raise error if not found)
census_key = load_api_key('CENSUS_API_KEY')
bls_key = load_api_key('BLS_API_KEY')
fred_key = load_api_key('FRED_API_KEY')
bea_key = load_api_key('BEA_API_KEY')

# Optional APIs (will warn if not found, returns None)
nces_key = load_api_key('NCES_API_KEY', required=False)
noaa_key = load_api_key('NOAA_API_KEY', required=False)

print("✅ API authentication successful")
```

### Check API Status (For Debugging)

```python
from tools.api_key_manager import print_api_status

print_api_status()
```

**Output:**
```
================================================================================
 QUIPU ANALYTICS SUITE - API STATUS REPORT
================================================================================

📌 CORE APIS (Required):
   CENSUS_API_KEY            ✅ Configured (Required)
   BLS_API_KEY               ✅ Configured (Required)
   FRED_API_KEY              ✅ Configured (Required)
   BEA_API_KEY               ✅ Configured (Required)

✅ All required APIs configured!
================================================================================
```

### Validate Configuration

```python
from tools.api_key_manager import validate_api_keys, get_missing_apis

if not validate_api_keys():
    missing = get_missing_apis()
    print(f"⚠️  Missing required APIs: {', '.join(missing)}")
    print("Configure them in /QuipuLabs-khipu/configs/apikeys")
else:
    print("✅ All required APIs configured")
```

---

## For API Configuration

### Config File Location

**Primary:** `/Users/bcdelo/Documents/GitHub/QuipuLabs-khipu/configs/apikeys`

### Supported Formats

**Format 1 (Legacy - Currently Used):**
```bash
CENSUS API: 199343249e46333a2676a4976d696e45a9d2e15d
BLS API KEY: 869945c941d14c65bb464751f51cee55
FRED API KEY: 8ec3c8309e60d874eae960d407f15460
BEA API KEY: 9D35B76D-D94E-47A2-9509-6D81CFDD4259
```

**Format 2 (Standard):**
```bash
CENSUS_API_KEY=199343249e46333a2676a4976d696e45a9d2e15d
BLS_API_KEY=869945c941d14c65bb464751f51cee55
FRED_API_KEY=8ec3c8309e60d874eae960d407f15460
BEA_API_KEY=9D35B76D-D94E-47A2-9509-6D81CFDD4259
```

**Both formats work!** The API Key Manager automatically detects and parses either format.

### Environment Variables (Alternative)

```bash
export CENSUS_API_KEY="199343249e46333a2676a4976d696e45a9d2e15d"
export BLS_API_KEY="869945c941d14c65bb464751f51cee55"
export FRED_API_KEY="8ec3c8309e60d874eae960d407f15460"
export BEA_API_KEY="9D35B76D-D94E-47A2-9509-6D81CFDD4259"
```

**Priority:** Environment variables > Config file

---

## API Registry

### Core APIs (Required - ✅ All Configured)

| API | Key Name | Status | Endpoint |
|-----|----------|--------|----------|
| Census | `CENSUS_API_KEY` | ✅ Working | https://api.census.gov/data/ |
| BLS | `BLS_API_KEY` | ✅ Working | https://api.bls.gov/publicAPI/v2/ |
| FRED | `FRED_API_KEY` | ✅ Working | https://api.stlouisfed.org/fred/ |
| BEA | `BEA_API_KEY` | ✅ Working | https://apps.bea.gov/api/data/ |

### Phase 1 APIs (High Priority - ⚠️ Register These)

| API | Key Name | Registration URL | Approval | Cost |
|-----|----------|------------------|----------|------|
| NCES | `NCES_API_KEY` | https://nces.ed.gov/ipeds/datacenter/ | 1-3 days | Free |
| FBI Crime | `FBI_CRIME_API_KEY` | https://crime-data-explorer.fr.cloud.gov/pages/docApi | Instant | Free |
| FEMA | `FEMA_API_KEY` | https://www.fema.gov/about/openfema/api | Instant | Free |
| USDA NASS | `USDA_NASS_API_KEY` | https://quickstats.nass.usda.gov/api | Instant | Free |
| NOAA | `NOAA_API_KEY` | https://www.ncdc.noaa.gov/cdo-web/token | Instant | Free |
| Media Cloud | `MEDIACLOUD_API_KEY` | https://mediacloud.org/ | 1-2 weeks | Free |

**Action:** Register for these 6 APIs in Week 2 for 85% domain coverage

### Open Access APIs (No Key Required)

| API | Purpose | Endpoint |
|-----|---------|----------|
| World Bank | International data | http://api.worldbank.org/v2/ |
| USASpending | Federal spending | https://api.usaspending.gov/api/v2/ |
| OpenStreetMap | Geospatial data | https://overpass-api.de/api/interpreter |
| USGS Water | Water quality | https://waterservices.usgs.gov/rest/ |
| GDELT | News events | https://api.gdeltproject.org/api/v2/ |
| Census TIGER | Boundaries | https://www2.census.gov/geo/tiger/ |

---

## Domain-to-API Mapping

Quick reference for which APIs are needed for each Analytics Model Matrix domain:

| Domain | Required APIs | Status |
|--------|---------------|--------|
| Income & Poverty | `CENSUS_API_KEY` | ✅ Ready |
| Inequality | `CENSUS_API_KEY` | ✅ Ready |
| Employment & Labor | `BLS_API_KEY`, `CENSUS_API_KEY` | ✅ Ready |
| Education | `NCES_API_KEY`, `CENSUS_API_KEY` | ⚠️ Phase 1 |
| Health | `CENSUS_API_KEY` | ✅ Ready |
| Housing | `CENSUS_API_KEY` | ✅ Ready |
| Trade | `BEA_API_KEY`, `CENSUS_API_KEY` | ✅ Ready |
| Crime | `FBI_CRIME_API_KEY` | ⚠️ Phase 1 |
| Environmental | `NOAA_API_KEY` | ⚠️ Phase 1 |
| Migration | `CENSUS_API_KEY` | ✅ Ready |
| Social Networks | `CENSUS_API_KEY` | ✅ Ready |
| Policy Evaluation | `BLS_API_KEY` | ✅ Ready |
| Resilience | `FEMA_API_KEY`, `USDA_NASS_API_KEY` | ⚠️ Phase 1 |
| Futures | `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY` | ✅ Ready |
| Information | `MEDIACLOUD_API_KEY` | ⚠️ Phase 1 |

**Current Coverage:** 6/19 domains (31.6%) with ✅ Ready status
**Phase 1 Target:** 16/19 domains (85%) after registering 6 APIs

---

## Testing

### Test API Key Manager

```bash
cd /Users/bcdelo/Documents/GitHub/QRL
source venv313/bin/activate
python tools/api_key_manager.py
```

**Expected Output:**
```
🔐 Testing API Key Manager

✅ All required APIs configured!
Total APIs configured: 5
Configuration complete: True

🧪 Testing key loading:
✅ Census API key loaded: 199343249e...

🎯 Testing domain API mapping:
Employment & Labor Markets:
  ✅ BLS_API_KEY
  ✅ CENSUS_API_KEY
```

### Test in Notebook

```python
# Test loading
from tools.api_key_manager import load_api_key, validate_api_keys

if validate_api_keys():
    census_key = load_api_key('CENSUS_API_KEY')
    print(f"✅ Census API: {census_key[:10]}...")
else:
    print("❌ API configuration incomplete")
```

---

## Troubleshooting

### Error: "API key 'CENSUS_API_KEY' not found"

**Solution 1:** Check config file exists
```bash
ls -la /Users/bcdelo/Documents/GitHub/QuipuLabs-khipu/configs/apikeys
```

**Solution 2:** Verify file format
```bash
cat /Users/bcdelo/Documents/GitHub/QuipuLabs-khipu/configs/apikeys
```

**Solution 3:** Use environment variable
```bash
export CENSUS_API_KEY="your_key_here"
```

### Error: "ModuleNotFoundError: No module named 'tools.api_key_manager'"

**Solution:** Add project root to path in notebook
```python
import sys
from pathlib import Path
project_root = Path.cwd().parent.parent
sys.path.append(str(project_root))
```

### Warning: "Optional API key 'NOAA_API_KEY' not found"

**This is normal!** Optional APIs warn but don't fail. Register the API when needed:
1. Visit https://www.ncdc.noaa.gov/cdo-web/token
2. Request API token (instant approval)
3. Add to config file: `NOAA API KEY: your_token_here`

---

## File Locations

### Source Code
- **API Key Manager:** `/Users/bcdelo/Documents/GitHub/QRL/tools/api_key_manager.py`

### Configuration
- **Primary Config:** `/Users/bcdelo/Documents/GitHub/QuipuLabs-khipu/configs/apikeys`
- **Alternative:** `../configs/apikeys` (relative to notebook)

### Documentation
- **Implementation Guide:** `/Users/bcdelo/Documents/GitHub/QRL/API_KEY_MANAGER_IMPLEMENTATION.md`
- **API Requirements:** `/Users/bcdelo/Documents/GitHub/QRL/ANALYTICS_MODEL_MATRIX_API_REQUIREMENTS.md`
- **Quick Reference:** `/Users/bcdelo/Documents/GitHub/QRL/API_KEY_MANAGER_QUICK_REFERENCE.md` (this file)

### Example Notebooks
- **Updated Example:** `/Users/bcdelo/Documents/GitHub/QRL/notebooks/tier3_timeseries/Tier3_Economic_Forecasting_FRED.ipynb`

---

## Next Steps

### Week 1 (October 8-15, 2025)

**Priority 1: Update Production Notebooks**
- [ ] `Tier2_Income_Prediction_ACS.ipynb` (Census API)
- [ ] `Tier2_Employment_Forecasting_BLS.ipynb` (BLS API)
- [ ] `Tier1_Income_Distribution_ACS.ipynb` (Census API)

**Priority 2: Register Phase 1 APIs**
- [ ] NCES (Education - 1-3 days)
- [ ] FBI Crime (Instant)
- [ ] FEMA (Instant)
- [ ] USDA NASS (Instant)
- [ ] NOAA (Instant)
- [ ] Media Cloud (1-2 weeks)

**Priority 3: Update Skeleton Notebooks**
- [ ] Update all 8 skeleton notebooks with API Key Manager
- [ ] Test execution of each updated notebook

### Week 2-4 (October 15-November 5, 2025)

**Complete Phase 1 Notebooks:**
- [ ] Finish Economic Forecasting (FRED API)
- [ ] Finish Inequality Analysis (Census API)
- [ ] Finish Education Performance (NCES API)
- [ ] Finish Crime Prediction (FBI API)
- [ ] Finish Disaster Impact (FEMA API)
- [ ] Complete remaining 3 notebooks

**Target:** 8/8 Phase 1 notebooks production-ready (100%)

---

## Quick Commands

### View API Status
```bash
cd /Users/bcdelo/Documents/GitHub/QRL
source venv313/bin/activate
python -c "from tools.api_key_manager import print_api_status; print_api_status()"
```

### Check Missing APIs
```bash
python -c "from tools.api_key_manager import get_missing_apis; print('\n'.join(get_missing_apis()) or 'All required APIs configured')"
```

### Validate Configuration
```bash
python -c "from tools.api_key_manager import validate_api_keys; print('✅ Complete' if validate_api_keys() else '❌ Incomplete')"
```

### Test API Loading
```bash
python -c "from tools.api_key_manager import load_api_key; k = load_api_key('CENSUS_API_KEY'); print(f'✅ Census API: {k[:10]}...')"
```

---

## Support

### Documentation
- **Full Documentation:** `API_KEY_MANAGER_IMPLEMENTATION.md`
- **API Requirements:** `ANALYTICS_MODEL_MATRIX_API_REQUIREMENTS.md`
- **Custom Instructions:** `.github/copilot-instructions.md` (Section: API Security & Configuration)

### Example Usage
- **Notebook Example:** `notebooks/tier3_timeseries/Tier3_Economic_Forecasting_FRED.ipynb`
- **Test Script:** Run `python tools/api_key_manager.py`

### Issues
- **Config not found:** Check `/QuipuLabs-khipu/configs/apikeys` exists
- **Import error:** Add project root to sys.path in notebook
- **Optional API warning:** Normal behavior, register API when needed

---

**Status:** ✅ READY FOR USE
**Last Updated:** October 8, 2025
**Version:** 1.0.0
