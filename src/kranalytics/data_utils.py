"""
Data Loading Utilities for KRAnalytics

This module provides utilities for loading data in notebooks, with automatic
fallback to sample data when API keys are not available.

Author: Khipu Analytics Team
License: MIT
"""

import os
import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Any
import warnings


def get_data_dir() -> Path:
    """
    Get the path to the data directory.
    
    Returns:
        Path to the data/sample_datasets directory
    """
    # Try to find data directory relative to this file
    current_file = Path(__file__).resolve()
    repo_root = current_file.parent.parent.parent
    data_dir = repo_root / 'data' / 'sample_datasets'
    
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    
    return data_dir


def load_sample_data(dataset_name: str, fallback_message: bool = True) -> Optional[pd.DataFrame]:
    """
    Load sample data from the data/sample_datasets directory.
    
    Args:
        dataset_name: Name of the dataset (e.g., 'census_income', 'bls_employment')
        fallback_message: Whether to print a message about using sample data
        
    Returns:
        DataFrame with sample data, or None if not found
    """
    data_dir = get_data_dir()
    
    # Try different file extensions
    for ext in ['.csv', '.parquet', '.pkl', '.json']:
        filepath = data_dir / f"{dataset_name}{ext}"
        if filepath.exists():
            if fallback_message:
                print(f"📊 Loading sample data from: {filepath.name}")
                print(f"ℹ️  This is pre-downloaded data - no API key required!")
            
            # Load based on extension
            if ext == '.csv':
                return pd.read_csv(filepath)
            elif ext == '.parquet':
                return pd.read_parquet(filepath)
            elif ext == '.pkl':
                return pd.read_pickle(filepath)
            elif ext == '.json':
                return pd.read_json(filepath)
    
    return None


def get_api_key(api_name: str, required: bool = False) -> Optional[str]:
    """
    Load API key from environment variables.
    
    This is a simplified version that only checks environment variables,
    making it safe for public distribution without exposing credential paths.
    
    Args:
        api_name: Name of the API key environment variable
        required: Whether to raise an error if key not found
        
    Returns:
        API key string or None
        
    Raises:
        ValueError: If required=True and key not found
    """
    key = os.environ.get(api_name)
    
    if not key and required:
        raise ValueError(
            f"API key '{api_name}' not found in environment variables. "
            f"Either set the environment variable or use sample data."
        )
    
    return key


def load_data_with_fallback(
    api_loader_func,
    dataset_name: str,
    api_key_name: str,
    api_loader_kwargs: Optional[Dict[str, Any]] = None
) -> pd.DataFrame:
    """
    Load data from API with automatic fallback to sample data.
    
    This function tries to load data from an API first, and if that fails
    (either due to missing API key or API error), it falls back to sample data.
    
    Args:
        api_loader_func: Function to call to load data from API
        dataset_name: Name of the sample dataset to use as fallback
        api_key_name: Name of the API key environment variable
        api_loader_kwargs: Keyword arguments to pass to api_loader_func
        
    Returns:
        DataFrame with data (either from API or sample data)
        
    Example:
        >>> def load_from_census_api(api_key, year=2020):
        ...     # API loading logic here
        ...     pass
        >>> 
        >>> df = load_data_with_fallback(
        ...     api_loader_func=load_from_census_api,
        ...     dataset_name='census_income_2020',
        ...     api_key_name='CENSUS_API_KEY',
        ...     api_loader_kwargs={'year': 2020}
        ... )
    """
    if api_loader_kwargs is None:
        api_loader_kwargs = {}
    
    # Try to get API key
    api_key = get_api_key(api_key_name, required=False)
    
    if api_key:
        try:
            print(f"🔑 API key found for {api_key_name}")
            print(f"📡 Attempting to load data from API...")
            
            # Try to load from API
            df = api_loader_func(api_key=api_key, **api_loader_kwargs)
            
            if df is not None and len(df) > 0:
                print(f"✅ Successfully loaded {len(df):,} records from API")
                return df
            else:
                warnings.warn(f"API returned empty data, falling back to sample data")
        except Exception as e:
            warnings.warn(f"API loading failed: {e}. Falling back to sample data.")
    else:
        print(f"ℹ️  No API key found for {api_key_name}")
    
    # Fall back to sample data
    print(f"📊 Loading sample data instead...")
    df = load_sample_data(dataset_name, fallback_message=True)
    
    if df is None:
        raise FileNotFoundError(
            f"Sample data '{dataset_name}' not found in data/sample_datasets/. "
            f"Please either:\n"
            f"  1. Set the {api_key_name} environment variable to load from API, or\n"
            f"  2. Download the sample data files\n"
            f"\nSee the README for instructions on obtaining sample data."
        )
    
    return df


def save_sample_data(df: pd.DataFrame, dataset_name: str, format: str = 'csv') -> Path:
    """
    Save a DataFrame as sample data for future use.
    
    This is useful for creating sample datasets from API data.
    
    Args:
        df: DataFrame to save
        dataset_name: Name for the dataset
        format: File format ('csv', 'parquet', 'pkl', 'json')
        
    Returns:
        Path to the saved file
    """
    data_dir = get_data_dir()
    filepath = data_dir / f"{dataset_name}.{format}"
    
    if format == 'csv':
        df.to_csv(filepath, index=False)
    elif format == 'parquet':
        df.to_parquet(filepath, index=False)
    elif format == 'pkl':
        df.to_pickle(filepath)
    elif format == 'json':
        df.to_json(filepath, orient='records')
    else:
        raise ValueError(f"Unsupported format: {format}")
    
    print(f"✅ Saved sample data to: {filepath}")
    return filepath


# Example usage and documentation
if __name__ == "__main__":
    print("KRAnalytics Data Utilities")
    print("=" * 50)
    print(f"Data directory: {get_data_dir()}")
    print("\nExample usage in notebooks:")
    print("""
    from kranalytics.data_utils import load_data_with_fallback, load_sample_data
    
    # Option 1: Load with automatic fallback
    df = load_data_with_fallback(
        api_loader_func=load_census_data,
        dataset_name='census_income_2020',
        api_key_name='CENSUS_API_KEY',
        api_loader_kwargs={'year': 2020}
    )
    
    # Option 2: Load sample data directly (no API)
    df = load_sample_data('census_income_2020')
    """)
