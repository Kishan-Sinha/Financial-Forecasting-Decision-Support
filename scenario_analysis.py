"""Scenario analysis and what-if analysis for financial forecasting."""
import numpy as np
import pandas as pd

class ScenarioAnalysis:
    """Perform scenario-based analysis on forecasted data."""
    
    def __init__(self, forecast_values, base_case_name='Base Case'):
        """
        Initialize scenario analysis.
        forecast_values: array of forecasted values
        """
        self.forecast_values = forecast_values
        self.base_case_name = base_case_name
        self.scenarios = {base_case_name: forecast_values}
        
    def add_optimistic_scenario(self, growth_rate=0.15, name='Optimistic'):
        """
        Create optimistic scenario with positive growth.
        growth_rate: percentage increase (e.g., 0.15 for 15%)
        """
        optimistic = self.forecast_values * (1 + growth_rate)
        self.scenarios[name] = optimistic
        return optimistic
    
    def add_pessimistic_scenario(self, decline_rate=0.15, name='Pessimistic'):
        """
        Create pessimistic scenario with negative growth.
        decline_rate: percentage decrease (e.g., 0.15 for 15%)
        """
        pessimistic = self.forecast_values * (1 - decline_rate)
        self.scenarios[name] = pessimistic
        return pessimistic
    
    def add_custom_scenario(self, multiplier, name='Custom'):
        """
        Create custom scenario with specified multiplier.
        multiplier: factor to multiply forecast values
        """
        custom = self.forecast_values * multiplier
        self.scenarios[name] = custom
        return custom
    
    def get_scenario_comparison(self):
        """
        Return comparison of all scenarios.
        Returns: DataFrame with scenario statistics
        """
        comparison_data = {}
        for scenario_name, values in self.scenarios.items():
            comparison_data[scenario_name] = {
                'Min': np.min(values),
                'Max': np.max(values),
                'Mean': np.mean(values),
                'Std Dev': np.std(values),
                'Total': np.sum(values)
            }
        
        return pd.DataFrame(comparison_data).T
    
    def get_scenario_summary(self):
        """
        Get detailed summary of all scenarios.
        Returns: Dictionary with statistics per scenario
        """
        summary = {}
        for scenario_name, values in self.scenarios.items():
            summary[scenario_name] = {
                'count': len(values),
                'mean': float(np.mean(values)),
                'std': float(np.std(values)),
                'min': float(np.min(values)),
                '25%': float(np.percentile(values, 25)),
                'median': float(np.median(values)),
                '75%': float(np.percentile(values, 75)),
                'max': float(np.max(values))
            }
        return summary

def perform_sensitivity_analysis(base_values, impact_factors):
    """
    Analyze sensitivity of forecast to different factors.
    impact_factors: dict with factor names and impact percentages
    Returns: DataFrame showing impact of each factor
    """
    sensitivity_results = {}
    
    for factor_name, impact_pct in impact_factors.items():
        # Calculate impact of +1% change in factor
        impact_value = base_values * (impact_pct / 100)
        sensitivity_results[factor_name] = {
            'Impact on Forecast': impact_value,
            'Impact %': impact_pct,
            'Total Change': np.sum(impact_value)
        }
    
    return pd.DataFrame(sensitivity_results).T

def calculate_budget_plan(forecast_values, budget_allocation):
    """
    Create budget planning based on forecast.
    budget_allocation: dict with allocation percentages
    Returns: DataFrame with budget allocations
    """
    total_forecast = np.sum(forecast_values)
    budget_plan = {}
    
    for dept, allocation_pct in budget_allocation.items():
        budget_amount = total_forecast * (allocation_pct / 100)
        budget_plan[dept] = {
            'Allocation %': allocation_pct,
            'Budget Amount': budget_amount,
            'Per Period': budget_amount / len(forecast_values)
        }
    
    return pd.DataFrame(budget_plan).T
