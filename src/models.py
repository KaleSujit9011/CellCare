import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn

import joblib
import os


class LSTMModel(nn.Module):
    def __init__(self, input_size=5, hidden_size=64, num_layers=2, forecast=10):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, forecast)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])
        return output


def prepare_lstm_data(df, lookback=10, forecast=10):
    """
    Converts tabular data into sequences for LSTM
    lookback: how many past cycles to use as input
    forecast: how many future cycles to predict
    """
    features = ['C1', 'C2', 'C3', 'C4', 'min_voltage']
    target = 'capacity'

    X, y = [], []

    for i in range(len(df) - lookback - forecast + 1):
        # Input: features from cycles i to i+lookback
        X.append(df[features].iloc[i:i + lookback].values)
        # Output: capacity for next forecast cycles
        y.append(df[target].iloc[i + lookback:i + lookback + forecast].values)

    return np.array(X), np.array(y)

def train_lstm(X_train, y_train, epochs=50):
    """
    X_train shape: (num_sequences, lookback, num_features)
    y_train shape: (num_sequences, forecast)
    """
    # Convert to PyTorch tensors
    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train)

    # Initialize model
    model = LSTMModel(input_size=5, hidden_size=64, num_layers=2)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(X_train).squeeze()

        # Reshape output to match y_train
        output = output.view(-1, 10)  # (batch, forecast)

        loss = criterion(output, y_train)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')

    return model

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
    from visualization import plot_actual_vs_predicted, plot_feature_importance, plot_model_comparison
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

    # LSTM training
    print("\n=== Training LSTM ===")
    X_lstm, y_lstm = prepare_lstm_data(battery, lookback=10, forecast=10)
    print(f"LSTM data shape: X={X_lstm.shape}, y={y_lstm.shape}")

    # Split for LSTM (use first 80% for training)
    split = int(len(X_lstm) * 0.8)
    X_lstm_train = X_lstm[:split]
    y_lstm_train = y_lstm[:split]
    X_lstm_test = X_lstm[split:]
    y_lstm_test = y_lstm[split:]

    lstm_model = train_lstm(X_lstm_train, y_lstm_train, epochs=50)

    # Save LSTM model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    torch.save(lstm_model.state_dict(), os.path.join(BASE_DIR, 'models', 'saved', 'lstm_model.pth'))
    print("LSTM model saved!")

    # Evaluate LSTM
    lstm_model.eval()
    with torch.no_grad():
        X_test_tensor = torch.FloatTensor(X_lstm_test)
        lstm_pred = lstm_model(X_test_tensor).numpy()

    print(f"LSTM test predictions shape: {lstm_pred.shape}")
    print(f"Sample prediction (first sequence, 10 future capacities):\n{lstm_pred[0]}")