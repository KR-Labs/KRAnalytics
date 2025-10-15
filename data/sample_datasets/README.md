# Sample Datasets for KRAnalytics Tutorials

This directory contains pre-downloaded sample datasets that allow you to run the tutorial notebooks **without requiring API keys**.

##  Directory Structure

```
data/
 sample_datasets/
     census_income_2020.csv          # Income data from Census ACS
     census_inequality_2020.csv      # Inequality metrics
     bls_employment_counties.csv     # County-level employment (QCEW)
     bls_employment_national.csv     # National employment (LNS series)
     epa_environmental_burden.csv    # EPA EJScreen data
     fbi_crime_stats.csv             # FBI UCR crime statistics
     README.md                       # This file
```

##  Purpose

The sample datasets serve three purposes:

1. **No API Keys Required**: Run tutorials immediately without obtaining API keys
2. **Reproducibility**: Consistent data for learning and testing
3. **Offline Access**: Work without internet connection

##  Available Datasets

### 1. Census Income Data (census_income_2020.csv)
**Source:** U.S. Census Bureau American Community Survey (ACS)  
**Coverage:** 2020 state-level data  
**Variables:**
- Median household income
- Poverty rates
- Income distribution by percentile
- Geographic identifiers (state FIPS, names)

**Used in:**
- `01_Income_Analysis_Tutorial.ipynb`
- `03_Income_Distribution_Tutorial.ipynb`

---

### 2. Inequality Metrics (census_inequality_2020.csv)
**Source:** Derived from Census ACS detailed tables  
**Coverage:** 2020 state-level data  
**Variables:**
- Gini coefficient
- Income quintiles
- Top 10% vs bottom 40% ratios
- Lorenz curve data points

**Used in:**
- `02_Inequality_Analysis_Tutorial.ipynb`

---

### 3. BLS Employment - Counties (bls_employment_counties.csv)
**Source:** Bureau of Labor Statistics Quarterly Census of Employment and Wages (QCEW)  
**Coverage:** 2018-2023 quarterly data for selected counties  
**Variables:**
- Employment levels by county
- Average wages
- Industry classifications (NAICS)
- Quarterly time series

**Used in:**
- `04_Employment_Forecasting_Counties_Tutorial.ipynb`

---

### 4. BLS Employment - National (bls_employment_national.csv)
**Source:** Bureau of Labor Statistics Labor Force Statistics (LNS series)  
**Coverage:** 2018-2023 monthly data  
**Variables:**
- Unemployment rate
- Labor force participation rate
- Employment-population ratio
- Monthly time series

**Used in:**
- `05_Employment_Forecasting_BLS_Tutorial.ipynb`

---

### 5. Environmental Burden (epa_environmental_burden.csv)
**Source:** EPA Environmental Justice Screening Tool (EJScreen)  
**Coverage:** Census tract-level data  
**Variables:**
- Air quality indices
- Proximity to hazardous waste sites
- Demographic characteristics
- Environmental health indicators

**Used in:**
- `06_Environmental_Burden_Tutorial.ipynb`

---

### 6. Crime Statistics (fbi_crime_stats.csv)
**Source:** FBI Uniform Crime Reporting (UCR) Program  
**Coverage:** 2018-2023 state-level data  
**Variables:**
- Violent crime rates
- Property crime rates
- Crime types (assault, burglary, etc.)
- Population and geographic data

**Used in:**
- `07_Crime_Prediction_Tutorial.ipynb`

---

##  Using Sample Data in Notebooks

The notebooks are designed to automatically use sample data if API keys are not available:

```python
from kranalytics.data_utils import load_data_with_fallback, load_sample_data

# Option 1: Automatic fallback (tries API first, then sample data)
df = load_data_with_fallback(
    api_loader_func=load_census_data,
    dataset_name='census_income_2020',
    api_key_name='CENSUS_API_KEY'
)

# Option 2: Load sample data directly (skip API entirely)
df = load_sample_data('census_income_2020')
```

If API keys are set in environment variables, notebooks will use live data. Otherwise, they automatically fall back to these sample datasets.

##  Downloading Sample Data

### Option 1: Download Pre-packaged Data (Recommended)

