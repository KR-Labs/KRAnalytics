# FRED API Key - Quick Setup Guide

##  Current Issue
Your dashboard is running with **sample data** because the FRED API key in your config file is not valid:
- **Found:** `eccedeaedf` (14 characters)
- **Required:** 32-character alphanumeric lowercase string

---

##  How to Get a Valid FRED API Key (5 minutes)

### Step 1: Sign Up
Visit: **https://fredaccount.stlouisfed.org/login/secure/**

1. Click "Sign Up" (top right)
2. Fill in:
   - Email address
   - Password
   - First/Last name
3. Click "Create Account"
4. Check your email and verify account

### Step 2: Generate API Key
1. Log in to your account
2. Visit: **https://fredaccount.stlouisfed.org/apikeys**
3. Click "Request API Key"
4. Enter:
   - **Key Description:** "QRL Unified Dashboard"
   - **Purpose:** "Economic analytics dashboard"
5. Click "Request API Key"
6. Copy the 32-character key (looks like: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)

### Step 3: Update Your Dashboard
```bash
# Option A: Set environment variable (temporary - this session only)
export FRED_API_KEY="your_32_character_key_here"

# Option B: Add to your shell profile (permanent)
echo 'export FRED_API_KEY="your_32_character_key_here"' >> ~/.zshrc
source ~/.zshrc

# Option C: Create .env file in QRL directory
cd /Users/bcdelo/Documents/GitHub/QRL
echo 'FRED_API_KEY=your_32_character_key_here' > .env
```

### Step 4: Restart Dashboard
```bash
# Kill current process
kill 56212

# Restart with new key
cd /Users/bcdelo/Documents/GitHub/QRL
FRED_API_KEY="your_32_character_key_here" nohup python3 khipu/dashboards/unified_dashboard_v2.py > /tmp/unified_dashboard_v2.log 2>&1 &

# Verify it loaded
sleep 5
tail -50 /tmp/unified_dashboard_v2.log | grep " Loaded"
```

**Expected Output:**
```
 Loaded 9 national indicators from FRED
   GDP per Capita: 215 observations
   Median Household Income: 34 observations
   Poverty Rate: 34 observations
   Unemployment Rate: 840 observations
   Labor Force Participation Rate: 840 observations
   Income Inequality (Gini): 56 observations
   Personal Income: 840 observations
   Personal Consumption Expenditures per Capita: 840 observations
   Homeownership Rate: 108 observations
```

---

##  What You'll Get with Valid API Key

### Real-Time National Indicators (9 from FRED)
1. **GDP per Capita** - Real economic output per person (1947-present)
2. **Median Household Income** - Central household earnings (1984-present)
3. **Poverty Rate** - Below-poverty-threshold population (1959-present)
4. **Unemployment Rate** - Monthly labor market indicator (1948-present)
5. **Labor Force Participation** - Active workforce percentage (1948-present)
6. **Gini Coefficient** - Income inequality measure (1967-present)
7. **Personal Income** - Total income from all sources (1959-present)
8. **Consumption per Capita** - Purchasing power indicator (1959-present)
9. **Homeownership Rate** - Household wealth proxy (1965-present)

### Plus 1 from OmniEcon Database
10. **Taxable Income Distribution** - IRS SOI data (already in your database)

### Data Benefits
-  **Historical depth:** Back to 1947 for some series
-  **Multiple frequencies:** Monthly, quarterly, annual
-  **Official sources:** BEA, BLS, Census Bureau
-  **Auto-updated:** FRED updates as agencies release new data
-  **Cached locally:** 24-hour cache (reduce API calls)

---

##  API Key Best Practices

### Security
-  **Never commit to Git:** Add to `.gitignore`
-  **Use environment variables:** Keep separate from code
-  **Rotate periodically:** Generate new key every 6-12 months
-  **Don't share:** Each user should have their own key

### Rate Limits (FRED API)
- **Limit:** 120 requests/minute (generous for dashboard use)
- **Dashboard usage:** ~10 requests at startup (then cached)
- **Cache strategy:** 24-hour TTL reduces API calls to 1x per day
- **No cost:** FRED API is completely free

---

##  Testing Your Setup

### Verify API Key Works
```bash
# Test FRED API directly
python3 << 'EOF'
from fredapi import Fred
fred = Fred(api_key='your_32_character_key_here')
data = fred.get_series('UNRATE')
print(f" API key works! Latest unemployment rate: {data.iloc[-1]:.1f}%")
EOF
```

