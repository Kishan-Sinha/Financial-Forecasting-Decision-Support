"""Data loader module for fetching and preparing financial data."""
import pandas as pd
import numpy as np
from datetime import datetime

def load_sample_data():
    """
    Load sample financial time series data.
    Downloads from Plotly's public datasets.
    Returns: DataFrame with Date and financial metrics
    """
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv'
    try:
        df = pd.read_csv(url)
        df['Date'] = pd.to_datetime(df['Date'])
        return df.sort_values('Date').reset_index(drop=True)
    except Exception as e:
        print(f"Error loading data: {e}")
        return create_synthetic_data()

def create_synthetic_data(n_periods=365):
    """
    Create synthetic financial data for testing.
    Generates realistic time series with trend and seasonality.
    """
    dates = pd.date_range(start='2022-01-01', periods=n_periods, freq='D')
    np.random.seed(42)
    
    # Create synthetic sales data with trend and seasonality
    trend = np.linspace(100000, 150000, n_periods)
    seasonality = 20000 * np.sin(np.linspace(0, 4*np.pi, n_periods))
    noise = np.random.normal(0, 5000, n_periods)
    
    sales = trend + seasonality + noise
    
    df = pd.DataFrame({
        'Date': dates,
        'Sales': sales,
        'Cost': sales * 0.6 + np.random.normal(0, 2000, n_periods),
        'Revenue': sales * 1.5
    })
    
    return df

def prepare_data(df, target_column='Sales'):
    """
    Prepare data for time series analysis.
    Handles missing values and removes outliers.
    """
    df = df.copy()
    
    # Handle missing values
    df[target_column] = df[target_column].fillna(df[target_column].mean())
    
    # Remove outliers using IQR method
    Q1 = df[target_column].quantile(0.25)
    Q3 = df[target_column].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[target_column] >= Q1 - 1.5*IQR) & (df[target_column] <= Q3 + 1.5*IQR)]
    
    return df.reset_index(drop=True)

def get_train_test_split(df, test_size=0.2):
    """
    Split data into training and testing sets.
    Uses time-based split to maintain temporal order.
    """
    split_point = int(len(df) * (1 - test_size))
    train = df.iloc[:split_point].copy()
    test = df.iloc[split_point:].copy()
    return train, test
