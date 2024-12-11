def analyze_biometric_data(data):
    """
    Analyzes biometric data for health issues.

    Parameters:
    - data (dict): A dictionary containing biometric data with keys 'heart_rate' and 'blood_pressure'.

    Returns:
    - dict: Analysis results indicating any health issues.
    """
    results = {}
    
    # Example thresholds
    if data['heart_rate'] < 60 or data['heart_rate'] > 100:
        results['heart_rate_issue'] = "Abnormal heart rate detected."
    else:
        results['heart_rate_issue'] = "Heart rate is normal."

    if data['blood_pressure'][0] > 130 or data['blood_pressure'][1] > 80:
        results['blood_pressure_issue'] = "High blood pressure detected."
    else:
        results['blood_pressure_issue'] = "Blood pressure is normal."

    return results