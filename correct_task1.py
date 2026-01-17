# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    """
    Calculate the average value of non-cancelled orders.

    Args:
        orders (list): A list of order dictionaries, each expected to have
                       'status' (str) and 'amount' (numeric) keys.

    Returns:
        float: The average order value of non-cancelled orders.
               Returns 0.0 if there are no non-cancelled orders.

    Raises:
        ValueError: If any order is missing required keys or if input is not a list.
    """
    if not isinstance(orders, list):
        raise ValueError("Input must be a list of orders.")

    total = 0
    valid_order_count = 0

    for order in orders:
        if not isinstance(order, dict):
            raise ValueError("Each order must be a dictionary.")
        
        if "status" not in order or "amount" not in order:
            raise ValueError("Each order must contain 'status' and 'amount' keys.")
        
        if order["status"] != "cancelled":
            total += order["amount"]
            valid_order_count += 1

    # Avoid division by zero: return 0.0 if no valid orders exist
    if valid_order_count == 0:
        return 0.0

    return total / valid_order_count