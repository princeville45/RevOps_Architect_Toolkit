import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

class SalesForecaster:
    """
    High-Conviction Predictive Modeling
    Domain: Wholesale Logistics (C-Way Depot)
    Architect: Irem Victor Chinonso
    """
    def __init__(self):
        self.model = LinearRegression()
        
    def train_on_historical_data(self, days, sales_volume):
        """
        Trains the model on historical sales velocity.
        days: np.array of days (1, 2, 3...)
        sales_volume: np.array of units sold
        """
        X = days.reshape(-1, 1)
        y = sales_volume
        self.model.fit(X, y)
        print("Model Training Complete: Sales Velocity Index established.")

    def predict_next_period(self, next_day):
        """Predicts sales for the given day."""
        prediction = self.model.predict([[next_day]])
        return round(prediction[0], 2)

    def calculate_depletion_point(self, current_stock, avg_daily_sales):
        """Predicts when stock will hit zero based on velocity."""
        days_remaining = current_stock / avg_daily_sales
        return round(days_remaining, 1)

if __name__ == "__main__":
    forecaster = SalesForecaster()
    
    # Historical Simulation: Last 7 days at C-Way Depot
    days = np.array([1, 2, 3, 4, 5, 6, 7])
    sales = np.array([150, 165, 140, 180, 190, 210, 205]) # Units
    
    forecaster.train_on_historical_data(days, sales)
    
    next_day_prediction = forecaster.predict_next_period(8)
    stock_status = forecaster.calculate_depletion_point(1200, 180) # 1200 units, 180 avg sales
    
    print(f"Forecasted Sales (Day 8): {next_day_prediction} units")
    print(f"Inventory Depletion Warning: {stock_status} days of stock remaining.")
    print("Status: Logistics Intelligence Synchronized.")
