"""Integrated report generation engine for complete financial forecasting system."""
import pandas as pd
import numpy as np
from data_loader import load_sample_data, prepare_data, get_train_test_split
from forecast_model import ARIMAForecaster, validate_model
from scenario_analysis import ScenarioAnalysis, calculate_budget_plan
from visualization_report import ReportGenerator
from datetime import datetime, timedelta

class FinancialReportEngine:
    """Complete system for generating financial forecasting reports with visualizations."""
    
    def __init__(self):
        self.data = None
        self.forecaster = None
        self.scenario = None
        self.budget_plan = None
        self.metrics = None
        self.report_gen = ReportGenerator()
    
    def load_and_prepare_data(self):
        """Load and prepare financial data."""
        print("\n[1/5] Loading and preparing data...")
        self.data = load_sample_data()
        self.data = prepare_data(self.data, target_column='Sales' if 'Sales' in self.data.columns else self.data.columns[1])
        print(f"Data prepared: {len(self.data)} records")
        return self.data
    
    def train_and_forecast(self, order=(1, 1, 1), forecast_steps=30):
        """Train ARIMA model and generate forecast."""
        print("\n[2/5] Training ARIMA model and generating forecast...")
        
        train_df, test_df = get_train_test_split(self.data, test_size=0.2)
        target_col = 'Sales' if 'Sales' in self.data.columns else self.data.columns[1]
        
        self.forecaster = ARIMAForecaster(order=order)
        self.forecaster.fit(train_df[target_col].values)
        
        # Generate forecast
        forecast_df = self.forecaster.forecast(steps=forecast_steps)
        self.forecast_values = forecast_df['mean'].values
        self.forecast_ci_lower = forecast_df['mean_ci_lower'].values
        self.forecast_ci_upper = forecast_df['mean_ci_upper'].values
        
        # Validate
        test_forecast = self.forecaster.fitted_model.fittedvalues[-len(test_df):]
        self.metrics = validate_model(test_df[target_col].values, test_forecast)
        
        print(f"Forecast generated for {forecast_steps} periods")
        print(f"Model Accuracy: {self.metrics['Accuracy']:.2f}%")
        
        return self.forecast_values
    
    def run_scenario_analysis(self, growth_rates={'optimistic': 0.15, 'pessimistic': 0.15}):
        """Run scenario analysis on forecast."""
        print("\n[3/5] Running scenario analysis...")
        
        self.scenario = ScenarioAnalysis(self.forecast_values, base_case_name='Base Case')
        self.scenario.add_optimistic_scenario(growth_rate=growth_rates['optimistic'], 
                                             name='Optimistic (15% Growth)')
        self.scenario.add_pessimistic_scenario(decline_rate=growth_rates['pessimistic'], 
                                              name='Pessimistic (15% Decline)')
        
        comparison = self.scenario.get_scenario_comparison()
        print("\nScenario Comparison:")
        print(comparison)
        
        return comparison
    
    def create_budget_plan(self, budget_allocation=None):
        """Generate budget allocation plan."""
        print("\n[4/5] Creating budget allocation plan...")
        
        if budget_allocation is None:
            budget_allocation = {
                'Operations': 40,
                'Marketing': 25,
                'R&D': 20,
                'Administration': 15
            }
        
        self.budget_plan = calculate_budget_plan(self.forecast_values, budget_allocation)
        print("\nBudget Plan:")
        print(self.budget_plan)
        
        return self.budget_plan
    
    def generate_pdf_report(self, filename='Financial_Forecasting_Report.pdf'):
        """Generate comprehensive PDF report with visualizations."""
        print("\n[5/5] Generating PDF report...")
        
        # Prepare data for visualizations
        target_col = 'Sales' if 'Sales' in self.data.columns else self.data.columns[1]
        historical_dates = self.data[self.data.columns[0] if self.data.columns[0] != target_col else self.data.columns[1]]
        if not isinstance(historical_dates.iloc[0], (pd.Timestamp, np.datetime64)):
            historical_dates = pd.date_range(start='2022-01-01', periods=len(self.data), freq='D')
        
        forecast_dates = pd.date_range(start=historical_dates.iloc[-1] + timedelta(days=1), periods=len(self.forecast_values), freq='D')
        
        # Create visualizations
        forecast_fig = self.report_gen.create_forecast_chart(
            historical_dates, self.data[target_col].values,
            forecast_dates, self.forecast_values,
            self.forecast_ci_upper, self.forecast_ci_lower
        )
        
        # Scenario comparison data
        scenarios_data = self.scenario.get_scenario_summary()
        scenarios_list = [
            {'Scenario': name, 'Min': stats['min'], 'Mean': stats['mean'], 'Max': stats['max'], 'Total': np.sum(values)}
            for name, (values, stats) in [(k, (v, scenarios_data[k])) for k, v in self.scenario.scenarios.items()]
        ]
        
        scenarios_fig = self.report_gen.create_scenario_comparison(scenarios_list)
        metrics_fig = self.report_gen.create_metrics_table(self.metrics)
        budget_fig = self.report_gen.create_budget_allocation(self.budget_plan)
        
        # Summary text
        summary_text = f"""Executive Summary
        
Forecast Period: 30 days
Model Type: ARIMA (Auto Regressive Integrated Moving Average)
Forecast Accuracy (MAPE): {self.metrics['MAPE']:.2f}%
RMSE: ${self.metrics['RMSE']:,.2f}
MAE: ${self.metrics['MAE']:,.2f}

Key Findings:
• Base Case Forecast Total: ${np.sum(self.forecast_values):,.2f}
• Model Accuracy: {self.metrics['Accuracy']:.1f}%
• Three scenarios analyzed: Base, Optimistic (+15%), Pessimistic (-15%)
• Budget allocated across 4 departments

Recommendations:
1. Monitor actual performance against forecast weekly
2. Adjust growth assumptions if MAPE exceeds 7%
3. Review budget allocation quarterly based on actual spend"""
        
        # Generate PDF
        self.report_gen.generate_pdf_report(
            filename,
            'Financial Forecasting & Decision Support Report',
            'ARIMA Time Series Analysis with Scenario Planning',
            forecast_fig, scenarios_fig, metrics_fig, budget_fig,
            summary_text
        )
        
        print(f"PDF Report generated: {filename}")
        return filename
    
    def run_complete_analysis(self, output_pdf='Financial_Forecasting_Report.pdf'):
        """Execute complete financial forecasting and reporting workflow."""
        print("\n" + "="*60)
        print("Financial Forecasting & Decision Support System")
        print("="*60)
        
        # Execute pipeline
        self.load_and_prepare_data()
        self.train_and_forecast()
        self.run_scenario_analysis()
        self.create_budget_plan()
        self.generate_pdf_report(output_pdf)
        
        print("\n" + "="*60)
        print("[SUCCESS] Complete analysis finished!")
        print(f"Report saved to: {output_pdf}")
        print("="*60)
        
        return {
            'data': self.data,
            'forecast': self.forecast_values,
            'metrics': self.metrics,
            'scenario': self.scenario,
            'budget': self.budget_plan,
            'report_file': output_pdf
        }

if __name__ == "__main__":
    engine = FinancialReportEngine()
    results = engine.run_complete_analysis('Financial_Forecasting_Report.pdf')
