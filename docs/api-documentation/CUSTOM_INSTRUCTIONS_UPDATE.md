# Custom Instructions Update - Analytics Model Matrix & Notebook Generation
**Date:** October 8, 2025
**Purpose:** Integrate 19-domain Analytics Model Matrix and master-level notebook generation directive
**Status:** Ready for integration into `.github/copilot-instructions.md`

---

## **ANALYTICS MODEL MATRIX** (October 2025)

### **19-Domain Socioeconomic Analysis Framework**

**STRATEGIC MANDATE**: All notebook development must align with the 19-domain Analytics Model Matrix. This framework represents the complete scope of socioeconomic analysis capabilities across the Khipu Analytics Suite.

### **Domain Architecture**

#### **Domain 1: Income & Poverty Analysis**
**Data Sources:**
- Census ACS API: `acs/acs5` tables (B19001, B19013, B19025, B19301)
- Census SAIPE API: Small Area Income & Poverty Estimates
- Series IDs: `S1901_C01_012E` (median household income), `S1701_C01_042E` (poverty rate)

**Analytic Models:**
- OLS Regression: Income determinants
- GLM (Generalized Linear Models): Non-normal income distributions
- Quantile Regression: Income inequality across distribution
- Gini Coefficient: Income inequality measurement
- Lorenz Curves: Cumulative income distribution visualization

**OSS Tools:** `scikit-learn`, `statsmodels`, `quantreg`, `inequality` (Python)

**Plotly Visualizations:** Box plots, scatter plots with regression lines, histograms with KDE, Lorenz curves, choropleth maps

**Notebook Mapping:**
- Tier 1: `Tier1_Income_Distribution_ACS.ipynb` - Descriptive income statistics
- Tier 2: `Tier2_Income_Prediction_ACS.ipynb` ✅ **COMPLETE** - Predictive income modeling
- Tier 2: `Tier2_Poverty_Determinants_SAIPE.ipynb` - Poverty risk factors

---

#### **Domain 2: Inequality & Distribution**
**Data Sources:**
- Census ACS: Detailed household income tables
- World Bank WDI API: `SI.POV.GINI` (international Gini coefficients)
- Series IDs: `B19082_001E` (Gini index), `B19001_*` (income brackets)

**Analytic Models:**
- Theil Index: Decomposable inequality measure
- Entropy Index: Information-theoretic inequality
- Atkinson Index: Welfare-focused inequality
- Distributional Regression: Inequality across covariates
- Palma Ratio: Top 10% vs bottom 40% income share

**OSS Tools:** `ineqpy`, `inequalipy`, `statsmodels`, `scipy`

**Plotly Visualizations:** Lorenz curves, Theil decomposition charts, distributional regression plots, violin plots

**Notebook Mapping:**
- Tier 1: `Tier1_Inequality_Analysis_ACS.ipynb` ⚠️ **SKELETON** - Inequality metrics calculation
- Tier 2: `Tier2_Inequality_Determinants_ACS.ipynb` - Drivers of inequality

---

#### **Domain 3: Employment & Labor Markets**
**Data Sources:**
- BLS API: Labor Force Statistics (LNS series), QCEW (Quarterly Census)
- Census LEHD/LODES: Origin-destination employment data
- Series IDs: `LNS14000000` (unemployment rate), `LNS12300000` (labor force participation)

**Analytic Models:**
- ARIMA: Unemployment rate forecasting
- Prophet: Seasonal labor market trends
- Panel Models: Employment dynamics across regions
- Random Forest: Employment prediction
- Shift-Share Analysis: Employment composition changes

**OSS Tools:** `statsmodels`, `prophet`, `linearmodels`, `scikit-learn`

**Plotly Visualizations:** Time series with forecasts, heatmaps (employment by industry), sankey diagrams (job flows), choropleth maps

**Notebook Mapping:**
- Tier 2: `Tier2_Employment_Forecasting_BLS.ipynb` ✅ **COMPLETE** - Employment prediction
- Tier 3: `Tier3_Labor_Market_Dynamics_LEHD.ipynb` - Time series analysis
- Tier 4: `Tier4_Employment_Clusters_LODES.ipynb` - Regional employment patterns

---

