import numpy as np
from typing import List, Dict, Any

def calculate_statistics(numbers: List[float]) -> Dict[str, Any]:
    """
    Given a list of 9 numbers, reshape them into a 3x3 matrix and calculate basic statistics.
    
    The statistics calculated are: mean, variance, standard deviation, max, min, and sum.
    Calculations are performed along rows, columns, and for the flattened matrix.
    
    Args:
        numbers (List[float]): A list of exactly 9 numeric elements.
    
    Returns:
        Dict[str, Any]: A dictionary containing the statistics.
                        Each key maps to a list of three elements:
                        [column-wise values, row-wise values, overall value].
    
    Raises:
        ValueError: If the input list does not contain exactly 9 numbers.
    """
    # Validate input: must contain exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("Input list must contain exactly nine numbers.")
    
    # Convert the list into a 3x3 NumPy array for matrix operations
    matrix = np.array(numbers).reshape(3, 3)
    
    # Create a dictionary to store all calculated statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of each column
            matrix.mean(axis=1).tolist(),  # Mean of each row
            matrix.mean()                  # Mean of all elements
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Variance of each column
            matrix.var(axis=1).tolist(),   # Variance of each row
            matrix.var()                   # Variance of all elements
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Standard deviation of each column
            matrix.std(axis=1).tolist(),   # Standard deviation of each row
            matrix.std()                   # Standard deviation of all elements
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Maximum of each column
            matrix.max(axis=1).tolist(),   # Maximum of each row
            matrix.max()                   # Maximum of all elements
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Minimum of each column
            matrix.min(axis=1).tolist(),   # Minimum of each row
            matrix.min()                   # Minimum of all elements
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Sum of each column
            matrix.sum(axis=1).tolist(),   # Sum of each row
            matrix.sum()                   # Sum of all elements
        ]
    }
    
    return calculations
