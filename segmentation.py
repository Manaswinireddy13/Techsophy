from sklearn.cluster import KMeans

def segment_customers(df, risk_col='Churn_Risk_Score', n_segments=3):
    features = df[[risk_col, 'CustomerSatisfaction', 'TenureMonths']]
    km = KMeans(n_clusters=n_segments, random_state=42)
    df['Segment'] = km.fit_predict(features)
    return df, km