#### **Domain 4: Education Outcomes**
**Data Sources:**
- NCES IPEDS API: Institutional data (graduation rates, enrollment)
- ACS: Educational attainment tables (B15003)
- Series IDs: `B15003_022E` (bachelor's degree), `IPEDS.graduation_rate_100`

**Analytic Models:**
- Multilevel Models: Student/school/district hierarchies
- Random Forest: Graduation rate prediction
- Gradient Boosting: Educational attainment modeling
- Spatial Regression: Geographic education disparities
- Logistic Regression: College enrollment probability

**OSS Tools:** `statsmodels`, `scikit-learn`, `xgboost`, `pysal`

**Plotly Visualizations:** Bar charts (graduation rates), scatter plots (attainment vs income), choropleth maps, box plots by demographics

**Notebook Mapping:**
- Tier 2: `Tier2_Education_Performance_NCES.ipynb` ⚠️ **SKELETON** - Education outcome modeling
- Tier 4: `Tier4_Education_Clusters_ACS.ipynb` - Regional education patterns

---

#### **Domain 5: Health & Epidemiology**
**Data Sources:**
- CDC WONDER API: Mortality data, health statistics
- County Health Rankings: Health outcomes, risk factors
- ACS: Health insurance coverage (B27001)

**Analytic Models:**
- Cox Proportional Hazards: Survival analysis
- Bayesian Hierarchical Models: Disease mapping
- XGBoost: Health outcome prediction
- Spatial Clustering: Disease hotspots
- SIR Models: Disease transmission dynamics

**OSS Tools:** `lifelines`, `pymc3`, `scikit-learn`, `pysal`, `scipy`

**Plotly Visualizations:** Survival curves, risk maps (choropleth), heatmaps (health disparities), epidemic curves

**Notebook Mapping:**
- Tier 2: `Tier2_Health_Outcomes_CDC.ipynb` - Health predictor modeling
- Tier 6: `Tier6_Mortality_Analysis_CDC.ipynb` - Advanced mortality analytics

---

#### **Domain 6: Housing & Displacement**
**Data Sources:**
- HUD Fair Market Rent: Rental market data
- Zillow Research Data: ZHVI (Home Value Index), rental index
- Eviction Lab: Eviction rates, filings
- ACS: Housing cost burden (B25070)

**Analytic Models:**
- Spatial Econometrics: Housing price spillovers
- Hedonic Pricing: Property value determinants
- Random Forest: Home value prediction
- Survival Analysis: Time to eviction
- Spatial Lag/Error Models: Geographic housing patterns

**OSS Tools:** `pysal`, `scikit-learn`, `geopandas`, `statsmodels`

**Plotly Visualizations:** Scatter plots (hedonic), choropleth maps (housing values), time series (evictions), bubble maps

**Notebook Mapping:**
- Tier 1: `Tier1_Housing_Markets_HUD.ipynb` ⚠️ **SKELETON** - Housing market descriptives
- Tier 2: `Tier2_Housing_Hedonic_Zillow.ipynb` ⚠️ **SKELETON** - Hedonic pricing models
- Tier 6: `Tier6_Eviction_Risk_Analysis.ipynb` - Eviction prediction

---

#### **Domain 7: Public Finance & Taxation**
**Data Sources:**
- IRS SOI: Tax statistics, 990 nonprofit data
- USASpending.gov API: Federal spending, contracts
- ACS: Commuting costs, tax burden proxies

**Analytic Models:**
- Input-Output Analysis: Economic multipliers
- Network Analysis: Fund flows between sectors
- Bayesian Networks: Tax policy impact
- Regression Analysis: Revenue determinants
- Spatial Fiscal Analysis: Tax competition

**OSS Tools:** `networkx`, `scipy`, `statsmodels`, `pymc3`

**Plotly Visualizations:** Sankey diagrams (fund flows), network graphs (spending), choropleth maps (tax burden), treemaps (budget)

**Notebook Mapping:**
- Tier 3: `Tier3_Tax_Revenue_Forecasting_IRS.ipynb` - Revenue prediction
- Tier 5: `Tier5_Fiscal_Network_Analysis.ipynb` - Public finance networks

---

#### **Domain 8: Trade & Value Chains**
**Data Sources:**
- BEA API: Input-output tables, trade data
- Census International Trade API: Import/export by state
- Series IDs: `BEASTAT.TradeGoodsByState`, `INTLTRADE.IM_*`

**Analytic Models:**
- Gravity Models: Trade flow prediction
- Multiregional Input-Output: Supply chain analysis
- ML Regression: Trade determinants
- Network Analysis: Value chain structure
- Structural Equation Models: Trade relationships

**OSS Tools:** `scipy`, `scikit-learn`, `networkx`, `statsmodels`

**Plotly Visualizations:** Sankey diagrams (trade flows), chord diagrams (bilateral trade), network graphs, choropleth maps

**Notebook Mapping:**
- Tier 3: `Tier3_Trade_Flows_BEA.ipynb` - Trade forecasting
- Tier 5: `Tier5_Value_Chain_Analysis_BEA.ipynb` - Supply chain networks

---

#### **Domain 9: Urban Dynamics & Land Use**
**Data Sources:**
- Census TIGER: Geospatial boundaries, roads
- OpenStreetMap Overpass API: Points of interest, amenities
- EPA EJScreen: Environmental justice indicators
- ACS: Commuting patterns (B08303)

**Analytic Models:**
- GIS Analysis: Spatial pattern detection
- K-Means Clustering: Neighborhood typologies
- DBSCAN: Density-based clustering
- Spatial Autoregression: Land use spillovers
- Agent-Based Models: Urban growth simulation

**OSS Tools:** `geopandas`, `scikit-learn`, `pysal`, `osmnx`, `mesa`

**Plotly Visualizations:** Mapbox layers, scatter mapbox (points of interest), choropleth maps, 3D surface plots

**Notebook Mapping:**
- Tier 4: `Tier4_Urban_Typologies_OSM.ipynb` - Neighborhood clustering
- Tier 6: `Tier6_Land_Use_Prediction_TIGER.ipynb` - Urban growth modeling

---

#### **Domain 10: Crime & Safety**
**Data Sources:**
- FBI UCR/NIBRS API: Crime statistics
- ACS: Safety perceptions, reporting rates
- Series IDs: `FBI.CRIME.{state}.{type}` (assault, burglary, etc.)

**Analytic Models:**
- Hotspot Analysis: Spatial crime clustering
- Poisson Regression: Crime count models
- Negative Binomial: Overdispersed crime counts
- Random Forest: Crime prediction
- Spatial-Temporal Models: Crime dynamics

**OSS Tools:** `pysal`, `statsmodels`, `scikit-learn`, `scipy`

**Plotly Visualizations:** Heatmaps (crime density), choropleth maps, time series (crime trends), scatter plots

**Notebook Mapping:**
- Tier 2: `Tier2_Crime_Prediction_FBI.ipynb` - Crime rate modeling
- Tier 6: `Tier6_Crime_Hotspots_FBI.ipynb` - Spatial crime analysis

---

#### **Domain 11: Environmental Justice & Resources**
**Data Sources:**
- EPA EJScreen: Environmental burden indicators
- USGS Water Services API: Water quality
- NOAA Climate API: Climate data, weather stations
- ACS: Housing proximity to hazards

**Analytic Models:**
- Spatial Regression: Environmental burden distribution
- Risk Index Construction: Composite exposure metrics
- Bayesian Models: Uncertainty quantification
- Multivariate Analysis: Multiple exposures
- Spatial Clustering: Environmental hotspots

**OSS Tools:** `pysal`, `scipy`, `pymc3`, `scikit-learn`, `geopandas`

**Plotly Visualizations:** Choropleth maps (burden), scatter plots (exposure vs demographics), heatmaps, risk matrices

**Notebook Mapping:**
- Tier 2: `Tier2_Environmental_Burden_EPA.ipynb` - Exposure modeling
- Tier 6: `Tier6_Environmental_Justice_Analysis.ipynb` - Advanced EJ analytics

---

#### **Domain 12: Cultural Capital & Creative Economy**
**Data Sources:**
- NEA Grants: Arts funding data
- IRS Form 990: Nonprofit cultural organizations
- ACS: Arts/culture employment (NAICS 71)

**Analytic Models:**
- Factor Analysis: Cultural capital dimensions
- PCA: Cultural indicators reduction
- Cluster Analysis: Cultural region typologies
- Random Forest: Arts organization success
- Network Analysis: Cultural ecosystem structure

**OSS Tools:** `scikit-learn`, `factor_analyzer`, `networkx`, `scipy`

**Plotly Visualizations:** Bar charts (grants by type), network graphs (organizations), choropleth maps, scatter matrices

**Notebook Mapping:**
- Tier 4: `Tier4_Cultural_Capital_Clusters_NEA.ipynb` - Cultural typologies
- Tier 5: `Tier5_Creative_Economy_Network_990.ipynb` - Cultural networks

---

#### **Domain 13: Institutional Trust & Legitimacy**
**Data Sources:**
- GSS (General Social Survey): Trust indicators
- ACS: Civic engagement proxies (voting, volunteering)

**Analytic Models:**
- Structural Equation Models: Latent trust constructs
- Bayesian Networks: Trust relationships
- Graph Analysis: Social capital networks
- Multilevel Models: Individual/community trust
- Time Series: Trust evolution

**OSS Tools:** `semopy`, `pymc3`, `networkx`, `statsmodels`

**Plotly Visualizations:** Path diagrams (SEM), network graphs (trust networks), time series (trust trends), bar charts

**Notebook Mapping:**
- Tier 2: `Tier2_Trust_Determinants_GSS.ipynb` - Trust predictor modeling
- Tier 5: `Tier5_Social_Capital_Networks_GSS.ipynb` - Trust network analysis

---

#### **Domain 14: Migration & Demographics**
**Data Sources:**
- ACS Migration Tables: County-to-county flows (B07001)
- IRS Migration Data: Tax return-based migration
- Series IDs: `B07001_065E` (moved from different state)

**Analytic Models:**
- Gravity Models: Migration flow prediction
- Spatial Interaction Models: Origin-destination dynamics
- XGBoost: Migration determinants
- Network Analysis: Migration networks
- Cohort Component Models: Population projection

**OSS Tools:** `scikit-learn`, `networkx`, `scipy`, `statsmodels`

**Plotly Visualizations:** Sankey diagrams (migration flows), chord diagrams, choropleth maps, network graphs

**Notebook Mapping:**
- Tier 3: `Tier3_Migration_Forecasting_ACS.ipynb` - Migration prediction
- Tier 5: `Tier5_Migration_Networks_IRS.ipynb` - Migration network analysis

---

#### **Domain 15: Social Networks & Connectivity**
**Data Sources:**
- FCC Broadband: Internet access, speed by location
- Census LEHD LODES: Worker commuting networks
- ACS: Commuting patterns, telecommunications access

**Analytic Models:**
- Graph Theory: Network structure analysis
- Network Centrality: Key node identification
- Community Detection: Network clustering
- Diffusion Models: Information spread
- Network Regression: Tie prediction

**OSS Tools:** `networkx`, `graph-tool`, `scikit-network`, `scipy`

**Plotly Visualizations:** Network graphs, sankey diagrams (commuting), chord diagrams, heatmaps (connectivity)

**Notebook Mapping:**
- Tier 4: `Tier4_Connectivity_Networks_FCC.ipynb` - Digital divide clustering
- Tier 5: `Tier5_Commuting_Networks_LODES.ipynb` - Labor market networks

---

#### **Domain 16: Policy Evaluation & Behavioral Dynamics**
**Data Sources:**
- BLS Consumer Expenditure Survey: Spending patterns
- State Administrative Data: Policy adoption dates
- ACS: Behavioral outcome proxies

**Analytic Models:**
- Difference-in-Differences: Causal policy impact
- Causal Inference: Counterfactual estimation
- Propensity Score Matching: Treatment effect isolation
- Random Forest: Outcome prediction
- Synthetic Control: Policy evaluation

**OSS Tools:** `causalinference`, `econml`, `scikit-learn`, `statsmodels`

**Plotly Visualizations:** Time series (treatment/control), bar charts (effect sizes), scatter plots (propensity scores)

**Notebook Mapping:**
- Tier 2: `Tier2_Policy_Impact_Analysis_BLS.ipynb` - Policy effect modeling
- Tier 5: `Tier5_Causal_Inference_Analysis.ipynb` - Advanced causal methods

---

#### **Domain 17: Resilience to Shocks**
**Data Sources:**
- FEMA Disasters API: Disaster declarations, aid
- USDA NASS: Agricultural statistics, crop data
- ACS: Economic vulnerability indicators

**Analytic Models:**
- Stress Testing: Shock sensitivity analysis
- Scenario Analysis: Multiple shock simulations
- Bayesian Change-Point: Shock detection
- Resilience Index: Recovery capacity measurement
- Time Series: Post-shock recovery trajectories

**OSS Tools:** `scipy`, `pymc3`, `scikit-learn`, `statsmodels`

**Plotly Visualizations:** Time series (shock events), bar charts (resilience scores), choropleth maps, waterfall charts

**Notebook Mapping:**
- Tier 3: `Tier3_Disaster_Impact_Forecasting_FEMA.ipynb` - Recovery prediction
- Tier 6: `Tier6_Resilience_Analysis_FEMA.ipynb` - Advanced resilience metrics

---

#### **Domain 18: Futures & Foresight**
**Data Sources:**
- FRED API: Macroeconomic indicators
- BLS API: Labor market projections
- BEA API: GDP forecasts
- IPCC/IIASA: Climate projections (NetCDF files)

**Analytic Models:**
- Scenario Simulation: Multiple future pathways
- System Dynamics: Feedback loop modeling
- Monte Carlo Simulation: Uncertainty quantification
- Ensemble Forecasting: Model averaging
- Long-range Time Series: Multi-horizon prediction

**OSS Tools:** `scipy`, `pymc3`, `prophet`, `statsmodels`, `xarray`

**Plotly Visualizations:** Fan charts (forecast uncertainty), scenario trees, time series (projections), waterfall charts

**Notebook Mapping:**
- Tier 3: `Tier3_Economic_Forecasting_FRED.ipynb` ⚠️ **SKELETON** - Macro forecasting
- Tier 5: `Tier5_Scenario_Analysis_Ensemble.ipynb` - Multi-model forecasting

---

#### **Domain 19: Information Ecosystems & Narrative Power**
**Data Sources:**
- GDELT API: Global news events, media monitoring
- Media Cloud API: News stories, media analysis

**Analytic Models:**
- NLP: Text analysis, entity extraction
- Topic Modeling (LDA): Thematic structure
- Sentiment Analysis: Opinion mining
- Network Analysis: Media source relationships
- Time Series: Narrative evolution tracking

**OSS Tools:** `spacy`, `gensim`, `transformers`, `networkx`, `nltk`

**Plotly Visualizations:** Word clouds, time series (topic prevalence), network graphs (media sources), heatmaps (sentiment)

**Notebook Mapping:**
- Tier 4: `Tier4_Media_Topic_Modeling_GDELT.ipynb` - Topic extraction
- Tier 6: `Tier6_Narrative_Network_Analysis.ipynb` - Media ecosystem mapping

---

### **API Security & Configuration Standards**

#### **Environment Variable Management**
**CRITICAL RULE**: **NEVER** hardcode API keys in notebooks. Always use environment-based credential management.

**API Configuration File:** `/KR-Labs-khipu/configs/apikeys`

**Standard API Loading Pattern:**
```python
# At top of every notebook requiring API access
import os
from pathlib import Path

def load_api_key(api_name: str, required: bool = True) -> str:
    """
    Load API key from environment or config file.

    Args:
        api_name: Name of API key (e.g., 'CENSUS_API_KEY')
        required: Whether to raise error if key not found

    Returns:
        API key string

    Raises:
        ValueError: If required key not found
    """
    # Priority 1: Environment variable
    key = os.environ.get(api_name)

    if not key:
        # Priority 2: Config file
        config_path = Path(__file__).parent.parent.parent / 'KR-Labs-khipu' / 'configs' / 'apikeys'
        if config_path.exists():
            with open(config_path, 'r') as f:
                for line in f:
                    if line.strip().startswith(api_name):
                        key = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break

    if not key and required:
        raise ValueError(
            f"API key '{api_name}' not found. "
            f"Set it in environment variables or {config_path}"
        )

    return key

# Usage in notebooks
census_api_key = load_api_key('CENSUS_API_KEY')
bls_api_key = load_api_key('BLS_API_KEY')
fred_api_key = load_api_key('FRED_API_KEY')
noaa_api_key = load_api_key('NOAA_API_KEY', required=False)  # Optional
```

#### **Required vs Optional APIs**

**Core APIs (Required - 4):**
1. `CENSUS_API_KEY` - Census ACS, SAIPE, LEHD, TIGER
2. `BLS_API_KEY` - Labor statistics, employment data
3. `FRED_API_KEY` - Macroeconomic indicators
4. `BEA_API_KEY` - Economic accounts, trade data

**Enhanced APIs (Optional - 6):**
5. `NCES_API_KEY` - Education outcomes
6. `FBI_CRIME_API_KEY` - Crime statistics
7. `NOAA_API_KEY` - Climate/weather data
8. `FEMA_API_KEY` - Disaster declarations
9. `USDA_NASS_API_KEY` - Agricultural data
10. `MEDIACLOUD_API_KEY` - Media analysis

**Open APIs (No Key Required - 6):**
11. World Bank API - International data
12. USASpending.gov API - Federal spending
13. OpenStreetMap Overpass API - Geospatial data
14. USGS Water Services - Water quality
15. GDELT API - News events
16. Census TIGER - Geospatial boundaries

**Data Downloads (No API Available - 11):**
17. County Health Rankings (CSV)
18. HUD Fair Market Rent (Excel/CSV)
19. Zillow Research Data (CSV)
20. Eviction Lab (CSV)
21. IRS SOI Statistics (CSV/Excel)
22. EPA EJScreen (CSV/Shapefile)
23. NEA Open Data (CSV/Excel)
24. GSS Survey Data (SPSS/Stata)
25. IRS Migration Data (CSV)
26. FCC Broadband Data (CSV)
27. IPCC Climate Projections (NetCDF)

---

### **Domain-Tier Mapping Matrix**

| Domain | Tier 1 (Descriptive) | Tier 2 (Predictive) | Tier 3 (Time Series) | Tier 4 (Clustering) | Tier 5 (Ensemble) | Tier 6 (Advanced) |
|--------|---------------------|---------------------|---------------------|---------------------|------------------|------------------|
| 1. Income & Poverty | Distribution ✅ | Prediction ✅ | - | - | - | Poverty Risk |
| 2. Inequality | Analysis ⚠️ | Determinants | - | - | - | Decomposition |
| 3. Employment | - | Forecasting ✅ | Dynamics | Clusters | - | - |
| 4. Education | - | Performance ⚠️ | - | Clusters | - | - |
| 5. Health | - | Outcomes | - | - | - | Mortality |
| 6. Housing | Markets ⚠️ | Hedonic ⚠️ | - | - | - | Eviction Risk |
| 7. Public Finance | - | - | Revenue | - | Networks | - |
| 8. Trade | - | - | Flows | - | Value Chains | - |
| 9. Urban Dynamics | - | - | - | Typologies | - | Land Use |
| 10. Crime & Safety | - | Prediction | - | - | - | Hotspots |
| 11. Environmental | - | Burden | - | - | - | Justice |
| 12. Cultural Capital | - | - | - | Clusters | Networks | - |
| 13. Institutional Trust | - | Determinants | Trends | - | Networks | - |
| 14. Migration | - | - | Forecasting | - | Networks | - |
| 15. Social Networks | - | - | - | Connectivity | Networks | - |
| 16. Policy Evaluation | - | Impact | - | - | Causal | - |
| 17. Resilience | - | - | Impact | - | - | Analysis |
| 18. Futures | - | - | Forecasting ⚠️ | - | Scenarios | - |
| 19. Information | - | - | - | Topics | - | Narratives |

**Legend:**
- ✅ = Complete notebook
- ⚠️ = Skeleton notebook
- Blank = Not yet created

---

## **MASTER-LEVEL NOTEBOOK GENERATION DIRECTIVE**

### **AI Agent Operational Protocol for Notebook Creation**

**MANDATE**: When creating ANY notebook in the Khipu Analytics Suite ecosystem, you MUST adhere to the following comprehensive requirements. These standards ensure enterprise-grade quality, academic rigor, and seamless integration across the 19-domain Analytics Model Matrix.

---

### **1. Notebook Metadata & Header Standards**

**Every notebook must begin with:**

```python
"""
═══════════════════════════════════════════════════════════════════════════
 {NOTEBOOK TITLE}
═══════════════════════════════════════════════════════════════════════════

Author: [Your Name / Khipu Analytics Team]
Affiliation: Khipu Analytics Suite
Version: v1.0
Date: {YYYY-MM-DD}
UUID: {unique-identifier}
Tier: {1-6}
Domain: {One of 19 Analytics Model Matrix domains}

════════════════════════════════════════════════════════════════════════════
 CITATION BLOCK
═══════════════════════════════════════════════════════════════════════════

To cite this notebook in publications:
    [Author Name]. ({Year}). {Notebook Title}. Khipu Analytics Suite,
    Tier {X} Analytics Framework. doi:{optional-doi}

To cite the framework:
    Khipu Analytics Suite. (2025). 6-Tier Hierarchical Learning Framework
    for Socioeconomic Data Science. https://github.com/KhipuAnalytics/khipu-analytics-suite

════════════════════════════════════════════════════════════════════════════
 NOTEBOOK DESCRIPTION
════════════════════════════════════════════════════════════════════════════

**Purpose:** [2-3 sentence description of analytical objective]

**Analytics Model Matrix Domain:** {Domain Name}

**Data Sources:**
- {Primary API/Dataset}: {Description}
- {Secondary API/Dataset}: {Description}

**Analytic Methods:**
- {Method 1}: {Purpose}
- {Method 2}: {Purpose}
- {Method 3}: {Purpose}

**Business Applications:**
1. {Application 1}
2. {Application 2}
3. {Application 3}

**Expected Insights:**
- {Insight 1}
- {Insight 2}

**Execution Time:** ~{X} minutes on standard hardware

════════════════════════════════════════════════════════════════════════════
 PREREQUISITES & DEPENDENCIES
════════════════════════════════════════════════════════════════════════════

**Prior Knowledge:**
- {Concept/Notebook 1}
- {Concept/Notebook 2}

**Required Notebooks (must complete first):**
- `{TierX_Notebook_Name.ipynb}` - {Purpose}
- `{TierY_Notebook_Name.ipynb}` - {Purpose}

**Next Steps After Completion:**
- `{TierZ_Notebook_Name.ipynb}` - {Advanced application}

**Python Environment:**
- Python ≥ 3.9
- See requirements.txt for package versions

════════════════════════════════════════════════════════════════════════════
 PROVENANCE & LICENSING
════════════════════════════════════════════════════════════════════════════

**Data Provenance:**
- {Dataset 1}: Source {Agency}, License {CC-BY/Public Domain}
- {Dataset 2}: Source {Organization}, License {License Type}

**Code License:** MIT License (see LICENSE file)

**Third-Party Acknowledgments:**
- {Library/Dataset}: {Citation}

════════════════════════════════════════════════════════════════════════════
"""
```

---

### **2. Cross-References & Execution Provenance**

**At start of notebook (after header):**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 1. EXECUTION ENVIRONMENT SETUP
# ═══════════════════════════════════════════════════════════════════════════

import sys
from pathlib import Path

# Add project root to path
project_root = Path.cwd().parent.parent
sys.path.append(str(project_root))

# Execution tracking (REQUIRED)
from src.khipu_analytics.execution_tracking import setup_notebook_tracking

metadata = setup_notebook_tracking(
    notebook_name="{TierX_NotebookName.ipynb}",
    version="v1.0",
    seed=42,  # Reproducibility
    save_log=True
)

print(f"✅ Execution tracking initialized: {metadata['execution_id']}")
print(f"📅 Start time: {metadata['start_time']}")
print(f"🌱 Random seed: {metadata['seed']}")
```

---

### **3. Data Ingestion & API Integration**

**Standard API Loading Pattern:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 2. API AUTHENTICATION & DATA LOADING
# ═══════════════════════════════════════════════════════════════════════════

import os
import requests
import pandas as pd
from pathlib import Path

def load_api_key(api_name: str, required: bool = True) -> str:
    """
    Load API key from environment or config file.

    SECURITY NOTE: API keys should NEVER be hardcoded in notebooks.
    Store in /KR-Labs-khipu/configs/apikeys or environment variables.
    """
    # Priority 1: Environment variable
    key = os.environ.get(api_name)

    if not key:
        # Priority 2: Config file
        config_path = Path.cwd().parent.parent.parent / 'KR-Labs-khipu' / 'configs' / 'apikeys'
        if config_path.exists():
            with open(config_path, 'r') as f:
                for line in f:
                    if line.strip().startswith(api_name):
                        key = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break

    if not key and required:
        raise ValueError(f"API key '{api_name}' not found. Set in environment or config file.")

    return key

# Load API keys (based on Analytics Model Matrix domain)
{api_name}_api_key = load_api_key('{API_KEY_NAME}')

print(f"✅ API authentication successful: {api_name}")

# ───────────────────────────────────────────────────────────────────────────
# 2.1. Data Ingestion from {Data Source}
# ───────────────────────────────────────────────────────────────────────────

def load_{dataset}_data(
    api_key: str,
    series_ids: list,
    start_year: int = 2018,
    end_year: int = 2023,
    geography: str = 'state'
) -> pd.DataFrame:
    """
    Load data from {API Name} API.

    Args:
        api_key: API authentication key
        series_ids: List of series IDs (from Analytics Model Matrix)
        start_year: Start year for data retrieval
        end_year: End year for data retrieval
        geography: Geographic level (state, county, metro, etc.)

    Returns:
        DataFrame with {data description}

    Data Source: {Agency Name} - {Dataset Name}
    API Endpoint: {API URL}
    Documentation: {API docs URL}
    """
    base_url = "{API_BASE_URL}"

    # Construct API request
    params = {
        'key': api_key,
        'seriesid': ','.join(series_ids),
        'startyear': start_year,
        'endyear': end_year,
        'registrationkey': api_key
    }

    try:
        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Parse response (implementation depends on API structure)
        df = pd.DataFrame(data['Results']['series'])

        # Data validation
        assert len(df) > 0, "No data returned from API"
        assert df['value'].notna().sum() > 0, "All values are missing"

        print(f"✅ Data loaded: {len(df):,} records from {start_year}-{end_year}")
        print(f"📊 Series IDs: {', '.join(series_ids)}")
        print(f"🗺️  Geographic level: {geography}")

        return df

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        print(f"ℹ️  Falling back to cached data if available...")
        # Implement fallback to cached data or sample dataset
        raise

# Execute data loading
df_raw = load_{dataset}_data(
    api_key={api_name}_api_key,
    series_ids=['{SERIES_ID_1}', '{SERIES_ID_2}'],  # From Analytics Model Matrix
    start_year=2018,
    end_year=2023,
    geography='state'
)

# Display data sample
print("\n📋 Data Preview:")
print(df_raw.head(10))
print(f"\n📏 Shape: {df_raw.shape[0]:,} rows × {df_raw.shape[1]} columns")
```

---

### **4. Analytic Models & Algorithms**

**Follow Analytics Model Matrix specifications for each domain:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 5. ANALYTIC MODEL IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════════════════

# Import domain-specific models from Analytics Model Matrix
from sklearn.{model_family} import {ModelClass}
from statsmodels.{module} import {StatisticalModel}

# ───────────────────────────────────────────────────────────────────────────
# 5.1. {Model Name} Implementation
# ───────────────────────────────────────────────────────────────────────────

"""
Model: {Model Name}
Domain: {Analytics Model Matrix Domain}
Purpose: {Analytical objective}
Reference: {Academic citation or documentation}
"""

# Model specification
model = {ModelClass}(
    # Hyperparameters aligned with domain best practices
    {param1}={value1},
    {param2}={value2},
    random_state=42  # Reproducibility
)

# Model training
print(f"\n🔬 Training {Model Name}...")
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)

