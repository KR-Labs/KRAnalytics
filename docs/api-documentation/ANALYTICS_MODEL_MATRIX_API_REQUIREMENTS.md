# Analytics Model Matrix - API Requirements & Security Configuration
**Date:** October 8, 2025
**Purpose:** Complete API inventory for 19-domain Analytics Model Matrix
**Status:** Security-enhanced configuration with environment variables

---

## 📊 Current API Configuration

### Existing APIs (Secured in `/QuipuLabs-khipu/configs/apikeys`)
1. ✅ **Census API** - `CENSUS_API_KEY`
2. ✅ **BLS (Bureau of Labor Statistics)** - `BLS_API_KEY`
3. ✅ **FRED (Federal Reserve)** - `FRED_API_KEY`
4. ✅ **BEA (Bureau of Economic Analysis)** - `BEA_API_KEY`

---

## 🔐 Required Additional APIs (by Domain)

### Domain 1-2: Income, Poverty, Inequality
- ✅ Census ACS API (existing)
- ✅ Census SAIPE API (existing Census key works)
- ⚠️ **World Bank API** (no key required - open access)
  - Endpoint: `http://api.worldbank.org/v2/`
  - Usage: Gini coefficient international comparisons
  - Format: JSON/XML

### Domain 3: Employment & Labor Markets
- ✅ BLS API (existing)
- ✅ **Census LEHD/LODES API** (existing Census key works)
  - Endpoint: `https://lehd.ces.census.gov/data/`
  - Usage: Origin-destination employment data
  - Format: CSV

### Domain 4: Education Outcomes
- 🆕 **NCES/IPEDS API** - `NCES_API_KEY`
  - Registration: https://nces.ed.gov/ipeds/datacenter/
  - Endpoint: `https://nces.ed.gov/ipeds/datacenter/API/`
  - Usage: College enrollment, graduation rates
  - Rate Limit: 1000 requests/hour
  - Format: JSON

### Domain 5: Health & Epidemiology
- 🆕 **CDC WONDER API** (no key - web interface only)
  - Endpoint: `https://wonder.cdc.gov/`
  - Usage: Mortality data, health statistics
  - **Note:** Requires web scraping or manual download
  - Alternative: Use County Health Rankings CSV downloads

- ⚠️ **County Health Rankings** (no API - CSV download)
  - URL: `https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation`
  - Usage: Health outcomes, risk factors by county
  - Format: CSV (annual updates)

### Domain 6: Housing & Displacement
- ⚠️ **HUD Fair Market Rent** (no API - Excel/CSV download)
  - URL: `https://www.huduser.gov/portal/datasets/fmr.html`
  - Usage: Fair market rent by metro/county
  - Format: Excel/CSV (annual)

- ⚠️ **Zillow Research Data** (no API - CSV download)
  - URL: `https://www.zillow.com/research/data/`
  - Usage: ZHVI (Home Value Index), rental index
  - Format: CSV (monthly updates)

- ⚠️ **Eviction Lab** (no API - CSV download)
  - URL: `https://evictionlab.org/get-the-data/`
  - Usage: Eviction rates, filings by location
  - Format: CSV

### Domain 7: Public Finance & Taxation
- 🆕 **IRS SOI API** (no public API - data files)
  - URL: `https://www.irs.gov/statistics/soi-tax-stats`
  - Usage: 990 nonprofit data, tax statistics
  - Format: CSV/Excel (annual)

- 🆕 **USASpending.gov API** - `USASPENDING_API_KEY` (optional)
  - Endpoint: `https://api.usaspending.gov/api/v2/`
  - Usage: Federal spending, contracts, grants
  - **No key required** - open API
  - Rate Limit: 1000 requests/hour
  - Format: JSON

### Domain 8: Trade & Value Chains
- ✅ BEA API (existing - covers I-O tables)
- 🆕 **Census International Trade API** - `CENSUS_TRADE_API_KEY`
  - Endpoint: `https://api.census.gov/data/timeseries/intltrade/`
  - **Uses same Census API key**
  - Usage: Import/export data by state/country
  - Format: JSON

