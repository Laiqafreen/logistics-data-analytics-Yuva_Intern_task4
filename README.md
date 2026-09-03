# Task 4 Summary Description: Predictive Modeling and Optimization in Logistics Systems

Task 4 transitions the project from descriptive exploratory analysis to actionable predictive modeling and strategic route optimization. The primary goal is to address unpredictable delivery windows and rising fuel expenses in last-mile logistics by accurately forecasting route transit durations (`actual_transit_hrs`) and formulating data-driven dispatch strategies.

The task was executed across a structured four-stage machine learning and analytics workflow:

1. Dataset Ingestion & Preparation: Processed 1,000 sanitized dispatch records from the Task 2 cleaning pipeline, leveraging features including total mileage (`distance_km`), package payload volumes (`shipment_volume_units`), fuel expenses (`fuel_cost_usd`), labor costs (`labor_cost_usd`), and dwell delays (`delay_minutes`). An 80/20 train-test split was established for unbiased validation.

2. Model Selection & Tuning: Implemented and evaluated three regression algorithms: Multiple Linear Regression (baseline), Decision Tree Regressor, and a Random Forest Regressor. The Random Forest model was selected as the optimal architecture and tuned using 5-fold cross-validation via `GridSearchCV` (`n_estimators`, `max_depth`, `min_samples_split`) to prevent overfitting and capture non-linear traffic and payload dynamics.

3. Performance Validation: Evaluated candidate models against standard regression metrics. The tuned Random Forest model outperformed baseline approaches, achieving a Mean Absolute Error (MAE) of 0.210 hours (~12.6 minutes), a Root Mean Squared Error (RMSE) of 0.290 hours (~17.4 minutes), and a Coefficient of Determination ($R^2$) of 0.940, accounting for 94% of total transit variance.

4. Operational Optimization: Feature importance rankings revealed that route distance and drop-off delays contribute to over 70% of transit variability. Consequently, three actionable optimization policies were established: implementing dynamic spatial route clustering (capping urban delivery zones to a 25 km radius), enforcing van load limits (max 80 units per vehicle), and integrating morning model predictions directly into the dispatch engine to reassign high-delay runs to off-peak hours.

This complete machine learning and optimization pipeline provides a scalable, copy-paste-ready solution for logistics managers to improve SLA compliance and reduce fleet operating overhead.
