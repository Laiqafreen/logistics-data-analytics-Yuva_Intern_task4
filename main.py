import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Step 1: Ingest preprocessed dataset from Task 2
df = pd.read_csv("Task_2_Data_Preprocessing/cleaned_logistics_data.csv")

# Define predictors and target variable
X = df[['distance_km', 'shipment_volume_units', 'fuel_cost_usd', 'labor_cost_usd', 'delay_minutes']]
y = df['actual_transit_hrs']

# Step 2: Perform 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Initialize candidate models
models = {
   

"Linear Regression": LinearRegression(),
"Decision Tree": DecisionTreeRegressor(random_state=42),
 "Random Forest": RandomForestRegressor(random_state=42)
}

# Step 4: Model evaluation loop
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    results[name] = {"MAE (hrs)": round(mae, 3), "RMSE (hrs)": round(rmse, 3), "R2 Score": round(r2, 3)}

# Step 5: Hyperparameter tuning for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
  

  estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='neg_mean_squared_error',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
best_rf = grid_search.best_estimator_

# Step 6: Evaluate tuned Random Forest model
final_preds = best_rf.predict(X_test)
final_rmse = np.sqrt(mean_squared_error(y_test, final_preds))
final_mae = mean_absolute_error(y_test, final_preds)
final_r2 = r2_score(y_test, final_preds)

print("Tuned Random Forest Model Results:")
print(f"Optimal Hyperparameters: {grid_search.best_params_}")
print(f"Mean Absolute Error (MAE): {final_mae:.3f} hours")
print(f"Root Mean Squared Error (RMSE): {final_rmse:.3f} hours")
pr;./;/l,.,int(f"Coefficient of Determination (R2): {final_r2:.3f}")
 “