### Domain 9: Urban Dynamics & Land Use
- 🆕 **Census TIGER API** (no key - open shapefiles)
  - Endpoint: `https://www2.census.gov/geo/tiger/`
  - Usage: Geospatial boundaries, roads, water
  - Format: Shapefile/GeoJSON

- 🆕 **OpenStreetMap Overpass API** (no key required)
  - Endpoint: `https://overpass-api.de/api/interpreter`
  - Usage: Points of interest, amenities, infrastructure
  - Rate Limit: Reasonable use (no strict limit)
  - Format: JSON/XML

- ⚠️ **EPA EJScreen** (no API - CSV/shapefile download)
  - URL: `https://www.epa.gov/ejscreen/download-ejscreen-data`
  - Usage: Environmental justice indicators
  - Format: CSV/Shapefile (annual)

### Domain 10: Crime & Safety
- 🆕 **FBI Crime Data API** - `FBI_API_KEY`
  - Registration: https://crime-data-explorer.fr.cloud.gov/pages/docApi
  - Endpoint: `https://api.usa.gov/crime/fbi/cde/`
  - Usage: UCR/NIBRS crime statistics
  - Rate Limit: 1000 requests/hour
  - Format: JSON

### Domain 11: Environmental Justice & Resources
- ⚠️ EPA EJScreen (covered above)

- 🆕 **USGS Water Services API** (no key required)
  - Endpoint: `https://waterservices.usgs.gov/rest/`
  - Usage: Water quality, streamflow data
  - Format: JSON/XML

- 🆕 **NOAA Climate Data API** - `NOAA_API_KEY`
  - Registration: https://www.ncdc.noaa.gov/cdo-web/token
  - Endpoint: `https://www.ncdc.noaa.gov/cdo-web/api/v2/`
  - Usage: Climate data, weather stations
  - Rate Limit: 1000 requests/day
  - Format: JSON

### Domain 12: Cultural Capital & Creative Economy
- 🆕 **NEA Open Data** (no API - CSV download)
  - URL: `https://www.arts.gov/open-data`
  - Usage: Arts grants, cultural funding
  - Format: CSV/Excel

- ⚠️ IRS Form 990 (covered in Domain 7)

### Domain 13: Institutional Trust & Legitimacy
- 🆕 **GSS (General Social Survey)** (no API - SPSS/Stata files)
  - URL: `https://gss.norc.org/get-the-data`
  - Usage: Survey data on trust, attitudes
  - Format: SPSS/Stata/ASCII (requires `pyreadstat`)

### Domain 14: Migration & Demographics
- ✅ Census ACS Migration Tables (existing Census key)
- ⚠️ **IRS Migration Data** (no API - CSV download)
  - URL: `https://www.irs.gov/statistics/soi-tax-stats-migration-data`
  - Usage: County-to-county migration flows
  - Format: CSV (annual)

### Domain 15: Social Networks & Connectivity
- 🆕 **FCC Broadband API** (no key - CSV download)
  - URL: `https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477`
  - Usage: Internet access, speed by location
  - Format: CSV

- ✅ Census LEHD LODES (covered in Domain 3)

### Domain 16: Policy Evaluation & Behavioral Dynamics
- ✅ BLS Consumer Expenditure Survey (BLS API)
- ⚠️ **State Administrative Data** (varies by state)
  - URL: State-specific open data portals
  - Usage: Policy adoption, implementation dates
  - Format: Varies (CSV, JSON, APIs)

### Domain 17: Resilience to Shocks
- 🆕 **FEMA Disasters API** - `FEMA_API_KEY`
  - Registration: https://www.fema.gov/about/openfema/api
  - Endpoint: `https://www.fema.gov/api/open/v2/`
  - Usage: Disaster declarations, FEMA aid
  - Rate Limit: 1000 requests/hour
  - Format: JSON

