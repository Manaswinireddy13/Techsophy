from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    df = df.copy()

    # Encode Gender, PolicyType
    for col in ['Gender', 'PolicyType']:
        df[col] = LabelEncoder().fit_transform(df[col])

    # Feature matrix and target
    X = df.drop(['CustomerID', 'Churn'], axis=1)
    y = df['Churn']

    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns.tolist()
