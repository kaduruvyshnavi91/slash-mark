import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost as xgb

# Load dataset
data = pd.read_csv('home_prices.csv')  # Replace with your dataset path

# Feature selection
features = ['income', 'num_schools', 'num_hospitals', 'crime_rate']
X = data[features]
y = data['sale_price']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')

# Feature importance
importance = model.feature_importances_
for i, v in enumerate(importance):
    print(f'Feature: {features[i]}, Score: {v:.5f}')