# Performance metrics (domain-appropriate)
from sklearn.metrics import {metric1}, {metric2}

{metric1}_score = {metric1}(y_test, y_pred)
{metric2}_score = {metric2}(y_test, y_pred)

print(f"✅ Model trained successfully")
print(f"📊 {Metric1}: {metric1_score:.4f}")
print(f"📊 {Metric2}: {metric2_score:.4f}")

# ───────────────────────────────────────────────────────────────────────────
# 5.2. Model Comparison (REQUIRED for Tier 2+)
# ───────────────────────────────────────────────────────────────────────────

"""
Compare multiple models as specified in Analytics Model Matrix.
Minimum 3 models for comprehensive evaluation.
"""

models = {
    '{Model1}': {Model1Class}({params}),
    '{Model2}': {Model2Class}({params}),
    '{Model3}': {Model3Class}({params})
}

results = []

for name, model in models.items():
    print(f"\n🔬 Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    results.append({
        'Model': name,
        '{Metric1}': {metric1}(y_test, y_pred),
        '{Metric2}': {metric2}(y_test, y_pred),
        'Training Time': training_time
    })

# Results table
results_df = pd.DataFrame(results).sort_values('{Primary Metric}', ascending=False)

print("\n📊 Model Comparison Results:")
print(results_df.to_string(index=False))

