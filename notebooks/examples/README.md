# KRAnalytics Tutorial Notebooks

This directory contains **5 comprehensive tutorial notebooks** demonstrating the capabilities of the KRAnalytics framework across multiple socioeconomic domains.

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

### 2️⃣ Income Distribution Tutorial
**File:** `02_Income_Distribution_Tutorial.ipynb`  
**Domain:** D01 - Income & Poverty Analysis  
**Tier:** 1 (Descriptive)  
**Data Sources:** US Census Bureau ACS  

**Key Concepts:**
- Income bracket analysis
- Distribution shape analysis (skewness, kurtosis)
- Percentile-based analysis
- Income concentration metrics
- Geographic income patterns
- Comparative distribution analysis

**Business Applications:**
- Market segmentation for consumer products
- Financial services targeting
- Regional economic profiling
- Wealth management strategy

---

### 3️⃣ Inequality Analysis Tutorial
**File:** `03_Inequality_Analysis_Tutorial.ipynb`  
**Domain:** D02 - Inequality & Distribution  
**Tier:** 1 (Descriptive)  
**Data Sources:** US Census Bureau ACS  

**Key Concepts:**
- Inequality metrics (Gini coefficient, Theil index)
- Income distribution analysis
- Lorenz curves and cumulative distribution functions
- Comparative inequality analysis across geographies
- Statistical testing for inequality differences
- Decomposition of inequality

**Business Applications:**
- Economic inequality assessment
- Social equity policy evaluation
- Resource allocation optimization
- Regional disparity analysis

---

### 4️⃣ Employment Forecasting Tutorial
**File:** `04_Employment_Forecasting_Tutorial.ipynb`  
**Domain:** D03 - Employment & Labor Markets  
**Tier:** 3 (Time Series)  
**Data Sources:** BLS LAUS (Local Area Unemployment Statistics)  

**Key Concepts:**
- State-level employment data from BLS API
- Time series decomposition (trend, seasonal, residual)
- ARIMA forecasting models
- Prophet time series modeling
- Multi-horizon forecasting (12-month ahead)
- Seasonal pattern analysis
- Unemployment rate prediction
- Confidence interval estimation

**Business Applications:**
- Workforce planning and hiring forecasts
- Economic development forecasting
- State labor market analysis
- Business cycle planning

---

### 5️⃣ Crime Prediction Tutorial
**File:** `05_Crime_Prediction_Tutorial.ipynb`  
**Domain:** D10 - Crime & Safety  
**Tier:** 2 (Predictive)  
**Data Sources:** Synthetic FBI UCR-style data  

**Key Concepts:**
- Crime count prediction (Poisson, Negative Binomial regression)
- Machine learning models (Random Forest, Gradient Boosting)
- Feature importance analysis for crime drivers
- Handling overdispersion in count data
- Model comparison and selection
- Interactive dashboards with Plotly
- Business insights generation

**Business Applications:**
- Public safety resource allocation
- Law enforcement strategic planning
- Crime prevention program targeting
- Urban planning and policy evaluation

---

## 🎯 Framework Capabilities Demonstrated

### Data Integration
- **API Integration:** Census Bureau ACS, BLS LAUS, FRED
- **Secure Credential Management:** Environment-based API key loading
- **Multiple Data Sources:** Government APIs, public datasets, synthetic data
- **Data Validation:** Automated quality checks and preprocessing

### Analytics Tiers
- **Tier 1 (Descriptive):** Statistical summaries, distributions, exploratory analysis (Notebooks 1, 2, 3)
- **Tier 2 (Predictive):** Machine learning models, classification, regression (Notebooks 1, 5)
- **Tier 3 (Time Series):** Forecasting, trend analysis, seasonal decomposition (Notebooks 1, 4)

### Machine Learning Models
-  **Linear Models:** OLS Regression, Quantile Regression
-  **Count Models:** Poisson Regression, Negative Binomial Regression
-  **Ensemble Methods:** Random Forest, Gradient Boosting
-  **Time Series:** ARIMA, Prophet (Facebook Prophet)
-  **Feature Engineering:** Encoding, scaling, selection, importance analysis

### Visualization
-  **Interactive Plotly Charts:** Choropleth maps, scatter plots, time series, 3D plots
-  **Statistical Visualizations:** Lorenz curves, distribution plots, correlation heatmaps
-  **Geographic Mapping:** County and state level visualizations
-  **Model Diagnostics:** Residual plots, feature importance charts, actual vs predicted plots
-  **Business Dashboards:** Interactive multi-panel dashboards with hover details

### Socioeconomic Domains Covered
1. **Income & Poverty** (Notebooks 1, 2)
2. **Inequality & Distribution** (Notebook 3)
3. **Employment & Labor Markets** (Notebook 4)
4. **Crime & Safety** (Notebook 5)

---

##  Getting Started

### Prerequisites
```bash
# Install required packages
pip install pandas numpy statsmodels prophet plotly scikit-learn requests

# Set up API keys (optional - some notebooks work with synthetic data)
export CENSUS_API_KEY="your_key_here"
export BLS_API_KEY="your_key_here"
```

### Running Notebooks
1. **Start with Notebook 1** (Income Analysis) to understand basic framework usage
2. **Explore Notebooks 2-3** for descriptive analytics techniques
3. **Try Notebook 4** for time series forecasting
4. **Complete with Notebook 5** for advanced predictive modeling
5. **Modify and experiment** - all notebooks are designed to be extended

### Execution Times
- **Tier 1 Notebooks (2, 3):** ~3-5 minutes
- **Tier 2 Notebooks (5):** ~5-10 minutes
- **Tier 3 Notebooks (1, 4):** ~10-15 minutes

### Data Requirements
- **Notebooks 1-4:** Require API keys for live data (Census, BLS)
- **Notebook 5:** Uses synthetic data, no API keys required
- All notebooks include fallback mechanisms for missing API keys

---

##  Documentation

For more information:
- **Framework Documentation:** See `/docs/README.md`
- **API Reference:** See `/docs/api/`
- **Contributing Guide:** See `CONTRIBUTING.md`

---

##  Citation

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

##  Support

- **Issues:** Report bugs or request features via [GitHub Issues](https://github.com/KR-Labs/KRAnalytics/issues)
- **Discussions:** Join community discussions in [GitHub Discussions](https://github.com/KR-Labs/KRAnalytics/discussions)
- **Email:** info@krlabs.dev

---

**Last Updated:** October 14, 2025
**Version:** v1.0
**License:** MIT
