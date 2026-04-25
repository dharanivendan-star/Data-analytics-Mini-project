
def detect_fraud(degree, threshold=0.1):
    suspicious = [node for node, val in degree.items() if val > threshold]
    return suspicious

