"""ARIMA forecasting model for time series prediction."""
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
warnings.filterwarnings('ignore')

class ARIMAForecaster:
    """ARIMA-based forecasting model for financial time series."""
    
    def __init__(self, order=(1, 1, 1)):
        """
        Initialize ARIMA model.
        order: tuple (p, d, q) for ARIMA parameters
        """
        self.order = order
        self.model = None
        self.fitted_model = None
        self.results = None
        
    def fit(self, data):
        """Fit ARIMA model to training data."""
        try:
            self.model = ARIMA(data, order=self.order)
            self.fitted_model = self.model.fit()
            self.results = self.fitted_model
            return True
        except Exception as e:
            print(f"Error fitting model: {e}")
            return False
    
    def forecast(self, steps=30):
        """
        Generate forecast for specified number of steps.
        Returns: forecast values and confidence intervals
        """
        if self.fitted_model is None:
            raise ValueError("Model not fitted. Call fit() first.")
        
        forecast_result = self.fitted_model.get_forecast(steps=steps)
        forecast_df = forecast_result.summary_frame()
        return forecast_df
    
    def get_summary(self):
        """Return model summary statistics."""
        if self.fitted_model is None:
            return None
        return self.fitted_model.summary()

def calculate_mape(actual, predicted):
    """
    Calculate Mean Absolute Percentage Error.
    MAPE = (1/n) * Σ(|actual - predicted| / |actual|) * 100
    """
    mask = actual != 0
    return np.mean(np.abs((actual[mask] - predicted[mask]) / actual[mask])) * 100

def calculate_rmse(actual, predicted):
    """
    Calculate Root Mean Squared Error.
    RMSE = sqrt((1/n) * Σ(actual - predicted)²)
    """
    return np.sqrt(np.mean((actual - predicted) ** 2))

def validate_model(actual, predicted):
    """
    Comprehensive model validation with multiple metrics.
    Returns: dictionary with MAE, RMSE, MAPE, and accuracy score
    """
    mae = np.mean(np.abs(actual - predicted))
    rmse = calculate_rmse(actual, predicted)
    mape = calculate_mape(actual, predicted)
    
    # Accuracy score (inverted MAPE, capped at 100%)
    accuracy = min(100, 100 - mape) if mape < 100 else 0
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape,
        'Accuracy': accuracy
    }

def auto_arima_order(data, max_p=5, max_d=2, max_q=5):
    """
    Suggest best ARIMA order by testing combinations.
    Uses AIC criterion for model selection.
    """
    best_aic = float('inf')
    best_order = (0, 0, 0)
    
    for p in range(max_p + 1):
        for d in range(max_d + 1):
            for q in range(max_q + 1):
                try:
                    model = ARIMA(data, order=(p, d, q))
                    results = model.fit()
                    if results.aic < best_aic:
                        best_aic = results.aic
                        best_order = (p, d, q)
                except:
                    continue
    
    return best_order