- 🆕 **USDA NASS QuickStats API** - `USDA_NASS_API_KEY`
  - Registration: https://quickstats.nass.usda.gov/api
  - Endpoint: `https://quickstats.nass.usda.gov/api/`
  - Usage: Agricultural statistics, crop data
  - Rate Limit: 1000 requests/hour
  - Format: JSON/CSV

### Domain 18: Futures & Foresight
- ✅ FRED API (existing - macroeconomic indicators)
- ✅ BLS API (existing)
- ✅ BEA API (existing)
- ⚠️ **IPCC/IIASA Climate Projections** (no API - NetCDF files)
  - URL: https://www.ipcc-data.org/
  - Usage: Climate scenario modeling
  - Format: NetCDF (requires `xarray`)

### Domain 19: Information Ecosystems & Narrative Power
- 🆕 **GDELT API** (no key - open access)
  - Endpoint: `https://api.gdeltproject.org/api/v2/`
  - Usage: Global news events, media monitoring
  - Rate Limit: Reasonable use
  - Format: CSV/JSON

- 🆕 **Media Cloud API** - `MEDIACLOUD_API_KEY`
  - Registration: https://mediacloud.org/
  - Endpoint: `https://api.mediacloud.org/api/v2/`
  - Usage: News stories, media analysis
  - Format: JSON

---

## 📋 Complete API Requirements Summary

### APIs Requiring Registration (10)
1. 🆕 **NCES/IPEDS** - Education data
2. 🆕 **FBI Crime Data** - Crime statistics
3. 🆕 **NOAA Climate** - Weather/climate data
4. 🆕 **FEMA Disasters** - Disaster declarations
5. 🆕 **USDA NASS** - Agricultural statistics
6. 🆕 **Media Cloud** - News media analysis
7. ✅ **Census** (existing)
8. ✅ **BLS** (existing)
9. ✅ **FRED** (existing)
10. ✅ **BEA** (existing)

### Open APIs (No Key Required) (6)
1. World Bank API
2. USASpending.gov API
3. OpenStreetMap Overpass API
4. USGS Water Services
5. GDELT API
6. Census TIGER/Shapefiles

### Data Downloads (No API) (11)
1. County Health Rankings (CSV)
2. HUD Fair Market Rent (Excel/CSV)
3. Zillow Research Data (CSV)
4. Eviction Lab (CSV)
5. IRS SOI Statistics (CSV/Excel)
6. EPA EJScreen (CSV/Shapefile)
7. NEA Open Data (CSV/Excel)
8. GSS Survey Data (SPSS/Stata)
9. IRS Migration Data (CSV)
10. FCC Broadband Data (CSV)
11. IPCC Climate Projections (NetCDF)

---

## 🔐 Environment Variable Configuration

### Updated `.env` File Structure

