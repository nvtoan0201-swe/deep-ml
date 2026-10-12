
import numpy as np

def linear_regression_normal_equation(
    X: list[list[float]],
    y: list[float]
) -> list[float]:
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    XT = X.T
    XTX = XT @ X
    XTX_inv = np.linalg.inv(XTX)
    XTy = XT @ y

    theta = XTX_inv @ XTy

    return np.round(theta, 4).tolist()
