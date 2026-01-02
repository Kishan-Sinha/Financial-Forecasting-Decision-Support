# Financial Forecasting & Decision Support System - Complete Documentation

## Project Overview

This is a comprehensive financial forecasting system that implements ARIMA time series models for predicting financial metrics, combined with scenario analysis and decision support capabilities. The system uses real financial data from Plotly datasets and provides validation metrics (MAPE, RMSE) along with budget planning tools.

## System Architecture

### Core Components

1. **data_loader.py** - Data Management
   - `load_sample_data()`: Fetches time series data from Plotly's public datasets
   - `create_synthetic_data()`: Generates realistic synthetic financial data
   - `prepare_data()`: Handles missing values and outliers using IQR method
   - `get_train_test_split()`: Time-based data splitting for proper temporal validation

2. **forecast_model.py** - ARIMA Forecasting
   - `ARIMAForecaster` class: Encapsulates ARIMA model operations
   - `calculate_mape()`: Mean Absolute Percentage Error (accuracy metric)
   - `calculate_rmse()`: Root Mean Squared Error (error magnitude)
   - `validate_model()`: Comprehensive validation with multiple metrics
   - `auto_arima_order()`: Automatic parameter selection using AIC criterion

3. **scenario_analysis.py** - What-If Analysis
   - `ScenarioAnalysis` class: Creates and compares scenarios
   - Optimistic scenario: Growth-based projections (+15% default)
   - Pessimistic scenario: Decline-based projections (-15% default)
   - Custom scenarios: User-defined multipliers
   - `perform_sensitivity_analysis()`: Impact analysis of factors
   - `calculate_budget_plan()`: Budget allocation based on forecasts

4. **main.py** - Workflow Integration
   - Complete execution pipeline
   - Data loading and preparation
   - Model training and forecasting
   - Scenario analysis
   - Budget planning and reporting

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/Kishan-Sinha/Financial-Forecasting-Decision-Support.git
cd Financial-Forecasting-Decision-Support

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the system
python main.py
```

## Dependencies

- **pandas** (>=1.3.0): Data manipulation and analysis
- **numpy** (>=1.21.0): Numerical computations
- **scipy** (>=1.7.0): Scientific functions
- **scikit-learn** (>=0.24.0): Machine learning utilities
- **statsmodels** (>=0.13.0): ARIMA implementation
- **matplotlib** (>=3.4.0): Data visualization
- **seaborn** (>=0.11.0): Statistical visualization
- **openpyxl** (>=3.6.0): Excel file handling

## Usage Guide

### Basic Usage

```python
from data_loader import load_sample_data, prepare_data, get_train_test_split
from forecast_model import ARIMAForecaster, validate_model
from scenario_analysis import ScenarioAnalysis

# Load and prepare data
df = load_sample_data()
df = prepare_data(df, target_column='Sales')
train_df, test_df = get_train_test_split(df, test_size=0.2)

# Train model
forecaster = ARIMAForecaster(order=(1, 1, 1))
forecaster.fit(train_df['Sales'].values)

# Generate forecast
forecast_df = forecaster.forecast(steps=30)
print(forecast_df)