```bash
# ============================================================================
# QUIPU ANALYTICS SUITE - API CONFIGURATION
# ============================================================================
# Date: October 8, 2025
# Purpose: Centralized API key management for 19-domain Analytics Model Matrix
# Security: Never commit this file to version control
# ============================================================================

# EXISTING APIS (4)
# ============================================================================
CENSUS_API_KEY=your_census_api_key_here
BLS_API_KEY=your_bls_api_key_here
FRED_API_KEY=your_fred_api_key_here
BEA_API_KEY=your_bea_api_key_here

# NEW APIS REQUIRING REGISTRATION (6)
# ============================================================================
NCES_API_KEY=your_nces_api_key_here
FBI_CRIME_API_KEY=your_fbi_crime_api_key_here
NOAA_API_KEY=your_noaa_api_key_here
FEMA_API_KEY=your_fema_api_key_here
USDA_NASS_API_KEY=your_usda_nass_api_key_here
MEDIACLOUD_API_KEY=your_mediacloud_api_key_here

# OPTIONAL APIs (Open Access - Keys Optional)
# ============================================================================
USASPENDING_API_KEY=  # Optional - no key required
GDELT_API_KEY=  # Not used - open access
WORLDBANK_API_KEY=  # Not used - open access
OSM_API_KEY=  # Not used - open access
USGS_API_KEY=  # Not used - open access

# DATA DOWNLOAD PATHS (Local Storage)
# ============================================================================
COUNTY_HEALTH_RANKINGS_PATH=../data/external/county_health_rankings/
HUD_FMR_PATH=../data/external/hud_fmr/
ZILLOW_DATA_PATH=../data/external/zillow/
EVICTION_LAB_PATH=../data/external/eviction_lab/
IRS_SOI_PATH=../data/external/irs_soi/
EPA_EJSCREEN_PATH=../data/external/epa_ejscreen/
NEA_GRANTS_PATH=../data/external/nea_grants/
GSS_DATA_PATH=../data/external/gss/
IRS_MIGRATION_PATH=../data/external/irs_migration/
FCC_BROADBAND_PATH=../data/external/fcc_broadband/
IPCC_CLIMATE_PATH=../data/external/ipcc_climate/

# API ENDPOINTS (For Reference)
# ============================================================================
CENSUS_ENDPOINT=https://api.census.gov/data/
BLS_ENDPOINT=https://api.bls.gov/publicAPI/v2/
FRED_ENDPOINT=https://api.stlouisfed.org/fred/
BEA_ENDPOINT=https://apps.bea.gov/api/data/
NCES_ENDPOINT=https://nces.ed.gov/ipeds/datacenter/API/
FBI_ENDPOINT=https://api.usa.gov/crime/fbi/cde/
NOAA_ENDPOINT=https://www.ncdc.noaa.gov/cdo-web/api/v2/
FEMA_ENDPOINT=https://www.fema.gov/api/open/v2/
USDA_NASS_ENDPOINT=https://quickstats.nass.usda.gov/api/
MEDIACLOUD_ENDPOINT=https://api.mediacloud.org/api/v2/
USASPENDING_ENDPOINT=https://api.usaspending.gov/api/v2/
GDELT_ENDPOINT=https://api.gdeltproject.org/api/v2/
OSM_ENDPOINT=https://overpass-api.de/api/interpreter
USGS_ENDPOINT=https://waterservices.usgs.gov/rest/
WORLDBANK_ENDPOINT=http://api.worldbank.org/v2/
```

---

## 📝 Python API Loader Utility

### Create `tools/api_key_manager.py`

