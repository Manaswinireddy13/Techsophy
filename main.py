import pandas as pd

from preprocess import preprocess_data
from churn_model import train_churn_model
from risk_scoring import predict_risk_scores
from segmentation import segment_customers
from strategies import retention_strategy

if __name__ == "__main__":
    data = pd.read_csv('techsophydataset.csv')

    X, y, scaler, feature_names = preprocess_data(data)
    model, X_test, y_test = train_churn_model(X, y)

    data['Churn_Risk_Score'] = predict_risk_scores(model, X)

    data, km_model = segment_customers(data)
    data['Retention_Strategy'] = data['Churn_Risk_Score'].apply(retention_strategy)

    print("\n--- Sample Results ---")
    print(data[['CustomerID', 'Churn_Risk_Score', 'Segment', 'Retention_Strategy']].head())
