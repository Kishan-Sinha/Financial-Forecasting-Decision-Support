# PDF Report Generation - Execution Guide

## Overview

This guide provides step-by-step instructions to generate professional PDF reports from the Financial Forecasting Decision Support system.

## System Requirements

- **Python**: 3.7 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 2 GB (4 GB recommended for large datasets)
- **Disk Space**: 500 MB for dependencies + generated reports
- **Internet**: Required for initial pip install (optional after that)

## Step-by-Step Execution Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kishan-Sinha/Financial-Forecasting-Decision-Support.git
cd Financial-Forecasting-Decision-Support
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected Output:**
```
Collecting pandas
  Downloading pandas-x.x.x-...
Collecting numpy
  Downloading numpy-x.x.x-...
[... more packages ...]
Successfully installed pandas, numpy, statsmodels, scikit-learn, matplotlib, reportlab
```

### Step 4: Generate Sample Reports

#### Option A: Quick Sample Report (Recommended for first run)

```bash
python generate_sample_reports.py
```

**Expected Output:**
```
Loading financial data...
Data shape: (120, 1)
Data statistics:
  Mean: 5234.52
  Std Dev: 245.89
  Min: 4567.23
  Max: 6012.45
Fitting ARIMA model...
Testing different ARIMA parameters...
Best ARIMA(1,1,1) selected
Generating 12-month forecast...
Calculating performance metrics...
  MAPE: 3.45%
  RMSE: 187.23
  MAE: 156.78
Generating scenarios (Best/Base/Worst)...
Creating visualizations...
  - Forecast chart
  - Scenario comparison
  - Performance metrics
Generating PDF report...
Report saved to: Financial_Forecasting_Report.pdf (2.3 MB)
Execution completed successfully!
```

#### Option B: Full Analysis with Custom Data

1. **Prepare Your Data**
   - CSV file with columns: `date` and `value`
   - 50+ rows recommended
   - Monthly frequency

2. **Update data_loader.py**
   ```python
   # Change line 10 from:
   # data = load_plotly_data()
   # To:
   # data = pd.read_csv('your_data.csv')
   ```

3. **Run the Full Pipeline**
   ```bash
   python main.py
   ```

### Step 5: Verify Generated Files

```bash
# List generated files
ls -lh *.pdf  # macOS/Linux
dir *.pdf     # Windows
```

**Expected Output:**
```
-rw-r--r-- Financial_Forecasting_Report.pdf  2.3M
```

### Step 6: View the PDF Report

- **Windows**: Double-click the PDF file
- **macOS**: Use Preview (default) or any PDF viewer
- **Linux**: Use any PDF viewer (evince, okular, etc.)
  ```bash
  evince Financial_Forecasting_Report.pdf
  ```

## Expected PDF Report Contents

### Page 1: Title & Executive Summary
- Report title: "Financial Forecasting Report"
- Generation date and time
- Data period covered (e.g., "January 2016 - December 2025")
- Summary statistics table
- Key findings bullet points

### Page 2: ARIMA Forecast Visualization
- Line chart showing:
  - Historical data (blue line)
  - 12-month forecast (red line)
  - 95% confidence interval (shaded gray area)
- X-axis: Time periods (months)
- Y-axis: Values in original scale

### Page 3: Scenario Analysis Comparison
- Three forecast scenarios:
  - **Best Case**: 10% optimistic growth assumption
  - **Base Case**: ARIMA baseline forecast
  - **Worst Case**: 10% conservative decline assumption
- Comparative table with monthly values
- Scenario descriptions

### Page 4: Performance Metrics
- **MAPE** (Mean Absolute Percentage Error): ~2-5% for good fit
- **RMSE** (Root Mean Squared Error): Scaled to data values
- **MAE** (Mean Absolute Error): Average deviation
- **MASE** (Mean Absolute Scaled Error): Comparison to naive forecast
- Model diagnostics table

