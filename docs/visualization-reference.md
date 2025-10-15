# Visualization Reference Guide

This guide provides comprehensive documentation for creating high-impact, publication-ready visualizations using KRAnalytics.

## 🎨 Overview

KRAnalytics uses Plotly as its primary visualization engine, providing interactive, web-ready charts optimized for socioeconomic data analysis.

## 📊 Chart Types by Analysis Domain

### Income & Poverty Analysis
- **Choropleth Maps**: Geographic income distribution
- **Box Plots**: Income distribution by demographics
- **Scatter Plots**: Income vs. other socioeconomic factors
- **Histograms**: Income distribution analysis

### Employment & Labor Markets
- **Time Series**: Employment trends over time
- **Bar Charts**: Employment by industry/occupation
- **Heatmaps**: Employment patterns by geography and time
- **Sankey Diagrams**: Job flow analysis

### Inequality & Distribution
- **Lorenz Curves**: Income inequality visualization
- **Violin Plots**: Distribution comparison across groups
- **Area Charts**: Cumulative distribution functions

### Environmental & Health
- **Risk Maps**: Environmental burden visualization
- **Bubble Maps**: Multi-dimensional risk factors
- **Correlation Heatmaps**: Risk factor relationships

## 🚀 Quick Start Examples

### Basic Choropleth Map

```python
import plotly.express as px
import pandas as pd

# Create state-level income map
fig = px.choropleth(
    df,
    locations='state_code',
    color='median_income',
    hover_name='state_name',
    locationmode='USA-states',
    scope='usa',
    title='Median Household Income by State',
    color_continuous_scale='Viridis'
)

fig.show()
```

### Interactive Time Series

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['date'],
    y=df['unemployment_rate'],
    mode='lines+markers',
    name='Unemployment Rate',
    line=dict(color='red', width=2)
))

fig.update_layout(
    title='US Unemployment Rate Over Time',
    xaxis_title='Date',
    yaxis_title='Unemployment Rate (%)',
    hovermode='x unified'
)

fig.show()
```

### Multi-Dimensional Scatter Plot

```python
fig = px.scatter(
    df,
    x='median_income',
    y='poverty_rate',
    size='population',
    color='education_level',
    hover_name='county_name',
    title='Income vs Poverty Rate by County',
    labels={
        'median_income': 'Median Household Income ($)',
        'poverty_rate': 'Poverty Rate (%)'
    }
)

fig.show()
```

## 🎨 Design Best Practices

### Color Schemes

**Categorical Data:**
- Use qualitative color scales: `'Set3'`, `'Pastel'`, `'Dark2'`
- Limit to 8-10 categories for clarity

**Sequential Data:**
- Use sequential scales: `'Viridis'`, `'Blues'`, `'Plasma'`
- Good for continuous variables like income, population

**Diverging Data:**
- Use diverging scales: `'RdBu'`, `'RdYlBu'`, `'Spectral'`
- Good for data with meaningful center point

### Layout Guidelines

```python
# Standard layout configuration
fig.update_layout(
    title={
        'text': 'Your Title Here',
        'x': 0.5,  # Center the title
        'font': {'size': 16}
    },
    font={'family': 'Arial, sans-serif'},
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=60, r=60, t=80, b=60)
)
```

### Accessibility

1. **Color-blind friendly palettes**:
   ```python
   # Use colorbrewer scales
   color_scale = ['#d73027', '#f46d43', '#fdae61', '#fee08b', 
                  '#e6f598', '#abdda4', '#66c2a5', '#3288bd']
   ```

2. **Clear axis labels and units**:
   ```python
   fig.update_xaxes(title_text='Median Household Income (USD)')
   fig.update_yaxes(title_text='Poverty Rate (%)')
   ```

3. **Meaningful hover information**:
   ```python
   fig.update_traces(
       hovertemplate='<b>%{hovertext}</b><br>' +
                    'Income: $%{x:,.0f}<br>' +
                    'Poverty Rate: %{y:.1f}%<extra></extra>'
   )
   ```

## 📈 Advanced Visualizations

### Lorenz Curve for Inequality

```python
def create_lorenz_curve(income_data):
    """Create Lorenz curve for income inequality visualization"""
    # Sort income data
    sorted_income = np.sort(income_data)
    n = len(sorted_income)
    
    # Calculate cumulative percentages
    cumulative_income = np.cumsum(sorted_income)
    cumulative_income_pct = cumulative_income / cumulative_income[-1]
    population_pct = np.arange(1, n + 1) / n
    
    # Create figure
    fig = go.Figure()
    
    # Add Lorenz curve
    fig.add_trace(go.Scatter(
        x=population_pct,
        y=cumulative_income_pct,
        mode='lines',
        name='Lorenz Curve',
        line=dict(color='blue', width=3)
    ))
    
    # Add line of equality
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='lines',
        name='Perfect Equality',
        line=dict(color='red', dash='dash', width=2)
    ))
    
    fig.update_layout(
        title='Income Inequality - Lorenz Curve',
        xaxis_title='Cumulative Population Share',
        yaxis_title='Cumulative Income Share',
        showlegend=True
    )
    
    return fig
