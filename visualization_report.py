"""Generate visualizations and reports for financial forecasting."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime
import io

class ReportGenerator:
    """Generate professional reports with visualizations."""
    
    def __init__(self, title="Financial Forecasting Report"):
        self.title = title
        self.figures = []
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 7)
        plt.rcParams['font.size'] = 10
    
    def create_forecast_chart(self, historical_dates, historical_values, 
                             forecast_dates, forecast_values, confidence_upper=None, 
                             confidence_lower=None):
        """Create forecast visualization with historical data."""
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Historical data
        ax.plot(historical_dates, historical_values, 'b-o', linewidth=2, 
               label='Historical Data', markersize=4)
        
        # Forecast
        ax.plot(forecast_dates, forecast_values, 'r--s', linewidth=2, 
               label='Forecast', markersize=4)
        
        # Confidence intervals
        if confidence_upper is not None and confidence_lower is not None:
            ax.fill_between(forecast_dates, confidence_lower, confidence_upper, 
                           alpha=0.2, color='red', label='95% Confidence Interval')
        
        ax.set_xlabel('Date', fontsize=11, fontweight='bold')
        ax.set_ylabel('Value ($)', fontsize=11, fontweight='bold')
        ax.set_title('ARIMA Forecast: Historical vs. Predicted Values', 
                    fontsize=13, fontweight='bold')
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return fig
    
    def create_scenario_comparison(self, scenarios_data):
        """Create scenario comparison bar chart."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Scenario comparison
        scenarios_df = pd.DataFrame(scenarios_data)
        scenarios_df.set_index('Scenario')[['Min', 'Mean', 'Max']].plot(
            kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax1.set_title('Scenario Comparison: Min, Mean, Max Values', 
                     fontsize=12, fontweight='bold')
        ax1.set_ylabel('Value ($)', fontsize=10)
        ax1.set_xlabel('Scenario', fontsize=10)
        ax1.legend(fontsize=9)
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
        
        # Total comparison
        totals = pd.DataFrame(scenarios_data).set_index('Scenario')['Total']
        colors = ['#2ECC71' if 'Optimistic' in idx else '#E74C3C' if 'Pessimistic' in idx else '#3498DB' 
                 for idx in totals.index]
        ax2.bar(totals.index, totals.values, color=colors)
        ax2.set_title('Total Forecast by Scenario', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Total Value ($)', fontsize=10)
        ax2.set_xlabel('Scenario', fontsize=10)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
        
        # Add value labels on bars
        for i, v in enumerate(totals.values):
            ax2.text(i, v, f'${v:,.0f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def create_metrics_table(self, metrics_dict):
        """Create metrics visualization table."""
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.axis('tight')
        ax.axis('off')
        
        # Prepare data
        metrics_data = []
        for key, value in metrics_dict.items():
            if isinstance(value, float):
                metrics_data.append([key, f'{value:,.2f}'])
            else:
                metrics_data.append([key, str(value)])
        
        # Create table
        table = ax.table(cellText=metrics_data, 
                        colLabels=['Metric', 'Value'],
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.5, 0.5])
        
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        
        # Style header
        for i in range(2):
            table[(0, i)].set_facecolor('#3498DB')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Alternate row colors
        for i in range(1, len(metrics_data) + 1):
            for j in range(2):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor('#ECF0F1')
                else:
                    table[(i, j)].set_facecolor('#FFFFFF')
        
        plt.title('Model Validation Metrics', fontsize=12, fontweight='bold', pad=20)
        return fig
    
    def create_budget_allocation(self, budget_data):
        """Create budget allocation pie chart."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Pie chart
        if isinstance(budget_data, dict):
            labels = list(budget_data.keys())
            sizes = list(budget_data.values())
        else:
            labels = budget_data.index.tolist()
            sizes = budget_data['Allocation %'].tolist()
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        explode = [0.05] * len(labels)
        
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors[:len(labels)],
               autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
        ax1.set_title('Budget Allocation by Department', fontsize=12, fontweight='bold')
        
        # Bar chart with amounts
        if isinstance(budget_data, dict):
            amounts = sizes
        else:
            amounts = budget_data['Budget Amount'].tolist()
        
        ax2.barh(labels, amounts, color=colors[:len(labels)])
        ax2.set_xlabel('Budget Amount ($)', fontsize=10)
        ax2.set_title('Budget Amount by Department', fontsize=12, fontweight='bold')
        
        # Add value labels
        for i, v in enumerate(amounts):
            ax2.text(v, i, f' ${v:,.0f}', va='center', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def generate_pdf_report(self, filename, title, subtitle, 
                           forecast_fig, scenarios_fig, metrics_fig, 
                           budget_fig, summary_text):
        """Generate complete PDF report."""
        with PdfPages(filename) as pdf:
            # Title page
            fig = plt.figure(figsize=(8.5, 11))
            ax = fig.add_subplot(111)
            ax.axis('off')
            
            # Add content
            ax.text(0.5, 0.85, title, ha='center', va='center',
                   fontsize=24, fontweight='bold', transform=ax.transAxes)
            ax.text(0.5, 0.78, subtitle, ha='center', va='center',
                   fontsize=14, color='gray', transform=ax.transAxes)
            
            # Add date
            ax.text(0.5, 0.70, f'Report Generated: {datetime.now().strftime("%B %d, %Y")}',
                   ha='center', va='center', fontsize=11, transform=ax.transAxes)
            
            # Add summary
            summary_y = 0.60
            for line in summary_text.split('\n'):
                if line.strip():
                    ax.text(0.1, summary_y, line, fontsize=10, 
                           transform=ax.transAxes, wrap=True)
                    summary_y -= 0.04
            
            pdf.savefig(fig, bbox_inches='tight')
            plt.close(fig)
            
            # Add charts
            for fig in [forecast_fig, scenarios_fig, metrics_fig, budget_fig]:
                if fig is not None:
                    pdf.savefig(fig, bbox_inches='tight')
                    plt.close(fig)
        
        print(f"PDF report generated successfully: {filename}")