### Page 5: Budget Planning & Recommendations
- Budget allocation chart
- Variance analysis (Actual vs Forecast)
- Decision recommendations:
  - Confidence level assessment
  - Risk factors identified
  - Actionable next steps

## Troubleshooting Common Issues

### Issue 1: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'pandas'`

**Solution**:
```bash
# Reinstall all dependencies
pip install --force-reinstall -r requirements.txt
```

### Issue 2: No Data File Found

**Error**: `FileNotFoundError: Data file not found`

**Solution**:
```bash
# Ensure internet connection for automatic data download
# Or provide CSV file path in data_loader.py
```

### Issue 3: PDF Not Generated

**Error**: Report generation fails silently

**Solution**:
```bash
# Check write permissions
ls -l .  # Unix/Linux

# Verify reportlab installation
pip install --upgrade reportlab

# Run with verbose output
python generate_sample_reports.py -v
```

### Issue 4: Memory Error with Large Dataset

**Error**: `MemoryError: Unable to allocate X GB`

**Solution**:
```bash
# Process data in chunks
# Edit data_loader.py to use sampling:
data = load_data().sample(frac=0.8, random_state=42)
```

## Performance Metrics Interpretation

| Metric | Meaning | Good Range |
|--------|---------|-------------|
| **MAPE** | Percentage accuracy | < 5% (excellent), < 10% (good) |
| **RMSE** | Average error magnitude | Lower is better |
| **MAE** | Average absolute deviation | Lower is better |
| **MASE** | Scaled error vs baseline | < 1 means better than naive |

## Advanced Usage

### Custom Report Generation

```python
from report_engine import ReportGenerator
from forecast_model import ARIMAForecaster
from data_loader import load_financial_data

# Load data
data = load_financial_data()

# Fit model
forecaster = ARIMAForecaster(data)
forecaster.fit()
forecast = forecaster.predict(periods=12)
metrics = forecaster.get_metrics()

# Generate custom report
report = ReportGenerator(forecast, metrics)
report.generate_pdf('Custom_Report.pdf', title='My Custom Report')
```

### Schedule Regular Report Generation

```bash
# Linux/macOS - Daily report generation
# Add to crontab: crontab -e
0 9 * * * cd ~/Financial-Forecasting-Decision-Support && python generate_sample_reports.py
```

```batch
# Windows - Task Scheduler
# Create task to run: python generate_sample_reports.py
# Frequency: Daily at 9:00 AM
```

## Output Files Location

```
Financial-Forecasting-Decision-Support/
├── Financial_Forecasting_Report.pdf    # Generated report
├── sample_outputs/                     # Sample reports directory
├── DOCUMENTATION.md                   # Detailed documentation
└── SAMPLE_REPORT_OUTPUT.md             # Sample output details
```

## Quality Assurance Checklist

After generating a report, verify:

- [ ] PDF file exists and is > 1 MB
- [ ] All 5 pages are present
- [ ] Charts are visible and properly formatted
- [ ] Performance metrics are displayed
- [ ] Forecast dates are correct
- [ ] Budget recommendations are present
- [ ] No error messages in console

## Next Steps

1. **Review the generated PDF** - Open in your preferred PDF viewer
2. **Analyze the forecasts** - Check scenario comparisons
3. **Implement recommendations** - Use insights for decision-making
4. **Update data source** - Modify data_loader.py for custom data
5. **Schedule automation** - Set up daily/weekly report generation

## Support & Documentation

- **README.md** - Project overview and installation
- **DOCUMENTATION.md** - Comprehensive usage guide
- **REPORT_GENERATION.md** - Detailed report structure
- **SAMPLE_REPORT_OUTPUT.md** - Example outputs
- **sample_outputs/README.md** - Report directory guide

## Version Information

- **Report Generator Version**: 1.0
- **Python Compatibility**: 3.7+
- **Last Updated**: January 2025