# Select best model
best_model_name = results_df.iloc[0]['Model']
print(f"\n🏆 Best Model: {best_model_name}")
```

---

### **5. Visualization & Insights**

**Use PlotlyVisualizationEngine for ALL visualizations:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 6. VISUALIZATION & INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════

from tools.plotly_visualization_engine import PlotlyVisualizationEngine

viz_engine = PlotlyVisualizationEngine()

# ───────────────────────────────────────────────────────────────────────────
# 6.1. Domain-Specific Visualizations
# ───────────────────────────────────────────────────────────────────────────

"""
Visualization types specified in Analytics Model Matrix:
{Domain Name}: {Viz Type 1}, {Viz Type 2}, {Viz Type 3}
"""

# Generate ML-driven visualizations
charts = viz_engine.generate_tier_visualizations(
    data=df_results,
    tier_type="tier_{X}",
    analysis_focus="{domain_focus}",
    domain="{Analytics Model Matrix Domain}"
)

# Display charts
for i, chart in enumerate(charts, 1):
    chart.show()
    print(f"📊 Chart {i}: {chart.layout.title.text}")

# ───────────────────────────────────────────────────────────────────────────
# 6.2. Business Insights Generation
# ───────────────────────────────────────────────────────────────────────────

"""
CRITICAL: Every notebook must conclude with actionable business insights.
Connect analytical findings to real-world applications.
"""

print("\n" + "="*80)
print(" KEY INSIGHTS & RECOMMENDATIONS")
print("="*80)

insights = [
    f"1. {Insight based on model results}",
    f"2. {Geographic/demographic pattern identified}",
    f"3. {Policy/business implication}",
    f"4. {Recommendation for action}"
]

for insight in insights:
    print(f"\n💡 {insight}")

print("\n" + "="*80)
```

