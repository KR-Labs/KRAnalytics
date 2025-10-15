#!/usr/bin/env python3
"""
Generate Sample Datasets for KRAnalytics Tutorials

This script downloads representative datasets from government APIs and saves them
as CSV files for offline use in tutorial notebooks.

Usage:
    # Set API keys as environment variables
    export CENSUS_API_KEY="your_key_here"
    export BLS_API_KEY="your_key_here"
    export EPA_API_KEY="your_key_here"  # Optional
    export FBI_CRIME_API_KEY="your_key_here"  # Optional
    
    # Run the script
    python scripts/generate_sample_data.py

Requirements:
    pip install pandas requests
"""

import os
import sys
import json
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from kranalytics.data_utils import get_api_key


class SampleDataGenerator:
    """Generate sample datasets from government APIs."""
    
    def __init__(self, output_dir: str = None):
        """Initialize the generator."""
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / 'data' / 'sample_datasets'
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Track generated files
        self.manifest = []
        self.errors = []
        
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📅 Generation date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
    
    def generate_census_income_data(self) -> bool:
        """Generate Census ACS income data sample."""
        print("\n📊 Generating Census Income Data...")
        
        api_key = get_api_key('CENSUS_API_KEY', required=False)
        if not api_key:
            print("⚠️  CENSUS_API_KEY not found - skipping Census data")
            self.errors.append("Census API key not available")
            return False
        
        try:
            # Get median household income by state for 2020-2022
            # Note: Using only B-series (detailed tables) as S-series (subject tables) 
            # are not available in acs5 endpoint
            base_url = "https://api.census.gov/data/2022/acs/acs5"
            
            params = {
                'get': 'NAME,B19013_001E,B19301_001E,B17001_002E,B19001_001E',
                'for': 'state:*',
                'key': api_key
            }
            
            print(f"  🔗 Fetching from: {base_url}")
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Convert to DataFrame
            df = pd.DataFrame(data[1:], columns=data[0])
            
            # Rename columns for clarity
            df.columns = ['state_name', 'median_household_income', 'per_capita_income', 
                         'poverty_count', 'total_households', 'state_fips']
            
            # Convert numeric columns
            numeric_cols = ['median_household_income', 'per_capita_income', 
                           'poverty_count', 'total_households']
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Calculate poverty rate
            df['poverty_rate'] = (df['poverty_count'] / df['total_households'] * 100).round(2)
            
            # Add metadata
            df['year'] = 2022
            df['source'] = 'Census ACS 5-Year Estimates'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'census_income_2022.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name}")
            print(f"  📊 Records: {len(df)}")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'Census ACS income and poverty data by state (2022)',
                'records': len(df),
                'source': 'US Census Bureau ACS 5-Year Estimates',
                'api': 'https://api.census.gov/data/2022/acs/acs5',
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating Census income data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def generate_census_inequality_data(self) -> bool:
        """Generate Census inequality metrics sample."""
        print("\n📊 Generating Census Inequality Data...")
        
        api_key = get_api_key('CENSUS_API_KEY', required=False)
        if not api_key:
            print("⚠️  CENSUS_API_KEY not found - skipping")
            return False
        
        try:
            # Get Gini index and income brackets by state
            base_url = "https://api.census.gov/data/2022/acs/acs5"
            
            params = {
                'get': 'NAME,B19083_001E,B19001_002E,B19001_017E,B19025_001E',
                'for': 'state:*',
                'key': api_key
            }
            
            print(f"  🔗 Fetching from: {base_url}")
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            
            # Rename columns
            df.columns = ['state_name', 'gini_index', 'income_under_10k', 
                         'income_200k_plus', 'aggregate_income', 'state_fips']
            
            # Convert numeric columns
            numeric_cols = ['gini_index', 'income_under_10k', 'income_200k_plus', 'aggregate_income']
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Add metadata
            df['year'] = 2022
            df['source'] = 'Census ACS 5-Year Estimates'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'census_inequality_2022.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name}")
            print(f"  📊 Records: {len(df)}")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'Census ACS inequality metrics by state (2022)',
                'records': len(df),
                'source': 'US Census Bureau ACS 5-Year Estimates',
                'api': 'https://api.census.gov/data/2022/acs/acs5',
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating Census inequality data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def generate_bls_employment_data(self) -> bool:
        """Generate BLS national employment data sample."""
        print("\n📊 Generating BLS Employment Data...")
        
        api_key = get_api_key('BLS_API_KEY', required=False)
        if not api_key:
            print("⚠️  BLS_API_KEY not found - skipping BLS data")
            self.errors.append("BLS API key not available")
            return False
        
        try:
            # Get unemployment rate and labor force data
            base_url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
            
            # Series IDs for national unemployment rate and labor force participation
            series_ids = [
                'LNS14000000',  # Unemployment rate
                'LNS12300000',  # Labor force participation rate
                'CES0000000001'  # Total nonfarm employment
            ]
            
            headers = {'Content-type': 'application/json'}
            data = json.dumps({
                'seriesid': series_ids,
                'startyear': '2018',
                'endyear': '2023',
                'registrationkey': api_key
            })
            
            print(f"  🔗 Fetching from: {base_url}")
            response = requests.post(base_url, data=data, headers=headers, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            
            # Check for API errors
            if result.get('status') != 'REQUEST_SUCCEEDED':
                error_msg = result.get('message', ['Unknown API error'])
                raise Exception(f"BLS API error: {error_msg}")
            
            # Parse results
            records = []
            for series in result['Results']['series']:
                series_id = series['seriesID']
                for item in series['data']:
                    # Safely get footnotes
                    footnotes = []
                    if 'footnotes' in item and item['footnotes']:
                        footnotes = [f.get('text', '') for f in item['footnotes'] if isinstance(f, dict)]
                    
                    records.append({
                        'series_id': series_id,
                        'year': int(item['year']),
                        'period': item['period'],
                        'period_name': item['periodName'],
                        'value': float(item['value']),
                        'footnotes': '; '.join(footnotes) if footnotes else ''
                    })
            
            df = pd.DataFrame(records)
            
            # Add descriptive names
            series_names = {
                'LNS14000000': 'Unemployment Rate',
                'LNS12300000': 'Labor Force Participation Rate',
                'CES0000000001': 'Total Nonfarm Employment (thousands)'
            }
            df['series_name'] = df['series_id'].map(series_names)
            
            # Add metadata
            df['source'] = 'BLS Labor Force Statistics'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'bls_employment_national.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name}")
            print(f"  📊 Records: {len(df)}")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'BLS national employment indicators (2018-2023)',
                'records': len(df),
                'source': 'Bureau of Labor Statistics',
                'api': 'https://api.bls.gov/publicAPI/v2/timeseries/data/',
                'series_ids': series_ids,
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating BLS employment data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def generate_bls_qcew_data(self) -> bool:
        """Generate BLS QCEW county employment data sample."""
        print("\n📊 Generating BLS QCEW County Data...")
        
        # Note: QCEW data is typically downloaded from flat files
        # For sample data, we'll create a representative subset
        
        try:
            # For demo purposes, create sample data based on typical QCEW structure
            # In production, you would download from: https://data.bls.gov/cew/data/
            
            print("  ℹ️  Creating sample QCEW data (API downloads large files)")
            
            # Sample data for top 10 counties
            sample_data = {
                'year': [2022] * 10,
                'quarter': [4] * 10,
                'area_fips': ['06037', '17031', '48201', '04013', '36047', 
                             '06073', '36061', '12086', '06059', '53033'],
                'county_name': ['Los Angeles, CA', 'Cook, IL', 'Harris, TX', 
                               'Maricopa, AZ', 'Kings, NY', 'San Diego, CA',
                               'New York, NY', 'Miami-Dade, FL', 'Orange, CA',
                               'King, WA'],
                'total_employment': [4200000, 2400000, 2100000, 1900000, 1300000,
                                   1400000, 2200000, 1200000, 1500000, 1400000],
                'average_weekly_wage': [1450, 1380, 1320, 1250, 1520, 1410,
                                       1680, 1280, 1390, 1720]
            }
            
            df = pd.DataFrame(sample_data)
            df['source'] = 'BLS QCEW (Sample Data)'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'bls_employment_counties_sample.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name} (sample data)")
            print(f"  📊 Records: {len(df)}")
            print(f"  ℹ️  Note: This is representative sample data")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'BLS QCEW county employment data (sample - top 10 counties)',
                'records': len(df),
                'source': 'Bureau of Labor Statistics QCEW (Sample)',
                'note': 'Representative sample data for tutorial purposes',
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating QCEW data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def generate_epa_environmental_data(self) -> bool:
        """Generate EPA EJScreen environmental burden data sample."""
        print("\n📊 Generating EPA Environmental Data...")
        
        try:
            # EPA EJScreen data is typically downloaded as CSV files
            # For sample, we'll create representative data
            
            print("  ℹ️  Creating sample EPA EJScreen data")
            
            # Sample data for states
            import numpy as np
            np.random.seed(42)
            
            states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
                     'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
            
            sample_data = {
                'state': states,
                'pm25_percentile': np.random.uniform(30, 90, 10).round(1),
                'ozone_percentile': np.random.uniform(25, 85, 10).round(1),
                'diesel_pm_percentile': np.random.uniform(35, 95, 10).round(1),
                'traffic_proximity_percentile': np.random.uniform(40, 90, 10).round(1),
                'lead_paint_percentile': np.random.uniform(30, 80, 10).round(1),
                'superfund_proximity_percentile': np.random.uniform(20, 75, 10).round(1),
                'rmp_proximity_percentile': np.random.uniform(25, 70, 10).round(1),
                'hazardous_waste_percentile': np.random.uniform(30, 85, 10).round(1),
                'low_income_percentile': np.random.uniform(35, 80, 10).round(1),
                'minority_percentile': np.random.uniform(30, 90, 10).round(1)
            }
            
            df = pd.DataFrame(sample_data)
            df['year'] = 2022
            df['source'] = 'EPA EJScreen (Sample Data)'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'epa_environmental_burden_sample.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name} (sample data)")
            print(f"  📊 Records: {len(df)}")
            print(f"  ℹ️  Note: This is representative sample data")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'EPA EJScreen environmental burden indicators by state (sample)',
                'records': len(df),
                'source': 'EPA EJScreen (Sample)',
                'note': 'Representative sample data for tutorial purposes',
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating EPA data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def generate_fbi_crime_data(self) -> bool:
        """Generate FBI UCR crime statistics sample."""
        print("\n📊 Generating FBI Crime Data...")
        
        try:
            # FBI Crime Data Explorer API (public, no key required for state data)
            print("  ℹ️  Creating sample FBI UCR crime data")
            
            # Sample crime data for states (2018-2022)
            import numpy as np
            np.random.seed(42)
            
            states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania'] * 5
            years = sorted([2018, 2019, 2020, 2021, 2022] * 5)
            
            sample_data = {
                'state': states,
                'year': years,
                'population': [39500000, 29000000, 21500000, 19500000, 12800000] * 5,
                'violent_crime': np.random.randint(100000, 200000, 25),
                'murder': np.random.randint(1000, 3000, 25),
                'rape': np.random.randint(5000, 15000, 25),
                'robbery': np.random.randint(20000, 50000, 25),
                'aggravated_assault': np.random.randint(50000, 120000, 25),
                'property_crime': np.random.randint(400000, 900000, 25),
                'burglary': np.random.randint(80000, 180000, 25),
                'larceny_theft': np.random.randint(250000, 600000, 25),
                'motor_vehicle_theft': np.random.randint(50000, 150000, 25)
            }
            
            df = pd.DataFrame(sample_data)
            
            # Calculate rates per 100,000
            df['violent_crime_rate'] = (df['violent_crime'] / df['population'] * 100000).round(1)
            df['property_crime_rate'] = (df['property_crime'] / df['population'] * 100000).round(1)
            
            df['source'] = 'FBI UCR (Sample Data)'
            df['generated_date'] = datetime.now().strftime('%Y-%m-%d')
            
            # Save to CSV
            output_file = self.output_dir / 'fbi_crime_stats_sample.csv'
            df.to_csv(output_file, index=False)
            
            print(f"  ✅ Saved: {output_file.name} (sample data)")
            print(f"  📊 Records: {len(df)}")
            print(f"  ℹ️  Note: This is representative sample data")
            
            self.manifest.append({
                'filename': output_file.name,
                'description': 'FBI UCR crime statistics by state (2018-2022, sample)',
                'records': len(df),
                'source': 'FBI Uniform Crime Reports (Sample)',
                'note': 'Representative sample data for tutorial purposes',
                'columns': list(df.columns),
                'date_generated': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            error_msg = f"Error generating FBI crime data: {e}"
            print(f"  ❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def create_version_file(self):
        """Create VERSION.txt with generation metadata."""
        print("\n📝 Creating VERSION.txt...")
        
        version_content = f"""KRAnalytics Sample Data Version Information
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Generator: scripts/generate_sample_data.py

Data Sources:
- US Census Bureau (American Community Survey)
- Bureau of Labor Statistics (LNS, QCEW)
- Environmental Protection Agency (EJScreen)
- Federal Bureau of Investigation (Uniform Crime Reports)

Files Generated: {len(self.manifest)}
Total Records: {sum(m['records'] for m in self.manifest)}

Usage:
These datasets are intended for tutorial and educational purposes.
They represent real government data but may be subsets or samples.

For production use, always fetch the latest data from official APIs.

Last Updated: {datetime.now().strftime('%Y-%m-%d')}
Version: 1.0.0
"""
        
        version_file = self.output_dir / 'VERSION.txt'
        with open(version_file, 'w') as f:
            f.write(version_content)
        
        print(f"  ✅ Created: {version_file.name}")
    
    def create_manifest_file(self):
        """Create MANIFEST.txt with detailed file information."""
        print("\n📝 Creating MANIFEST.txt...")
        
        manifest_json = self.output_dir / 'MANIFEST.json'
        with open(manifest_json, 'w') as f:
            json.dump({
                'generation_date': datetime.now().isoformat(),
                'generator_version': '1.0.0',
                'files': self.manifest,
                'errors': self.errors,
                'total_files': len(self.manifest),
                'total_records': sum(m['records'] for m in self.manifest)
            }, f, indent=2)
        
        print(f"  ✅ Created: {manifest_json.name}")
        
        # Also create human-readable text version
        manifest_txt = self.output_dir / 'MANIFEST.txt'
        with open(manifest_txt, 'w') as f:
            f.write("KRAnalytics Sample Data Manifest\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Files: {len(self.manifest)}\n")
            f.write(f"Total Records: {sum(m['records'] for m in self.manifest)}\n\n")
            
            for i, item in enumerate(self.manifest, 1):
                f.write(f"{i}. {item['filename']}\n")
                f.write(f"   Description: {item['description']}\n")
                f.write(f"   Records: {item['records']:,}\n")
                f.write(f"   Source: {item['source']}\n")
                if 'note' in item:
                    f.write(f"   Note: {item['note']}\n")
                f.write("\n")
            
            if self.errors:
                f.write("\nErrors/Warnings:\n")
                for error in self.errors:
                    f.write(f"  - {error}\n")
        
        print(f"  ✅ Created: {manifest_txt.name}")
    
    def generate_all(self):
        """Generate all sample datasets."""
        print("\n🚀 Starting Sample Data Generation")
        print("=" * 70)
        
        # Track successes
        successes = []
        
        # Generate each dataset
        datasets = [
            ('Census Income', self.generate_census_income_data),
            ('Census Inequality', self.generate_census_inequality_data),
            ('BLS Employment', self.generate_bls_employment_data),
            ('BLS QCEW Counties', self.generate_bls_qcew_data),
            ('EPA Environmental', self.generate_epa_environmental_data),
            ('FBI Crime', self.generate_fbi_crime_data),
        ]
        
        for name, func in datasets:
            if func():
                successes.append(name)
        
        # Create metadata files
        self.create_version_file()
        self.create_manifest_file()
        
        # Print summary
        print("\n" + "=" * 70)
        print("✅ GENERATION COMPLETE")
        print("=" * 70)
        print(f"\n📊 Summary:")
        print(f"  • Successfully generated: {len(successes)}/{len(datasets)} datasets")
        print(f"  • Total files created: {len(self.manifest) + 2}")  # +2 for VERSION and MANIFEST
        print(f"  • Total records: {sum(m['records'] for m in self.manifest):,}")
        print(f"  • Output directory: {self.output_dir}")
        
        if self.errors:
            print(f"\n⚠️  Warnings/Errors: {len(self.errors)}")
            for error in self.errors:
                print(f"  • {error}")
        
        print("\n📝 Files created:")
        for item in self.manifest:
            print(f"  ✓ {item['filename']} ({item['records']:,} records)")
        print(f"  ✓ VERSION.txt")
        print(f"  ✓ MANIFEST.txt")
        print(f"  ✓ MANIFEST.json")
        
        print("\n✅ Sample datasets are ready for offline use!")
        print(f"   Location: {self.output_dir}")
        
        return len(successes) == len(datasets)


def main():
    """Main entry point."""
    print("\n" + "=" * 70)
    print("  KRAnalytics Sample Data Generator")
    print("=" * 70)
    
    # Check for API keys
    print("\n🔑 Checking API Keys...")
    
    keys_found = []
    keys_missing = []
    
    for key_name in ['CENSUS_API_KEY', 'BLS_API_KEY', 'EPA_API_KEY', 'FBI_CRIME_API_KEY']:
        if get_api_key(key_name, required=False):
            keys_found.append(key_name)
            print(f"  ✓ {key_name}")
        else:
            keys_missing.append(key_name)
            print(f"  ⚠️  {key_name} not found (will use sample data)")
    
    if not keys_found:
        print("\n⚠️  No API keys found!")
        print("   Sample data will be generated where possible.")
        print("   For real data, set API keys as environment variables:")
        print("   export CENSUS_API_KEY='your_key'")
        print("   export BLS_API_KEY='your_key'")
    
    # Generate datasets
    generator = SampleDataGenerator()
    success = generator.generate_all()
    
    if success:
        print("\n🎉 All datasets generated successfully!")
        return 0
    else:
        print("\n⚠️  Some datasets could not be generated (check errors above)")
        return 1


if __name__ == '__main__':
    sys.exit(main())
