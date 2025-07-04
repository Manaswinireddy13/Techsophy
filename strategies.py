def retention_strategy(score):
    if score > 0.7:
        return 'High risk ➝ Priority call + discount'
    elif score > 0.4:
        return 'Medium risk ➝ Loyalty email'
    else:
        return 'Low risk ➝ Standard engagement'
