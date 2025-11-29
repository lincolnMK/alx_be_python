def safe_divide(numerator, denominator):
    """Divides two numbers, returning None if division by zero is attempted."""
    try:
        result = float(numerator) / float(denominator)
        return (f"The result of the division is: {result}")
    
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.")

    except ValueError:
        return ("Error: Please enter numeric values only.")