---

### **6. Sampling & Intelligent Data Handling**

**Implement tier-appropriate sampling strategies:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 3. INTELLIGENT DATA SAMPLING
# ═══════════════════════════════════════════════════════════════════════════

"""
Sampling Strategy (from Analytics Model Matrix):
- Tier 1-2: Full datasets up to 100K rows
- Tier 3-6: Intelligent sampling for 500K+ datasets
- Distribution analysis: Force full datasets
- Time series: Maintain temporal continuity
- Anomaly detection: Preserve rare events
"""

from tools.kaggle_dataset_manager import KaggleDatasetManager

# Determine sampling strategy based on tier and analysis type
TIER_CONFIG = {
    "dataset_size_threshold": 150000 if tier in [1, 2] else 500000,
    "sampling_method": "stratified" if analysis_type == "distribution" else "random",
    "sample_fraction": 1.0 if tier in [1, 2] else 0.3,
    "preserve_distributions": True if analysis_type == "distribution" else False,
    "maintain_temporal_order": True if tier == 3 else False
}

# Apply intelligent sampling
if len(df_raw) > TIER_CONFIG['dataset_size_threshold']:
    print(f"\n📊 Dataset size ({len(df_raw):,} rows) exceeds threshold")
    print(f"🎯 Applying {TIER_CONFIG['sampling_method']} sampling...")

    if TIER_CONFIG['sampling_method'] == 'stratified':
        # Stratified sampling (preserve distributions)
        df = df_raw.groupby('{stratify_column}', group_keys=False).apply(
            lambda x: x.sample(frac=TIER_CONFIG['sample_fraction'], random_state=42)
        )
    else:
        # Random sampling
        df = df_raw.sample(frac=TIER_CONFIG['sample_fraction'], random_state=42)

    print(f"✅ Sampled dataset: {len(df):,} rows ({len(df)/len(df_raw)*100:.1f}% of original)")
