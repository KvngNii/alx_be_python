def safe_divide(numerator, denominator):
    """
    Safely performs division with error handling for division by zero and non-numeric inputs.
    
    Parameters:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str: A message indicating the result or describing the error
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
