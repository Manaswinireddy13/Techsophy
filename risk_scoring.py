def predict_risk_scores(model, X):
    return model.predict_proba(X)[:, 1]