# Scenario analysis
scenario = ScenarioAnalysis(forecast_df['mean'].values)
scenario.add_optimistic_scenario(growth_rate=0.15)
scenario.add_pessimistic_scenario(decline_rate=0.15)
print(scenario.get_scenario_comparison())
```

### Running the Complete System

```bash
python main.py
```

This will execute the entire workflow:
1. Load financial data
2. Prepare and validate data
3. Train ARIMA model
4. Generate 30-period forecast
5. Validate model performance
6. Create scenarios (Base, Optimistic, Pessimistic)
7. Generate budget allocation plan
8. Produce summary report

## Key Features

### 1. Time Series Forecasting
- ARIMA (AutoRegressive Integrated Moving Average) models
- Automatic parameter optimization
- Confidence intervals in forecasts
- Multiple validation metrics

### 2. Model Validation Metrics

**MAE (Mean Absolute Error)**
- Average absolute difference between actual and predicted values
- Same units as the data
- Formula: MAE = (1/n) × Σ|actual - predicted|

**RMSE (Root Mean Squared Error)**
- Penalizes larger errors more heavily
- Formula: RMSE = √((1/n) × Σ(actual - predicted)²)

**MAPE (Mean Absolute Percentage Error)**
- Percentage-based error metric
- Formula: MAPE = (1/n) × Σ(|actual - predicted| / |actual|) × 100%
- Interpretation: Lower is better (< 10% is excellent)

**Accuracy Score**
- Derived from MAPE: Accuracy = 100% - MAPE
- Capped at 100% for interpretability

### 3. Scenario Analysis

The system supports three types of scenarios:

**Base Case**: Original forecast values

**Optimistic Scenario**: 
- 15% growth rate by default
- For positive business environment
- Helps identify upside opportunities

**Pessimistic Scenario**:
- 15% decline by default
- For challenging business environment
- Helps prepare risk mitigation strategies

### 4. Budget Planning

Automatic budget allocation based on forecasts:
- Operations: 40% of total forecast
- Marketing: 25% of total forecast
- R&D: 20% of total forecast
- Administration: 15% of total forecast

Calculates:
- Total budget allocation per department
- Budget per period (period = month or quarter)
- Percentage allocation

## Data Sources

### Primary Data Source: Plotly Datasets
URL: https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv

**Data Characteristics:**
- Time series format with daily observations
- Multiple time series columns (A, B, C, D, E, F, G)
- Date range: 2008-2020+
- Real financial/market data

### Fallback: Synthetic Data
If external data fails to load, the system generates synthetic data with:
- Trend component (increasing over time)
- Seasonality component (regular patterns)
- Random noise (realistic variability)
- 365-day historical data
- 3 metrics: Sales, Cost, Revenue

## Model Parameters

### ARIMA Parameters (p, d, q)

**p (AR order)**: Number of autoregressive terms
- Default: 1
- Range: 0-5

**d (Differencing)**: Number of differences to make series stationary
- Default: 1
- Typical range: 0-2

**q (MA order)**: Number of moving average terms
- Default: 1
- Range: 0-5

### Forecast Periods
- Default: 30 periods
- Configurable in forecast() method
- Includes confidence intervals

## Output Files and Reports

### Console Output
The system prints a detailed report including:
1. Data loading status
2. Data preparation summary
3. Train/test split information
4. Model training results
5. Forecast for 30 periods
6. Validation metrics
7. Scenario comparison table
8. Budget allocation plan
9. Summary statistics

### Return Values (from main.py)
```python
forecast, metrics, scenario, budget = main()
```
- **forecast**: Array of 30 forecasted values
- **metrics**: Dictionary with MAE, RMSE, MAPE, Accuracy
- **scenario**: ScenarioAnalysis object with all scenarios
- **budget**: DataFrame with budget allocations

## Advanced Usage

### Custom ARIMA Order
```python
forecaster = ARIMAForecaster(order=(2, 1, 2))
forecaster.fit(train_data)
```

### Custom Scenarios
```python
scenario = ScenarioAnalysis(forecast_values)
scenario.add_custom_scenario(multiplier=1.25, name='Best Case')
scenario.add_custom_scenario(multiplier=0.75, name='Worst Case')
```

### Sensitivity Analysis
```python
from scenario_analysis import perform_sensitivity_analysis

impact_factors = {
    'Interest Rate': 5,
    'Market Growth': 10,
    'Competition': -8
}

sensitivity = perform_sensitivity_analysis(forecast_values, impact_factors)
print(sensitivity)
```

## Performance Considerations

- **Data Size**: Handles 1000+ observations efficiently
- **Execution Time**: ~5-10 seconds for full workflow
- **Memory**: < 500MB for typical datasets
- **Scalability**: Linear time complexity

## Troubleshooting

### Issue: Data Loading Fails
**Solution**: System automatically falls back to synthetic data generation

### Issue: ARIMA Model Won't Converge
**Solution**: Try different (p, d, q) parameters or use auto_arima_order()

### Issue: High MAPE Score
**Possible Causes**:
- Data contains outliers
- Insufficient training data
- ARIMA order not optimal
- Non-stationary data

**Solutions**:
- Increase training data
- Use outlier removal in prepare_data()
- Run auto_arima_order()
- Apply differencing (increase d parameter)

## Future Enhancements

1. **Multiple Forecasting Models**
   - SARIMA (Seasonal ARIMA)
   - Exponential Smoothing
   - Prophet
   - Machine Learning models (LSTM, XGBoost)

2. **Interactive Dashboard**
   - Dash/Streamlit web interface
   - Real-time data updates
   - Custom scenario builder

3. **Export Capabilities**
   - PDF reports
   - Excel workbooks
   - JSON outputs

4. **Advanced Analytics**
   - Monte Carlo simulations
   - Risk analysis
   - Confidence interval visualization

## References

1. Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: forecasting and control.
2. Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: principles and practice.
3. statsmodels documentation: https://www.statsmodels.org/

## License

MIT License - Feel free to use this in your projects

## Author

Kishan Sinha
https://github.com/Kishan-Sinha

## Contact & Support

For issues, questions, or suggestions, please open an issue on GitHub.
