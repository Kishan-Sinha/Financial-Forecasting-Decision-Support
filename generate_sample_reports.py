"""Script to generate and save sample reports with visualizations."""
import sys
from report_engine import FinancialReportEngine
from visualization_report import ReportGenerator
import pandas as pd
import numpy as np

print("\n" + "="*70)
print("FINANCIAL FORECASTING & DECISION SUPPORT - SAMPLE REPORT GENERATION")
print("="*70)

print("\nThis script generates professional PDF reports with visualizations.")
print("\nGenerated Reports:")
print("-" * 70)

try:
    # Initialize and run complete analysis
    print("\n[GENERATING] Financial Forecasting Report...")
    engine = FinancialReportEngine()
    
    # Run complete analysis and generate PDF
    results = engine.run_complete_analysis(
        output_pdf='Financial_Forecasting_Report.pdf'
    )
    
    print("\n[SUCCESS] Report generated successfully!")
    print("\nReport Details:")
    print("-" * 70)
    print(f"File: Financial_Forecasting_Report.pdf")
    print(f"Location: Root directory of repository")
    print(f"\nReport Contents:")
    print("  📄 Page 1: Title Page & Executive Summary")
    print("     - Report metadata and generation date")
    print("     - Key performance metrics")
    print("     - Model accuracy and validation results")
    print("\n  📊 Page 2: ARIMA Forecast Chart")
    print("     - Historical data visualization (blue line)")
    print("     - Forecasted values (red dashed line)")
    print("     - 95% confidence intervals (shaded region)")
    print("     - Date-based axis with proper formatting")
    print("\n  📈 Page 3: Scenario Comparison Analysis")
    print("     - Left panel: Min, Mean, Max values across scenarios")
    print("     - Right panel: Total forecast by scenario")
    print("     - Base Case, Optimistic (+15%), Pessimistic (-15%)")
    print("\n  📋 Page 4: Model Validation Metrics Table")
    print("     - MAE (Mean Absolute Error)")
    print("     - RMSE (Root Mean Squared Error)")
    print("     - MAPE (Mean Absolute Percentage Error)")
    print("     - Accuracy Score (100% - MAPE)")
    print("\n  💰 Page 5: Budget Allocation Plan")
    print("     - Pie chart: Percentage allocation by department")
    print("     - Bar chart: Dollar amounts per department")
    print("     - Operations: 40%, Marketing: 25%, R&D: 20%, Admin: 15%")
    
    print("\n" + "="*70)
    print("ANALYSIS RESULTS SUMMARY")
    print("="*70)
    
    # Display metrics
    metrics = results['metrics']
    print(f"\nModel Performance Metrics:")
    print(f"  • MAE:       ${metrics['MAE']:>15,.2f}")
    print(f"  • RMSE:      ${metrics['RMSE']:>15,.2f}")
    print(f"  • MAPE:      {metrics['MAPE']:>15.2f}%")
    print(f"  • Accuracy:  {metrics['Accuracy']:>15.2f}%")
    
    # Display forecast statistics
    forecast = results['forecast']
    print(f"\nForecast Statistics (30-day period):")
    print(f"  • Total Forecast:      ${np.sum(forecast):>15,.2f}")
    print(f"  • Average per Period:  ${np.mean(forecast):>15,.2f}")
    print(f"  • Min Value:           ${np.min(forecast):>15,.2f}")
    print(f"  • Max Value:           ${np.max(forecast):>15,.2f}")
    print(f"  • Std Deviation:       ${np.std(forecast):>15,.2f}")
    
    # Display scenario comparison
    print(f"\nScenario Analysis Results:")
    scenario_summary = results['scenario'].get_scenario_summary()
    for scenario_name, stats in scenario_summary.items():
        print(f"\n  {scenario_name}:")
        print(f"    - Mean:   ${stats['mean']:>15,.2f}")
        print(f"    - Total:  ${np.sum([stats['mean']])*30:>15,.2f}")
    
    # Display budget plan
    print(f"\nBudget Allocation Plan:")
    budget = results['budget']
    for dept, row in budget.iterrows():
        print(f"  • {dept:<20} ${row['Budget Amount']:>12,.2f} ({row['Allocation %']:>5.1f}%)")
    
    print("\n" + "="*70)
    print("📥 HOW TO ACCESS THE REPORTS")
    print("="*70)
    print("\n1. PDF Report Location: Financial_Forecasting_Report.pdf")
    print("   Download from GitHub repository root directory")
    print("\n2. View in Browser:")
    print("   - GitHub shows PDF preview in browser")
    print("   - Download for high-quality printing")
    print("\n3. Share with Stakeholders:")
    print("   - Professional 5-page PDF document")
    print("   - Ready for executive presentations")
    print("   - Print-optimized format (8.5x11 inches)")
    print("\n" + "="*70)
    print("✅ REPORT GENERATION COMPLETE")
    print("="*70)
    print(f"\nPDF file saved: Financial_Forecasting_Report.pdf")
    print("\nNext Steps:")
    print("  1. Download the PDF from the repository")
    print("  2. Review the analysis and visualizations")
    print("  3. Share with decision makers")
    print("  4. Use insights for strategic planning")
    print("\n" + "="*70 + "\n")
    
except Exception as e:
    print(f"\n[ERROR] Failed to generate report: {str(e)}")
    print(f"\nTroubleshooting:")
    print(f"  1. Ensure all dependencies are installed: pip install -r requirements.txt")
    print(f"  2. Check Python version: Python 3.7+")
    print(f"  3. Verify data loading: Check internet connection for Plotly data")
    print(f"\nError details: {type(e).__name__}: {str(e)}")
    sys.exit(1)
