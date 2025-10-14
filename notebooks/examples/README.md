# KRAnalytics Tutorial Notebooks

This directory contains **7 comprehensive tutorial notebooks** demonstrating the capabilities of the KRAnalytics framework across multiple socioeconomic domains.

## 📚 Tutorial Catalog

### 1️⃣ Income Analysis Tutorial
**File:** `01_Income_Analysis_Tutorial.ipynb`
**Domain:** D01 - Income & Poverty Analysis
**Tier:** 1-3 (Descriptive, Predictive, Time Series)
**Data Sources:** US Census Bureau ACS, FRED API
**Key Concepts:**
- API key management with secure credential loading
- Data retrieval from Census Bureau
- Descriptive statistics and income distributions
- Predictive modeling (Linear Regression, Random Forest)
- Interactive Plotly visualizations (choropleth maps, scatter plots)
- Geographic analysis (county and state level)

**Business Applications:**
- Economic policy planning
- Regional economic development analysis
- Poverty intervention targeting

---

### 2️⃣ Inequality Analysis Tutorial
**File:** `02_Inequality_Analysis_Tutorial.ipynb`
**Domain:** D02 - Inequality & Distribution
**Tier:** 1 (Descriptive)
**Data Sources:** US Census Bureau ACS
**Key Concepts:**
- Inequality metrics (Gini coefficient, Theil index)
- Income distribution analysis
- Lorenz curves and cumulative distribution functions
- Comparative inequality analysis across geographies
- Statistical testing for inequality differences

**Business Applications:**
- Economic inequality assessment
- Social equity policy evaluation
- Resource allocation optimization

---

### 3️⃣ Income Distribution Tutorial
**File:** `03_Income_Distribution_Tutorial.ipynb`
**Domain:** D01 - Income & Poverty Analysis
**Tier:** 1 (Descriptive)
**Data Sources:** US Census Bureau ACS
**Key Concepts:**
- Income bracket analysis
- Distribution shape analysis (skewness, kurtosis)
- Percentile-based analysis
- Income concentration metrics
- Geographic income patterns

**Business Applications:**
- Market segmentation for consumer products
- Financial services targeting
- Regional economic profiling

---

### 4️⃣ Employment Forecasting - Counties Tutorial
**File:** `04_Employment_Forecasting_Counties_Tutorial.ipynb`
**Domain:** D03 - Employment & Labor Markets
**Tier:** 3 (Time Series)
**Data Sources:** BLS QCEW (Quarterly Census of Employment and Wages)
**Key Concepts:**
- County-level employment data
- Time series decomposition
- ARIMA forecasting models
- Seasonal pattern analysis
- Employment trend prediction
- Industry-specific employment dynamics

**Business Applications:**
- Workforce planning
- Economic development forecasting
- Regional labor market analysis

---

### 5️⃣ Employment Forecasting - BLS Tutorial
**File:** `05_Employment_Forecasting_BLS_Tutorial.ipynb`
**Domain:** D03 - Employment & Labor Markets
**Tier:** 3 (Time Series)
**Data Sources:** BLS Labor Force Statistics (LNS series)
**Key Concepts:**
- National employment indicators
- Unemployment rate forecasting
- Labor force participation trends
- Prophet time series modeling
- Multi-horizon forecasting
- Confidence interval estimation

**Business Applications:**
- Macroeconomic analysis
- Investment strategy development
- Business cycle planning

---

### 6️⃣ Environmental Burden Tutorial
**File:** `06_Environmental_Burden_Tutorial.ipynb`
**Domain:** D11 - Environmental Justice & Resources
**Tier:** 2 (Predictive)
**Data Sources:** EPA EJScreen
**Key Concepts:**
- Environmental burden indicators
- Spatial analysis of environmental exposures
- Environmental justice assessment
- Predictive modeling of environmental risk
- Demographic-environmental correlations
- Composite risk index construction

**Business Applications:**
- Environmental policy evaluation
- Community health risk assessment
- Environmental justice advocacy
- Real estate risk analysis

