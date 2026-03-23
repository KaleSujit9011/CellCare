import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split

def prepare_data(battery):
    features = ['C1', 'C2', 'C3', 'C4', 'min_voltage']
    X = battery[features]
    y = battery['capacity']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    return X_train, X_test, y_train, y_test

def train_Random_Forest(X_train, y_train):
    X_train, X_test, y_train, y_test  = prepare_data(battery)
    # train
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    return rf_model

def evaluate_model(rf_model, X_test, y_test):
    #random forest
    # predict
    y_pred = rf_model.predict(X_test)

    # evaluate
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mae,r2

if __name__ == "__main__":
    battery = pd.read_csv("../data/processed/battery_features.csv")
    X_train, X_test, y_train, y_test = prepare_data(battery)
    rf_model = train_Random_Forest(X_train, y_train)
    mae, r2 = evaluate_model(rf_model, X_test, y_test)
    print(f"Random Forest MAE: {mae:.2f}")
    print(f"Random Forest R2: {r2:.2f}")