else:
    df = df_raw.copy()
    print(f"✅ Using full dataset: {len(df):,} rows")
```

---

### **7. Workspace Cohesion Standards**

**Ensure integration with ecosystem:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 8. NOTEBOOK REGISTRATION & ECOSYSTEM INTEGRATION
# ═══════════════════════════════════════════════════════════════════════════

"""
REQUIRED: Register notebook in config/notebook_registry.json

Entry format:
{
  "notebook_name": "{TierX_NotebookName.ipynb}",
  "tier": {X},
  "domain": "{Analytics Model Matrix Domain}",
  "category": "{analytical_category}",
  "difficulty": "{beginner|intermediate|advanced}",
  "data_sources": ["{API1}", "{API2}"],
  "models": ["{Model1}", "{Model2}"],
  "business_applications": [
    "{Application 1}",
    "{Application 2}"
  ],
  "technical_features": [
    "{Feature 1}",
    "{Feature 2}"
  ],
  "estimated_runtime_minutes": {X},
  "requires_api_keys": ["{API_KEY_NAME}"],
  "prerequisites": ["{PrerequisiteNotebook.ipynb}"],
  "next_steps": ["{AdvancedNotebook.ipynb}"]
}
"""

# Verify registration (automated check)
import json
from pathlib import Path

registry_path = Path.cwd().parent.parent / 'config' / 'notebook_registry.json'

if registry_path.exists():
    with open(registry_path, 'r') as f:
        registry = json.load(f)

    notebook_name = "{TierX_NotebookName.ipynb}"

    if notebook_name in [nb['notebook_name'] for nb in registry['notebooks']]:
        print(f"✅ Notebook registered in ecosystem")
    else:
        print(f"⚠️  WARNING: Notebook not found in registry - add entry to config/notebook_registry.json")
else:
    print(f"⚠️  Registry file not found: {registry_path}")

# Cross-platform integration check
khipu_executor_path = Path.cwd().parent.parent.parent / 'KR-Labs-khipu' / 'khipu' / 'core' / 'notebook_executor.py'

if khipu_executor_path.exists():
    print("✅ Khipu notebook executor available for production deployment")
else:
    print("ℹ️  Khipu executor not found - notebook available for educational use only")
```

