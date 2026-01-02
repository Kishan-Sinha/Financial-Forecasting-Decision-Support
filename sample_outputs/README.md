# Sample Outputs

This directory contains sample outputs generated from the Financial Forecasting Decision Support system.

## Generated Reports

When you run the `generate_sample_reports.py` script, it will create the following PDF reports in this directory:

### Financial_Forecasting_Report.pdf
- **Size**: ~2-3 MB
- **Format**: Adobe PDF (Print-optimized)
- **Pages**: 5 professional pages
- **Contents**:
  - Page 1: Title Page & Executive Summary
  - Page 2: ARIMA Forecast Visualization Chart
  - Page 3: Scenario Analysis Comparison (Best/Base/Worst)
  - Page 4: Performance Metrics Table (MAPE, RMSE, MAE, MASE)
  - Page 5: Budget Allocation & Variance Charts

## How to Generate Sample Reports

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Reports
```bash
python generate_sample_reports.py
```

### Step 3: View Results
The generated PDF file will appear in this directory and can be opened with any PDF viewer.

## Report Details

### Page 1: Executive Summary
- Project overview
- Key findings summary
- Time period covered
- Dataset statistics (mean, std dev, min, max)

### Page 2: ARIMA Forecast Chart
- Historical data visualization (blue line)
- 12-month forecast (red line)
- Confidence intervals (shaded area)
- X-axis: Time periods
- Y-axis: Values in original scale

### Page 3: Scenario Analysis
- Three scenarios plotted:
  - **Best Case**: Optimistic forecast (+10% growth assumption)
  - **Base Case**: Most likely forecast (default ARIMA)
  - **Worst Case**: Conservative forecast (-10% growth assumption)
- Scenario table with values for next 12 months

### Page 4: Performance Metrics
- MAPE (Mean Absolute Percentage Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- MASE (Mean Absolute Scaled Error)
- Statistical summary table

### Page 5: Budget Planning
- Budget allocation chart
- Month-wise budget vs. forecast comparison
- Variance analysis
- Recommendations table

## Example Output Structure

```
sample_outputs/
├── README.md (this file)
├── Financial_Forecasting_Report.pdf
└── metadata.json (optional)
```

## Console Output During Generation

When running the script, you will see:
```
Loading financial data...
Data shape: (120, 1)
Fitting ARIMA(1,1,1) model...
Generating forecast...
Creating visualizations...
Generating PDF report...
Report saved to: Financial_Forecasting_Report.pdf
```

## Data Used

The sample report is generated using:
- **Source**: Time series financial data (120 months)
- **Format**: CSV/DataFrame with timestamp and value columns
- **Frequency**: Monthly data
- **Validation**: ARIMA model with automatic parameter selection

## Customization

To generate reports with your own data:

1. Update `main.py` with your data source
2. Modify `data_loader.py` to load your dataset
3. Run `python main.py` to generate custom reports

## Troubleshooting

### PDF not generated
- Ensure reportlab is installed: `pip install reportlab`
- Check write permissions in this directory
- Verify data_loader.py successfully loads data

### Memory issues with large datasets
- Process data in chunks
- Reduce visualization resolution
- Increase system RAM

## Files Reference

- `generate_sample_reports.py` - Script to generate reports
- `report_engine.py` - Core report generation engine
- `visualization_report.py` - Visualization and chart generation
- `forecast_model.py` - ARIMA model implementation
- `scenario_analysis.py` - Scenario generation and analysis