---

### 7️⃣ Crime Prediction Tutorial
**File:** `07_Crime_Prediction_Tutorial.ipynb`
**Domain:** D10 - Crime & Safety
**Tier:** 2 (Predictive)
**Data Sources:** FBI UCR/NIBRS API
**Key Concepts:**
- Crime statistics analysis
- Predictive crime modeling
- Random Forest classification
- Feature importance analysis
- Geographic crime patterns
- Crime hotspot identification

**Business Applications:**
- Public safety resource allocation
- Law enforcement strategic planning
- Urban planning and development
- Insurance risk assessment

---

## 🎯 Framework Capabilities Demonstrated

### Data Integration
- ✅ **API Integration:** Census, BLS, EPA, FBI
- ✅ **Secure Credential Management:** Environment-based API key loading
- ✅ **Multiple Data Sources:** Government APIs, public datasets
- ✅ **Data Validation:** Automated quality checks

### Analytics Tiers
- ✅ **Tier 1 (Descriptive):** Statistical summaries, distributions, exploratory analysis
- ✅ **Tier 2 (Predictive):** Machine learning models, classification, regression
- ✅ **Tier 3 (Time Series):** Forecasting, trend analysis, seasonal decomposition

### Machine Learning Models
- ✅ **Linear Models:** OLS Regression, Quantile Regression
- ✅ **Ensemble Methods:** Random Forest, Gradient Boosting
- ✅ **Time Series:** ARIMA, Prophet
- ✅ **Feature Engineering:** Encoding, scaling, selection

### Visualization
- ✅ **Interactive Plotly Charts:** Choropleth maps, scatter plots, time series
- ✅ **Statistical Visualizations:** Lorenz curves, distribution plots, correlation heatmaps
- ✅ **Geographic Mapping:** County/state level visualizations
- ✅ **Model Diagnostics:** Residual plots, feature importance charts

### Socioeconomic Domains Covered
1. **Income & Poverty** (Notebooks 1, 3)
2. **Inequality & Distribution** (Notebook 2)
3. **Employment & Labor Markets** (Notebooks 4, 5)
4. **Environmental Justice** (Notebook 6)
5. **Crime & Safety** (Notebook 7)

---

## 🚀 Getting Started

### Prerequisites
```bash
# Install required packages
pip install -r requirements.txt

# Set up API keys (optional for some notebooks)
export CENSUS_API_KEY="your_key_here"
export BLS_API_KEY="your_key_here"
export FBI_CRIME_API_KEY="your_key_here"
```

### Running Notebooks
1. **Start with Notebook 1** to understand basic framework usage
2. **Progress through notebooks** in order for incremental complexity
3. **Explore specific domains** based on your analytical needs
4. **Modify and experiment** - all notebooks are designed to be extended

### Execution Times
- **Tier 1 Notebooks:** ~3-5 minutes
- **Tier 2 Notebooks:** ~5-10 minutes
- **Tier 3 Notebooks:** ~10-15 minutes

---

## 📖 Documentation

For more information:
- **Framework Documentation:** See `/docs/README.md`
- **API Reference:** See `/docs/api/`
- **Contributing Guide:** See `CONTRIBUTING.md`

---

## 📝 Citation

If you use these notebooks in your research or work, please cite:

```bibtex
@software{kranalytics2025,
  title = {KRAnalytics: Open-Source Socioeconomic Data Science Framework},
  author = {KR-Labs},
  year = {2025},
  url = {https://github.com/KR-Labs/KRAnalytics}
}
```

---

## 📧 Support

- **Issues:** Report bugs or request features via [GitHub Issues](https://github.com/KR-Labs/KRAnalytics/issues)
- **Discussions:** Join community discussions in [GitHub Discussions](https://github.com/KR-Labs/KRAnalytics/discussions)
- **Email:** info@krlabs.dev

---

**Last Updated:** October 14, 2025
**Version:** v1.0
**License:** MIT