---

### **8. Reproducibility & Logging**

**Complete provenance tracking:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 9. EXECUTION SUMMARY & PROVENANCE
# ═══════════════════════════════════════════════════════════════════════════

from datetime import datetime
import platform

# Generate execution summary
execution_summary = {
    "notebook": "{TierX_NotebookName.ipynb}",
    "version": "v1.0",
    "execution_id": metadata['execution_id'],
    "start_time": metadata['start_time'],
    "end_time": datetime.now().isoformat(),
    "duration_seconds": (datetime.now() - datetime.fromisoformat(metadata['start_time'])).total_seconds(),
    "python_version": platform.python_version(),
    "platform": platform.platform(),
    "random_seed": metadata['seed'],
    "data_sources": [
        {
            "name": "{Data Source}",
            "api": "{API Name}",
            "series_ids": ["{SERIES_ID_1}", "{SERIES_ID_2}"],
            "records": len(df_raw),
            "date_range": f"{df_raw['date'].min()} to {df_raw['date'].max()}"
        }
    ],
    "models_trained": [
        {
            "name": "{Model Name}",
            "parameters": {model.get_params()},
            "performance": {
                "{metric1}": {metric1_score},
                "{metric2}": {metric2_score}
            }
        }
    ],
    "visualizations_generated": len(charts),
    "output_files": []
}

# Save execution log
log_path = Path.cwd().parent.parent / 'logs' / 'execution' / f"{execution_summary['execution_id']}.json"
log_path.parent.mkdir(parents=True, exist_ok=True)

