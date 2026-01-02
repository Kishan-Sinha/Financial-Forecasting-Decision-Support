# Financial-Forecasting-Decision-Support
A comprehensive financial forecasting tool using ARIMA models, scenario analysis, and decision support features. Implements time series analysis with validation metrics (MAPE, RMSE) and budget planning capabilities.

## Features

- **ARIMA Time Series Forecasting**: Automatic parameter selection and model fitting
- **Scenario Analysis**: Generate best-case, base-case, and worst-case forecasts
- **Performance Metrics**: MAPE, RMSE, MAE, MASE calculations
- **Budget Planning**: Integrated budget allocation and variance analysis
- **PDF Report Generation**: Professional 5-page PDF reports with visualizations
- **Decision Support**: Actionable insights and recommendations

## Quick Start

### Installation

```bash
git clone https://github.com/Kishan-Sinha/Financial-Forecasting-Decision-Support.git
cd Financial-Forecasting-Decision-Support
pip install -r requirements.txt
```

### Generate Sample Reports

```bash
python generate_sample_reports.py
```

This will create `Financial_Forecasting_Report.pdf` in the current directory.

### Run Full Analysis

```bash
python main.py
```

For custom data, modify the data source in `data_loader.py`.

## Project Structure

```
.
├── data_loader.py              # Data loading and preprocessing
├── forecast_model.py          # ARIMA model implementation
├── scenario_analysis.py       # Scenario generation module
├── visualization_report.py    # Chart and visualization generation
├── report_engine.py          # PDF report generation engine
├── generate_sample_reports.py # Demo script
├── main.py                   # Main execution script
├── requirements.txt           # Dependencies
├─┠─ sample_outputs/            # Sample PDF reports location
├┤── DOCUMENTATION.md          # Comprehensive usage guide
├── REPORT_GENERATION.md       # PDF generation details
└── SAMPLE_REPORT_OUTPUT.md    # Sample report documentation
```

## Generated PDF Reports

### Sample Report Structure

The system generates professional 5-page PDF reports containing:

1. **Title & Executive Summary**
   - Project overview and key findings
   - Dataset statistics
   - Analysis period

2. **ARIMA Forecast Visualization**
   - Historical data plot (blue line)
   - 12-month forecast (red line)
   - 95% confidence intervals (shaded area)

3. **Scenario Analysis**
   - Best-case scenario (+10% growth)
   - Base-case forecast (ARIMA model)
   - Worst-case scenario (-10% growth)
   - Comparative table

4. **Performance Metrics**
   - MAPE (Mean Absolute Percentage Error)
   - RMSE (Root Mean Squared Error)
   - MAE (Mean Absolute Error)
   - MASE (Mean Absolute Scaled Error)

5. **Budget Planning & Recommendations**
   - Budget allocation charts
   - Variance analysis
   - Decision recommendations

## Usage Examples

### Basic Forecast

```python
from forecast_model import ARIMAForecaster
from data_loader import load_financial_data

data = load_financial_data()
forecaster = ARIMAForecaster(data)
forecast = forecaster.fit_predict(periods=12)
metrics = forecaster.calculate_metrics()
print(f"MAPE: {metrics['mape']:.2f}%")
```

### Generate Scenarios

```python
from scenario_analysis import ScenarioAnalyzer

analyzer = ScenarioAnalyzer(forecast_data)
best_case = analyzer.best_case_scenario(growth_rate=0.10)
base_case = analyzer.base_case_scenario()
worst_case = analyzer.worst_case_scenario(growth_rate=-0.10)
```

### Create PDF Report

```python
from report_engine import ReportGenerator

report_gen = ReportGenerator(forecast, metrics, scenarios)
report_gen.generate_pdf('Financial_Forecasting_Report.pdf')
```

## PDF Report Files Location

Generated PDF reports are saved in the `sample_outputs/` directory:

```
sample_outputs/
├── README.md                          # Report documentation
├── Financial_Forecasting_Report.pdf   # Main report (generated locally)
└── [additional reports here]          # More custom reports
```

**Note**: PDF files are generated when you run `python generate_sample_reports.py` locally. See `sample_outputs/README.md` for detailed instructions.

## Key Modules

### data_loader.py
Loads and preprocesses financial time series data from various sources.

### forecast_model.py
Implements ARIMA time series forecasting with automatic parameter optimization.

### scenario_analysis.py
Generates multiple forecast scenarios for decision support.

### visualization_report.py
Creates professional charts and visualizations for PDF reports.

### report_engine.py
Core PDF generation engine using ReportLab.

## Requirements

- Python 3.7+
- pandas
- numpy
- statsmodels (ARIMA)
- scikit-learn
- matplotlib
- reportlab (PDF generation)

## Dataset

The system uses financial time series data (120 months) with:
- Monthly frequency
- Multiple years of historical data
- Suitable for ARIMA modeling

## Performance Metrics Explained

- **MAPE**: Mean Absolute Percentage Error (0-100%, lower is better)
- **RMSE**: Root Mean Squared Error (in original data units)
- **MAE**: Mean Absolute Error (average deviation)
- **MASE**: Mean Absolute Scaled Error (comparison to naive forecast)

## Customization

1. **Change Data Source**: Update `data_loader.py`
2. **Adjust ARIMA Parameters**: Modify `forecast_model.py`
3. **Custom Scenarios**: Edit `scenario_analysis.py`
4. **Report Styling**: Update `report_engine.py`

## Documentation

- `DOCUMENTATION.md` - Comprehensive usage guide
- `REPORT_GENERATION.md` - Detailed PDF generation guide
- `SAMPLE_REPORT_OUTPUT.md` - Sample report structure and examples
- `sample_outputs/README.md` - Report files and execution instructions

## Workflow

```
Raw Data
   → Data Loading & Preprocessing
   → ARIMA Model Fitting
   → Forecast Generation (12 months)
   → Scenario Analysis (Best/Base/Worst)
   → Performance Metrics Calculation
   → Visualization Creation
   → PDF Report Generation
```

## Author

Kishan-Sinha

## License

MIT License

