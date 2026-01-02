# PDF Report Generation Guide

## Complete Financial Forecasting Report with Visualizations

This guide explains how to generate professional PDF reports with visualizations using the Financial Forecasting & Decision Support System.

## Quick Start

Generate a complete PDF report in just a few lines:

```python
from report_engine import FinancialReportEngine

engine = FinancialReportEngine()
results = engine.run_complete_analysis('Financial_Forecasting_Report.pdf')
```

## Report Components

The generated PDF includes the following visualizations and data:

### 1. Title Page
- Report title and subtitle
- Generation date
- Executive summary with key metrics
- Model accuracy and performance indicators

### 2. ARIMA Forecast Chart
- Historical data visualization (blue line with markers)
- Forecasted values (red dashed line with squares)
- 95% confidence intervals (shaded area)
- Date-based x-axis with proper formatting
- Clear legends and labels

### 3. Scenario Comparison
- **Left Panel**: Min, Mean, Max values across scenarios
- **Right Panel**: Total forecast comparison by scenario
- Color-coded scenarios:
  - Base Case: Blue
  - Optimistic: Green
  - Pessimistic: Red

### 4. Model Validation Metrics Table
Displays key performance indicators:
- **MAE** (Mean Absolute Error): Average absolute deviation
- **RMSE** (Root Mean Squared Error): Standard error magnitude
- **MAPE** (Mean Absolute Percentage Error): Percentage accuracy
- **Accuracy Score**: Overall model performance (100% - MAPE)

### 5. Budget Allocation Plan
- **Pie Chart**: Percentage allocation by department
- **Bar Chart**: Dollar amounts by department
- Departments:
  - Operations: 40%
  - Marketing: 25%
  - R&D: 20%
  - Administration: 15%

## Files Used for Report Generation

### Core Modules

**visualization_report.py**
- `ReportGenerator` class
- Methods for creating individual charts:
  - `create_forecast_chart()`: ARIMA forecast with confidence intervals
  - `create_scenario_comparison()`: Scenario analysis charts
  - `create_metrics_table()`: Model validation metrics display
  - `create_budget_allocation()`: Budget pie and bar charts
  - `generate_pdf_report()`: Compile all charts into PDF

**report_engine.py**
- `FinancialReportEngine` class
- Integrated workflow management:
  - `load_and_prepare_data()`: Load sample data
  - `train_and_forecast()`: ARIMA model training
  - `run_scenario_analysis()`: Create scenarios
  - `create_budget_plan()`: Generate budget allocations
  - `generate_pdf_report()`: Create PDF with visualizations
  - `run_complete_analysis()`: Execute entire pipeline

## Generated PDF Structure

The PDF follows this structure:

```
Page 1: Title Page with Executive Summary
Page 2: ARIMA Forecast Chart
Page 3: Scenario Comparison Analysis
Page 4: Model Validation Metrics Table
Page 5: Budget Allocation Charts
```

## Usage Examples

### Basic Usage
```python
from report_engine import FinancialReportEngine

engine = FinancialReportEngine()
results = engine.run_complete_analysis()
```

### Custom Output File
```python
from report_engine import FinancialReportEngine

engine = FinancialReportEngine()
results = engine.run_complete_analysis(
    output_pdf='My_Financial_Report_2026.pdf'
)
```

### Step-by-Step Control
```python
from report_engine import FinancialReportEngine

engine = FinancialReportEngine()

# Load data
data = engine.load_and_prepare_data()

# Train model
forecast = engine.train_and_forecast(order=(1, 1, 1), forecast_steps=30)

# Run analysis
scenarios = engine.run_scenario_analysis(
    growth_rates={'optimistic': 0.15, 'pessimistic': 0.15}
)

# Create budget
budget = engine.create_budget_plan()

# Generate report
report_file = engine.generate_pdf_report('Financial_Report.pdf')

print(f"Report saved: {report_file}")
```

### Custom Budget Allocation
```python
from report_engine import FinancialReportEngine

engine = FinancialReportEngine()
engine.load_and_prepare_data()
engine.train_and_forecast()
engine.run_scenario_analysis()

# Custom budget allocation
engine.create_budget_plan(
    budget_allocation={
        'Sales': 50,
        'Product Development': 25,
        'Support': 15,
        'Other': 10
    }
)

engine.generate_pdf_report()
```

