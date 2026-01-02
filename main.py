"""Main execution script for financial forecasting system."""
import pandas as pd
import numpy as np
from data_loader import load_sample_data, create_synthetic_data, prepare_data, get_train_test_split
from forecast_model import ARIMAForecaster, validate_model
from scenario_analysis import ScenarioAnalysis, calculate_budget_plan

def main():
    """
    Main execution function combining all components.
    """
    print("="*60)
    print("Financial Forecasting & Decision Support System")
    print("="*60)
    
    # Step 1: Load and prepare data
    print("\n[1] Loading financial data...")
    try:
        df = load_sample_data()
        print(f"Successfully loaded {len(df)} records from Plotly datasets")
    except:
        print("Using synthetic data instead")
        df = create_synthetic_data()
    
    # Prepare data
    print("\n[2] Preparing data...")
    df = prepare_data(df, target_column='Sales' if 'Sales' in df.columns else df.columns[1])
    print(f"Data prepared with {len(df)} records")
    
    # Step 2: Split data
    print("\n[3] Splitting data into train/test sets...")
    train_df, test_df = get_train_test_split(df, test_size=0.2)
    print(f"Training set: {len(train_df)} records")
    print(f"Testing set: {len(test_df)} records")
    
    # Get target column
    target_col = 'Sales' if 'Sales' in df.columns else df.columns[1]
    train_data = train_df[target_col].values
    test_data = test_df[target_col].values
    
    # Step 3: Train ARIMA model
    print("\n[4] Training ARIMA forecasting model...")
    forecaster = ARIMAForecaster(order=(1, 1, 1))
    if forecaster.fit(train_data):
        print("ARIMA model trained successfully")
    else:
        print("Error training model")
        return
    
    # Step 4: Generate forecast
    print("\n[5] Generating forecast for next 30 periods...")
    forecast_df = forecaster.forecast(steps=30)
    forecast_values = forecast_df['mean'].values
    print(f"Forecast generated: {len(forecast_values)} periods")
    
    # Step 5: Validate on test set
    print("\n[6] Model validation on test data...")
    test_forecast = forecaster.fitted_model.fittedvalues[-len(test_data):]
    metrics = validate_model(test_data, test_forecast)
    
    print(f"\n  Validation Metrics:")
    print(f"  - MAE (Mean Absolute Error): {metrics['MAE']:.2f}")
    print(f"  - RMSE (Root Mean Squared Error): {metrics['RMSE']:.2f}")
    print(f"  - MAPE (Mean Absolute % Error): {metrics['MAPE']:.2f}%")
    print(f"  - Accuracy Score: {metrics['Accuracy']:.2f}%")
    
    # Step 6: Scenario analysis
    print("\n[7] Running scenario analysis...")
    scenario = ScenarioAnalysis(forecast_values, base_case_name='Base Case')
    scenario.add_optimistic_scenario(growth_rate=0.15, name='Optimistic (15% Growth)')
    scenario.add_pessimistic_scenario(decline_rate=0.15, name='Pessimistic (15% Decline)')
    
    print(f"\n  Scenario Comparison:")
    comparison = scenario.get_scenario_comparison()
    print(comparison)
    
    # Step 7: Budget planning
    print("\n[8] Creating budget allocation plan...")
    budget_allocation = {
        'Operations': 40,
        'Marketing': 25,
        'R&D': 20,
        'Administration': 15
    }
    budget_plan = calculate_budget_plan(forecast_values, budget_allocation)
    print(f"\n  Budget Plan:")
    print(budget_plan)
    
    # Step 8: Summary report
    print("\n[9] Summary Report")
    print("="*60)
    print(f"Total Forecast (30 periods): ${np.sum(forecast_values):,.2f}")
    print(f"Average Period Forecast: ${np.mean(forecast_values):,.2f}")
    print(f"Forecast Std Deviation: ${np.std(forecast_values):,.2f}")
    print(f"\nModel Accuracy: {metrics['Accuracy']:.2f}%")
    print(f"Forecast Range: ${np.min(forecast_values):,.2f} - ${np.max(forecast_values):,.2f}")
    print("="*60)
    
    print("\n[SUCCESS] Financial forecasting analysis completed!")
    print("\nFiles and outputs ready for decision support.")
    return forecast_values, metrics, scenario, budget_plan

if __name__ == "__main__":
    forecast, metrics, scenario, budget = main()
