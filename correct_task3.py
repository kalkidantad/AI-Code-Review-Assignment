# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    """
    Computes the average of valid (non-None) numeric measurements in the input list.
    
    Args:
        values: List of values, where each is either None or convertible to float.
        
    Returns:
        float: Arithmetic mean of valid values.
        
    Raises:
        ValueError: If input is empty or contains no valid measurements.
        TypeError: If a non-None value cannot be converted to float.
    """
    if not values:
        raise ValueError("Input list is empty.")
    
    total = 0.0
    valid_count = 0

    for v in values:
        if v is not None:
            total += float(v)
            valid_count += 1

    if valid_count == 0:
        raise ValueError("No valid measurements found (all values are None).")
    
    return total / valid_count