with open(log_path, 'w') as f:
    json.dump(execution_summary, f, indent=2)

print(f"\n✅ Execution log saved: {log_path}")

# Display summary
print("\n" + "="*80)
print(" EXECUTION SUMMARY")
print("="*80)
print(f"📓 Notebook: {execution_summary['notebook']}")
print(f"⏱️  Duration: {execution_summary['duration_seconds']:.2f} seconds")
print(f"📊 Data records processed: {execution_summary['data_sources'][0]['records']:,}")
print(f"🤖 Models trained: {len(execution_summary['models_trained'])}")
print(f"📈 Visualizations: {execution_summary['visualizations_generated']}")
print(f"🔍 Execution ID: {execution_summary['execution_id']}")
print("="*80)
```

---

### **9. Documentation & Responsible Use**

**Include ethical considerations and limitations:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 10. RESPONSIBLE USE & LIMITATIONS
# ═══════════════════════════════════════════════════════════════════════════

"""
ETHICAL CONSIDERATIONS:

1. Data Privacy:
   - This analysis uses aggregated {geographic level} data
   - No individual-level identifiable information is used
   - Results should not be used to make decisions about individuals

2. Bias & Fairness:
   - Model may reflect historical biases in data
   - Results should be interpreted in socioeconomic context
   - Consider disparate impact across demographic groups

3. Limitations:
   - Analysis limited to {time period} data
   - Geographic coverage: {coverage description}
   - Model assumes {key assumptions}
   - Prediction accuracy varies by {factor}

4. Recommended Use Cases:
   ✅ Policy planning and resource allocation
   ✅ Academic research and education
   ✅ Aggregate trend analysis
   ❌ Individual-level decisions
   ❌ Discriminatory practices
   ❌ High-stakes automated decisions without human review

5. Data Quality Notes:
   - {Data quality consideration 1}
   - {Data quality consideration 2}
   - See API documentation for known limitations

For questions or concerns about responsible use, contact:
ethics@quipuanalytics.org
"""

print("\n⚠️  RESPONSIBLE USE NOTICE")
print("="*80)
print("This analysis is for {intended use cases}.")
print("Results should be interpreted with consideration of limitations.")
print("See cell above for complete ethical considerations.")
print("="*80)
```

---

### **10. Output Requirements**

**Final cell structure:**

```python
# ═══════════════════════════════════════════════════════════════════════════
# 11. EXPORT & REPRODUCIBILITY
# ═══════════════════════════════════════════════════════════════════════════

# Export results for downstream analysis
output_dir = Path.cwd().parent.parent / 'outputs' / '{tier}_{domain}_{date}'
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Model artifacts
import joblib
joblib.dump(best_model, output_dir / 'model.pkl')

# 2. Results data
df_results.to_csv(output_dir / 'results.csv', index=False)
df_results.to_parquet(output_dir / 'results.parquet')

# 3. Visualizations
for i, chart in enumerate(charts, 1):
    chart.write_html(output_dir / f'chart_{i}.html')
    chart.write_image(output_dir / f'chart_{i}.png', width=1200, height=800)

# 4. Execution summary
with open(output_dir / 'execution_summary.json', 'w') as f:
    json.dump(execution_summary, f, indent=2)

# 5. Reproducibility package
reproducibility_info = {
    "notebook": "{TierX_NotebookName.ipynb}",
    "version": "v1.0",
    "python_version": platform.python_version(),
    "packages": {
        "pandas": pd.__version__,
        "scikit-learn": sklearn.__version__,
        # ... include all package versions
    },
    "random_seed": 42,
    "data_source": {
        "api": "{API Name}",
        "series_ids": ["{SERIES_ID_1}"],
        "date_range": "{start_date} to {end_date}"
    },
    "model_hyperparameters": best_model.get_params()
}

with open(output_dir / 'reproducibility.json', 'w') as f:
    json.dump(reproducibility_info, f, indent=2)

print(f"\n✅ All outputs saved to: {output_dir}")
print(f"\n📦 Reproducibility package includes:")
print(f"   - Trained model (model.pkl)")
print(f"   - Results data (results.csv, results.parquet)")
print(f"   - Visualizations (chart_*.html, chart_*.png)")
print(f"   - Execution summary (execution_summary.json)")
print(f"   - Reproducibility info (reproducibility.json)")
```

---

### **Template Reference Notebook**

**For complete implementation example, see:**
- **Reference:** `notebooks/tier1_descriptive/Tier1_Correlation.ipynb`
- **Status:** Production-ready template
- **Use Case:** Copy structure for new notebooks

---

### **Quality Checklist**

Before submitting any notebook, verify:

- [ ] Header with complete metadata (author, version, UUID, domain)
- [ ] Citation block (framework + notebook-specific)
- [ ] Prerequisites and next steps documented
- [ ] Execution tracking initialized (`setup_notebook_tracking()`)
- [ ] API keys loaded from environment/config (NO hardcoding)
- [ ] Data source aligned with Analytics Model Matrix
- [ ] Minimum 3 models compared (Tier 2+)
- [ ] PlotlyVisualizationEngine used for all charts
- [ ] Business insights section included
- [ ] Intelligent sampling strategy applied
- [ ] Registered in `config/notebook_registry.json`
- [ ] Execution summary and provenance logged
- [ ] Responsible use section included
- [ ] Output files exported (model, results, charts, metadata)
- [ ] Reproducibility package complete
- [ ] All cells execute without errors
- [ ] Runtime < 10 minutes (or documented if longer)

---

**This directive ensures every notebook is:**
- ✅ Enterprise-grade (production-ready code quality)
- ✅ Academically rigorous (proper citations and provenance)
- ✅ Reproducible (complete execution metadata)
- ✅ Secure (environment-based API key management)
- ✅ Integrated (cross-referenced with ecosystem)
- ✅ Ethical (responsible use considerations)
- ✅ Aligned with Analytics Model Matrix (19 domains)

**Last Updated:** October 8, 2025
**Status:** Binding directive for all AI agents and contributors