```python
"""
API Key Manager for Quipu Analytics Suite
Centralized API key loading and validation
"""
import os
from typing import Dict, Optional
from pathlib import Path
import warnings

class APIKeyManager:
    """Manage API keys from environment variables and config files."""

    # Required APIs for full Analytics Model Matrix functionality
    REQUIRED_APIS = [
        'CENSUS_API_KEY',
        'BLS_API_KEY',
        'FRED_API_KEY',
        'BEA_API_KEY'
    ]

    # Optional APIs (enhanced functionality)
    OPTIONAL_APIS = [
        'NCES_API_KEY',
        'FBI_CRIME_API_KEY',
        'NOAA_API_KEY',
        'FEMA_API_KEY',
        'USDA_NASS_API_KEY',
        'MEDIACLOUD_API_KEY'
    ]

    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize API Key Manager.

        Args:
            env_file: Path to .env file (optional - will check default locations)
        """
        self.env_file = env_file
        self.keys: Dict[str, str] = {}
        self._load_keys()

    def _load_keys(self):
        """Load API keys from environment variables and config files."""
        # Priority 1: Environment variables
        for key in self.REQUIRED_APIS + self.OPTIONAL_APIS:
            if key in os.environ:
                self.keys[key] = os.environ[key]

        # Priority 2: .env file (if specified)
        if self.env_file and Path(self.env_file).exists():
            self._load_from_file(self.env_file)

        # Priority 3: Default config file
        default_config = Path(__file__).parent.parent.parent / 'QuipuLabs-khipu' / 'configs' / 'apikeys'
        if default_config.exists():
            self._load_from_file(str(default_config))

    def _load_from_file(self, filepath: str):
        """Load API keys from configuration file."""
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key not in self.keys:  # Don't override env vars
                        self.keys[key] = value

    def get_key(self, api_name: str, required: bool = True) -> Optional[str]:
        """
        Get API key for specified service.

        Args:
            api_name: Name of API key (e.g., 'CENSUS_API_KEY')
            required: Whether to raise error if key not found

        Returns:
            API key string or None

        Raises:
            ValueError: If required key not found
        """
        key = self.keys.get(api_name)

        if not key and required:
            raise ValueError(
                f"API key '{api_name}' not found. "
                f"Please set it in environment variables or config file."
            )

        if not key and not required:
            warnings.warn(f"Optional API key '{api_name}' not found. Some functionality may be limited.")

        return key

    def validate_required_keys(self) -> Dict[str, bool]:
        """
        Validate all required API keys are present.

        Returns:
            Dictionary of {api_name: is_present}
        """
        validation = {}
        for key in self.REQUIRED_APIS:
            validation[key] = key in self.keys and bool(self.keys[key])
        return validation

    def get_missing_keys(self) -> list:
        """Get list of missing required API keys."""
        return [key for key in self.REQUIRED_APIS if key not in self.keys or not self.keys[key]]

    def get_api_status(self) -> Dict[str, str]:
        """
        Get status of all API keys.

        Returns:
            Dictionary of {api_name: status}
        """
        status = {}

        for key in self.REQUIRED_APIS:
            if key in self.keys and self.keys[key]:
                status[key] = '✅ Configured'
            else:
                status[key] = '❌ Missing (REQUIRED)'

        for key in self.OPTIONAL_APIS:
            if key in self.keys and self.keys[key]:
                status[key] = '✅ Configured'
            else:
                status[key] = '⚠️  Not configured (optional)'

        return status

# Convenience function for notebook use
def load_api_key(api_name: str, required: bool = True) -> Optional[str]:
    """
    Quick API key loader for notebooks.

    Usage:
        census_key = load_api_key('CENSUS_API_KEY')
        noaa_key = load_api_key('NOAA_API_KEY', required=False)
    """
    manager = APIKeyManager()
    return manager.get_key(api_name, required=required)
```

---

## 🎯 Implementation Checklist

### Phase 1: Core APIs (Existing)
- [x] Census API
- [x] BLS API
- [x] FRED API
- [x] BEA API

### Phase 2: High-Priority New APIs (Weeks 1-2)
- [ ] NCES/IPEDS API (Education)
- [ ] FBI Crime Data API
- [ ] FEMA Disasters API
- [ ] USDA NASS API (Agriculture)

### Phase 3: Medium-Priority APIs (Weeks 3-4)
- [ ] NOAA Climate API
- [ ] Media Cloud API

### Phase 4: Data Downloads Automation (Weeks 5-8)
- [ ] Create download scripts for HUD, Zillow, Eviction Lab
- [ ] Automate IRS SOI data retrieval
- [ ] EPA EJScreen data processing pipeline
- [ ] GSS data import utilities

---

## 📚 Registration Links

1. **NCES/IPEDS**: https://nces.ed.gov/ipeds/datacenter/
2. **FBI Crime Data**: https://crime-data-explorer.fr.cloud.gov/pages/docApi
3. **NOAA Climate**: https://www.ncdc.noaa.gov/cdo-web/token
4. **FEMA**: https://www.fema.gov/about/openfema/api
5. **USDA NASS**: https://quickstats.nass.usda.gov/api
6. **Media Cloud**: https://mediacloud.org/

---

**Last Updated:** October 8, 2025
**Status:** Ready for implementation
**Priority:** Complete Phase 2 APIs for full 19-domain coverage