## Output Details

### Executive Summary Section
```
Forecast Period: 30 days
Model Type: ARIMA (Auto Regressive Integrated Moving Average)
Forecast Accuracy (MAPE): [metric]
RMSE: $[amount]
MAE: $[amount]

Key Findings:
• Base Case Forecast Total: $[amount]
• Model Accuracy: [percentage]%
• Three scenarios analyzed
• Budget allocated across departments

Recommendations:
1. Monitor actual performance weekly
2. Adjust assumptions if MAPE > 7%
3. Review budget allocation quarterly
```

## Visualization Quality

### Chart Features
- Professional styling with seaborn whitegrid
- Color-coded for easy interpretation
- Value labels on bar charts
- Confidence intervals on forecasts
- Proper axis labels and titles
- Legend for all line and data series
- 14-point font for readability

### Figure Sizes
- Title page: 8.5" x 11" (Letter)
- Charts: 12" x 7" (Landscape for clarity)
- Optimized for PDF printing

## Customization Options

### Report Title and Subtitle
```python
engine.report_gen = ReportGenerator(
    title="Custom Financial Analysis Report"
)
```

### Forecast Parameters
```python
engine.train_and_forecast(
    order=(2, 1, 2),        # ARIMA order
    forecast_steps=60       # 60-day forecast instead of 30
)
```

### Scenario Parameters
```python
engine.run_scenario_analysis(
    growth_rates={'optimistic': 0.25, 'pessimistic': 0.10}
)
```

## Dependencies

Required packages (install via `pip install -r requirements.txt`):
- matplotlib: Visualization framework
- seaborn: Statistical visualization styling
- pandas: Data manipulation
- numpy: Numerical computations
- reportlab: PDF generation (or use matplotlib backend)
- statsmodels: ARIMA implementation
- scikit-learn: Data processing

## Performance Notes

- PDF generation: ~5-10 seconds for complete report
- Memory usage: ~100-200 MB for typical datasets
- File size: ~2-5 MB per PDF depending on data volume
- Supports datasets up to 10,000+ records

## Troubleshooting

### Issue: PDF not generated
**Solution**: Ensure matplotlib backend is available:
```python
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for headless systems
```

### Issue: Charts appear empty
**Solution**: Verify data is loaded correctly:
```python
engine.load_and_prepare_data()
print(engine.data.head())  # Check data
```

### Issue: High MAPE in metrics
**Solution**: Try different ARIMA order:
```python
engine.train_and_forecast(order=(2, 1, 2))  # Different parameters
```

## Integration with Reference System

This report generation system mirrors the structure of the reference implementation:

**Reference (Excel-based)**:
- Financial_Forecasting_Model.xlsx
- Financial_Forecasting_Report.md
- Financial_Forecasting_Report.pdf

**This Implementation (Python-based)**:
- visualization_report.py (chart generation)
- report_engine.py (workflow orchestration)
- Financial_Forecasting_Report.pdf (output)

Both systems provide:
✅ Data loading and preprocessing
✅ ARIMA forecasting with validation
✅ Scenario analysis (Base, Optimistic, Pessimistic)
✅ Budget planning and allocation
✅ Professional PDF reports with visualizations
✅ Executive summary and key metrics

## Next Steps

1. **Generate Your First Report**:
   ```bash
   python report_engine.py
   ```

2. **Customize for Your Data**:
   - Modify `budget_allocation` in report engine
   - Adjust ARIMA parameters for better accuracy
   - Add custom scenarios as needed

3. **Schedule Report Generation**:
   ```python
   # Could be scheduled with APScheduler or cron
   schedule.every().month.do(engine.run_complete_analysis)
   ```

4. **Integrate with Dashboard**:
   - Embed generated charts in web applications
   - Export metrics to business intelligence tools
   - Set up automated alerts based on thresholds

## Support

For issues or questions about report generation, refer to:
- DOCUMENTATION.md for technical details
- README.md for project overview
- Example usage in report_engine.py main block