Download the complete sample dataset archive:

```bash
# From the repository root
wget https://github.com/KR-Labs/KRAnalytics/releases/download/v1.0.0/sample_data.zip
unzip sample_data.zip -d data/
```

### Option 2: Generate from APIs (Requires API Keys)

If you have API keys, you can generate your own sample data:

```bash
# Set API keys
export CENSUS_API_KEY="your_census_key"
export BLS_API_KEY="your_bls_key"
export EPA_API_KEY="your_epa_key"
export FBI_CRIME_API_KEY="your_fbi_key"

# Run data generation script
python scripts/generate_sample_data.py
```

### Option 3: Use Existing Tutorial Data

Run the notebooks once with API keys, and they'll cache the data:

```python
# In any notebook
from kranalytics.data_utils import save_sample_data

# After loading data from API
save_sample_data(df, 'dataset_name', format='csv')
```

##  Optional: Using Live API Data

To use live API data instead of samples:

1. **Obtain API Keys** from the respective data providers:
   - Census: https://api.census.gov/data/key_signup.html
   - BLS: https://data.bls.gov/registrationEngine/
   - EPA: https://www.epa.gov/developers/api-key-registration
   - FBI: https://crime-data-explorer.app.cloud.gov/pages/docApi

2. **Set Environment Variables**:
   ```bash
   export CENSUS_API_KEY="your_key_here"
   export BLS_API_KEY="your_key_here"
   # ... etc
   ```

3. **Run Notebooks** - They will automatically use API data when keys are present

##  Data License & Attribution

### Census Data
**Source:** U.S. Census Bureau  
**License:** Public Domain  
**Attribution:** U.S. Census Bureau, American Community Survey

### BLS Data
**Source:** U.S. Bureau of Labor Statistics  
**License:** Public Domain  
**Attribution:** U.S. Bureau of Labor Statistics

### EPA Data
**Source:** U.S. Environmental Protection Agency  
**License:** Public Domain  
**Attribution:** U.S. EPA, EJSCREEN

### FBI Data
**Source:** Federal Bureau of Investigation  
**License:** Public Domain  
**Attribution:** FBI Uniform Crime Reporting Program

All data is from U.S. government sources and is in the public domain.

##  Updating Sample Data

Sample data is updated periodically with new releases. To get the latest:

```bash
# Check current data version
cat data/sample_datasets/VERSION.txt

# Download latest data
wget https://github.com/KR-Labs/KRAnalytics/releases/latest/download/sample_data.zip
unzip -o sample_data.zip -d data/
```

##  Data Quality Notes

### Limitations of Sample Data:
- **Static Snapshot**: Sample data represents a specific time period and won't reflect current conditions
- **Geographic Coverage**: May be limited to selected states/counties for file size
- **Simplified**: Some variables may be aggregated or simplified
- **Educational Purpose**: Suitable for learning but use live API data for production analysis

### For Production Use:
 Always use live API data for real analyses  
 Verify data currency and coverage  
 Check for data updates and revisions  
 Review methodology documentation

##  Troubleshooting

### "Sample data not found" Error

**Problem:** Notebook can't find sample dataset

**Solutions:**
1. Check if file exists: `ls data/sample_datasets/`
2. Download sample data (see "Downloading Sample Data" above)
3. Verify file naming matches what notebook expects

### "Empty DataFrame" Warning

**Problem:** Sample data loaded but appears empty

**Solutions:**
1. Check file size: `du -h data/sample_datasets/*.csv`
2. Re-download if files are corrupted
3. Try generating fresh data with `scripts/generate_sample_data.py`

### API Fallback Not Working

**Problem:** Notebook tries API but doesn't fall back to sample data

**Solutions:**
1. Check if `kranalytics.data_utils` is imported correctly
2. Verify sample data exists in correct location
3. Update notebook to latest version

##  Support

For issues with sample data:
- **GitHub Issues**: https://github.com/KR-Labs/KRAnalytics/issues
- **Discussions**: https://github.com/KR-Labs/KRAnalytics/discussions
- **Email**: info@krlabs.dev

---

**Last Updated:** October 14, 2025  
**Data Version:** v1.0  
**Compatible with:** KRAnalytics v1.0+
