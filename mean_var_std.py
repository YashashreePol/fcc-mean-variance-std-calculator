import numpy as np


def calculate(list):

    # 1. Input Validation
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. reshape into 3x3 matrix
    matrix = np.array(list).reshape(3, 3)

    # 3. Define the Dictionary to store the calculations
    calculations = {}

    # 4. Define the metrics to calculate the functions
    metrix = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    # 5. Calculate for all metrics and dimensions
    for name, func in metrix.items():
        calculations[name] = [
            func(matrix, axis=0).tolist(),
            func(matrix, axis=1).tolist(),
            func(matrix).item()
        ]

    return calculations