### Check Dashboard Logs
```bash
# Should see successful loads
tail -100 /tmp/unified_dashboard_v2.log | grep -A 1 "Loading national"

# Expected:
#  Loading national indicators from FRED API...
#    GDP per Capita: 215 observations
#    Median Household Income: 34 observations
#   ... (7 more)
```

### Access Dashboard
1. Open: http://localhost:8050
2. Look at sidebar dropdowns
3. Should see all 10 indicators with real data
4. Select "GDP per Capita" → Should show chart with actual BEA data

---

##  Troubleshooting

### Error: "Bad Request. The value for variable api_key..."
**Cause:** API key is not 32 characters or contains invalid characters
**Solution:** Double-check you copied the entire key from FRED website

### Error: "Unauthorized. Your account has exceeded the API rate limit."
**Cause:** More than 120 requests per minute
**Solution:** Wait 60 seconds, restart dashboard (cache will prevent repeated calls)

### Error: "Series not found"
**Cause:** FRED series ID is incorrect or deprecated
**Solution:** Verify series IDs at https://fred.stlouisfed.org/

### Dashboard shows sample data despite valid key
**Cause:** Key not passed to dashboard process
**Solution:**
```bash
# Verify environment variable is set
echo $FRED_API_KEY

# If empty, set it and restart
export FRED_API_KEY="your_key"
kill $(ps aux | grep unified_dashboard_v2 | grep -v grep | awk '{print $2}')
cd /Users/bcdelo/Documents/GitHub/QRL
nohup python3 khipu/dashboards/unified_dashboard_v2.py > /tmp/unified_dashboard_v2.log 2>&1 &
```

---

##  FRED API Documentation

### Official Resources
- **Main Docs:** https://fred.stlouisfed.org/docs/api/
- **API Keys:** https://fredaccount.stlouisfed.org/apikeys
- **Series Search:** https://fred.stlouisfed.org/
- **Python Library:** https://github.com/mortada/fredapi

### Useful FRED Endpoints
- **Get Series Data:** `fred.get_series('SERIES_ID')`
- **Get Series Info:** `fred.get_series_info('SERIES_ID')`
- **Search Series:** `fred.search('keyword')`
- **Latest Observation:** `fred.get_series_latest_release('SERIES_ID')`

### Finding New Series
1. Go to https://fred.stlouisfed.org/
2. Search for indicator (e.g., "inflation rate")
3. Click on series you want
4. Copy series ID from URL (e.g., `CPIAUCSL`)
5. Add to `NATIONAL_INDICATORS` list in `unified_dashboard_v2.py`

---

##  Quick Commands Reference

```bash
# Get your FRED API key status
env | grep FRED

# Test API key
python3 -c "from fredapi import Fred; fred = Fred(api_key='YOUR_KEY'); print(fred.get_series('UNRATE').tail())"

# Restart dashboard with key
export FRED_API_KEY="YOUR_KEY"
kill $(ps aux | grep unified_dashboard_v2 | grep -v grep | awk '{print $2}')
cd /Users/bcdelo/Documents/GitHub/QRL
nohup python3 khipu/dashboards/unified_dashboard_v2.py > /tmp/unified_dashboard_v2.log 2>&1 &

# Check dashboard loaded FRED data
sleep 5
tail -50 /tmp/unified_dashboard_v2.log | grep " Loaded"

# Access dashboard
open http://localhost:8050
```

---

##  Final Checklist

Before considering setup complete:

- [ ] FRED account created and verified
- [ ] API key generated (32 characters)
- [ ] Environment variable set: `export FRED_API_KEY="..."`
- [ ] Dashboard restarted with new key
- [ ] Logs show " Loaded 9 national indicators from FRED"
- [ ] Dashboard accessible at http://localhost:8050
- [ ] Dropdowns show 10 national indicators
- [ ] Charts display real data (not sample)
- [ ] Data cached successfully (check logs for cache hits)

---

**Once completed, your dashboard will have real-time access to 9 official economic indicators from the Federal Reserve!**

**Questions?** Check the full documentation: `/Users/bcdelo/Documents/GitHub/QRL/docs/UNIFIED_DASHBOARD_V2_RELEASE.md`
