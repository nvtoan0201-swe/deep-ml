import numpy as np
import math

def sigmoid(z: float) -> float:
    if z >= 0:
        z_exp = math.exp(-z)
        return 1 / (1 + z_exp)
    else:
        z_exp = math.exp(z)
        return z_exp / (1 + z_exp)

def predict_logistic(
    X: np.ndarray,
    weights: np.ndarray,
    bias: float
) -> np.ndarray:
    z = X @ weights + bias

    predictions = []
    for zi in z:
        probability = sigmoid(float(zi))
        prediction = 1 if probability >= 0.5 else 0
        predictions.append(prediction)

    return np.array(predictions)