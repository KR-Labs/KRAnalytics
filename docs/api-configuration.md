# API Configuration Guide

This guide provides detailed instructions for setting up and configuring API connections to government and institutional data sources supported by KRAnalytics.

##  Supported Data Sources

KRAnalytics integrates with the following authoritative data providers:

### Core Government APIs
- **U.S. Census Bureau** - Demographic, income, poverty, and housing data
- **Bureau of Labor Statistics (BLS)** - Employment, wages, and unemployment statistics
- **Federal Reserve Economic Data (FRED)** - Macroeconomic indicators and interest rates
- **Bureau of Economic Analysis (BEA)** - GDP, trade, and national accounts

### Specialized APIs
- **National Center for Education Statistics (NCES)** - Educational outcomes
- **FBI Crime Data API** - Crime statistics
- **NOAA Climate API** - Weather and climate data
- **HUD Fair Market Rent** - Housing affordability metrics

##  Quick Setup

### Step 1: Get API Keys

Most APIs require free registration:

1. **Census Bureau**: Register at [api.census.gov](https://api.census.gov/data/key_signup.html)
2. **BLS**: Register at [bls.gov/developers](https://www.bls.gov/developers/api_signature_v2.html)
3. **FRED**: Register at [fred.stlouisfed.org/docs/api](https://fred.stlouisfed.org/docs/api/api_key.html)
4. **BEA**: Register at [bea.gov/API](https://www.bea.gov/api/signup/)

### Step 2: Set Environment Variables

```bash
# Option 1: Export in your shell
export CENSUS_API_KEY="your_census_key_here"
export BLS_API_KEY="your_bls_key_here"
export FRED_API_KEY="your_fred_key_here"
export BEA_API_KEY="your_bea_key_here"

# Option 2: Add to your .bashrc or .zshrc
echo 'export CENSUS_API_KEY="your_census_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### Step 3: Verify Configuration

```python
from kranalytics.data_utils import get_api_key

# Test API key loading
census_key = get_api_key('CENSUS_API_KEY')
print(f"Census API key configured: {'' if census_key else ''}")
```

##  Data Source Details

### U.S. Census Bureau API

**Base URL:** `https://api.census.gov/data`

**Key Datasets:**
- American Community Survey (ACS): `acs/acs5`
- Small Area Income & Poverty Estimates (SAIPE): `timeseries/poverty/saipe`
- Population Estimates: `pep/population`

**Example Usage:**
```python
from kranalytics.data_utils import load_data_with_fallback

# Load median household income data
def load_census_income(api_key, year=2022):
    # Census API implementation
    pass

df = load_data_with_fallback(
    api_loader_func=load_census_income,
    dataset_name='census_income_2022',
    api_key_name='CENSUS_API_KEY',
    api_loader_kwargs={'year': 2022}
)
```

### Bureau of Labor Statistics API

**Base URL:** `https://api.bls.gov/publicAPI/v2`

**Key Series:**
- Labor Force Statistics: `LNS` series
- Quarterly Census of Employment and Wages: `QCEW`
- Consumer Price Index: `CU` series

**Example Usage:**
```python
# Load unemployment rate data
series_ids = ['LNS14000000']  # Unemployment rate
df = load_bls_data(api_key=bls_key, series_ids=series_ids)
```

### Federal Reserve Economic Data (FRED)

**Base URL:** `https://api.stlouisfed.org/fred`

**Key Indicators:**
- GDP: `GDP`
- Interest Rates: `FEDFUNDS`
- Inflation: `CPIAUCSL`

### Bureau of Economic Analysis (BEA)

**Base URL:** `https://apps.bea.gov/api/data`

**Key Datasets:**
- National Income and Product Accounts (NIPA)
- Regional Economic Accounts
- International Trade

##  Advanced Configuration

### Using Configuration Files

Create a `.env` file in your project root:

```bash
# .env file
CENSUS_API_KEY=your_census_key_here
BLS_API_KEY=your_bls_key_here
FRED_API_KEY=your_fred_key_here
BEA_API_KEY=your_bea_key_here
```

Load with python-dotenv:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Rate Limiting and Best Practices

1. **Respect Rate Limits:**
   - Census: 500 queries per IP per day
   - BLS: 25 queries per day (unregistered), 500 per day (registered)
   - FRED: No specified limit, but be reasonable

2. **Cache Results:**
   - Use sample data for development
   - Cache API responses for repeated analysis

3. **Error Handling:**
   - Always implement fallback to sample data
   - Handle network timeouts gracefully

### Sample Data Fallback

KRAnalytics includes sample datasets that work without API keys:

```python
from kranalytics.data_utils import load_sample_data

# Load sample data (no API key required)
df = load_sample_data('census_income_2022')
```

##  Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** or secure credential management
3. **Rotate keys periodically** as recommended by providers
4. **Monitor usage** to detect unauthorized access

##  Troubleshooting

### Common Issues

**Issue**: `ValueError: API key 'CENSUS_API_KEY' not found`
**Solution**: Ensure environment variable is set: `echo $CENSUS_API_KEY`

**Issue**: `requests.exceptions.HTTPError: 403 Client Error`
**Solution**: Check if API key is valid and hasn't expired

**Issue**: `Rate limit exceeded`
**Solution**: Wait before retrying or use sample data for development

### Getting Help

- Check [GitHub Issues](https://github.com/KR-Labs/KRAnalytics/issues) for known problems
- Join [GitHub Discussions](https://github.com/KR-Labs/KRAnalytics/discussions) for questions
- Contact: info@krlabs.dev

---

**Last Updated:** October 14, 2025  
**Version:** v1.0.0