```

### Multi-Panel Dashboard

```python
from plotly.subplots import make_subplots

# Create 2x2 subplot dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Income Distribution', 'Poverty by State', 
                   'Employment Trends', 'Education Levels'),
    specs=[[{'type': 'histogram'}, {'type': 'geo'}],
           [{'type': 'scatter'}, {'type': 'bar'}]]
)

# Add plots to subplots
fig.add_trace(
    go.Histogram(x=df['income'], name='Income'),
    row=1, col=1
)

fig.add_trace(
    go.Choropleth(
        locations=df['state_code'],
        z=df['poverty_rate'],
        locationmode='USA-states'
    ),
    row=1, col=2
)

# Update layout
fig.update_layout(
    height=800,
    title_text='Socioeconomic Dashboard',
    showlegend=False
)

fig.show()
```

## 🗺️ Geographic Visualizations

### County-Level Choropleth

```python
# Load county FIPS data
import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig = px.choropleth(
    df,
    geojson=counties,
    locations='fips',
    color='unemployment_rate',
    hover_name='county_name',
    hover_data=['state_name'],
    scope='usa',
    title='County-Level Unemployment Rate',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()
```

### Bubble Map with Multiple Variables

```python
fig = px.scatter_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    size='population',
    color='median_income',
    hover_name='city_name',
    hover_data=['state_name', 'poverty_rate'],
    size_max=50,
    zoom=3,
    mapbox_style='open-street-map',
    title='US Cities: Population vs Income'
)

fig.show()
```

## 📊 Statistical Visualizations

### Box Plot with Statistical Annotations

```python
fig = px.box(
    df,
    x='region',
    y='income',
    title='Income Distribution by Region'
)

# Add mean markers
fig.add_trace(go.Scatter(
    x=df.groupby('region')['income'].mean().index,
    y=df.groupby('region')['income'].mean().values,
    mode='markers',
    marker=dict(color='red', size=8, symbol='diamond'),
    name='Mean'
))

fig.show()
```

### Correlation Heatmap

```python
# Calculate correlation matrix
corr_matrix = df[numeric_columns].corr()

fig = px.imshow(
    corr_matrix,
    title='Socioeconomic Variables Correlation Matrix',
    color_continuous_scale='RdBu',
    aspect='auto'
)

# Add correlation values as text
fig.update_traces(
    text=np.round(corr_matrix, 2),
    texttemplate='%{text}',
    textfont={'size': 10}
)

fig.show()
```

## 💾 Exporting and Sharing

### Save as Static Images

```python
# Save as PNG (requires kaleido)
fig.write_image('income_analysis.png', width=1200, height=800, scale=2)

# Save as PDF
fig.write_image('income_analysis.pdf')

# Save as SVG (vector format)
fig.write_image('income_analysis.svg')
```

### Export Interactive HTML

```python
# Save as interactive HTML
fig.write_html('income_dashboard.html')

# Embed in Jupyter with custom config
fig.show(config={'displayModeBar': False, 'staticPlot': False})
```

### Create Presentation-Ready Plots

```python
# Configure for presentations
fig.update_layout(
    font={'size': 14, 'family': 'Arial'},
    title={'font': {'size': 18}},
    width=1920,
    height=1080,
    margin=dict(l=100, r=100, t=100, b=100)
)
```

## 🔧 Performance Optimization

### Large Dataset Handling

```python
# Sample data for interactive exploration
if len(df) > 10000:
    df_sample = df.sample(n=5000, random_state=42)
    print(f"Sampling {len(df_sample):,} points from {len(df):,} total")
else:
    df_sample = df

# Use datashader for very large datasets
import datashader as ds
import datashader.transfer_functions as tf
```

### Reduce File Size

```python
# Optimize for web sharing
fig.update_layout(
    template='simple_white',  # Simpler template
    showlegend=False if len(traces) > 10 else True
)

# Remove unnecessary hover data
fig.update_traces(hovertemplate='<b>%{hovertext}</b><extra></extra>')
```

## 📚 Resources

- [Plotly Documentation](https://plotly.com/python/)
- [ColorBrewer Palettes](https://colorbrewer2.org/)
- [Data Visualization Best Practices](https://www.tableau.com/learn/articles/data-visualization)

---

**Last Updated:** October 14, 2025  
**Version:** v1.0.0