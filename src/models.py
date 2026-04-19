import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split

from visualization import plot_actual_vs_predicted, plot_feature_importance, plot_model_comparison

import joblib
import os

def prepare_data(battery):
    features = ['C1', 'C2', 'C3', 'C4', 'min_voltage']
    X = battery[features]
    y = battery['capacity']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    return X_train, X_test, y_train, y_test

def train_Random_Forest(battery ,X_train, y_train):
    X_train, X_test, y_train, y_test  = prepare_data(battery)
    # train
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    return rf_model

def train_xgboost(battery,X_train, y_train):
    X_train,X_test, y_train ,y_test = prepare_data(battery)
    xg_model = xgb.XGBRegressor(n_estimators=100, random_state = 42)
    xg_model.fit(X_train, y_train)

    return xg_model

def evaluate_model(model, X_test, y_test):
    # predict
    y_pred = model.predict(X_test)

    # evaluate
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mae,r2,y_pred

if __name__ == "__main__":
    battery = pd.read_csv("../data/processed/battery_features.csv")
    X_train, X_test, y_train, y_test = prepare_data(battery)
    rf_model = train_Random_Forest(battery , X_train, y_train)
    xgb_model = train_xgboost(battery, X_train, y_train)
    # random forest and XGBoost
    mae_rf, r2_rf,y_predrf = evaluate_model(rf_model, X_test, y_test)
    mae_xg, r2_xg ,y_predxg = evaluate_model(xgb_model, X_test, y_test)
    print(f"Random Forest MAE: {mae_rf:.4f} | R2: {r2_rf:.4f}")
    print(f"XGBoost      MAE: {mae_xg:.4f} | R2: {r2_xg:.4f}")
    plot_actual_vs_predicted(y_test, y_predrf, 'RandomForest')
    plot_actual_vs_predicted(y_test, y_predxg, 'XGBoost')
    features = ['C1', 'C2', 'C3', 'C4', 'min_voltage']
    plot_feature_importance(rf_model, features,'Random_Forest')
    plot_feature_importance(xgb_model, features,'XGBoost')
    plot_model_comparison(mae_rf, r2_rf, mae_xg, r2_xg)

    os.makedirs('../models/saved', exist_ok=True)
    joblib.dump(rf_model, '../models/saved/rf_model.pkl')
    joblib.dump(xgb_model, '../models/saved/xgb_model.pkl')
    print("Models saved!")