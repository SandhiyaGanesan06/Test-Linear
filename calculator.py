"""
Simple calculator module for testing Linear integration
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    # BUG: No zero division check
    return a / b

def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    # BUG: Returns wrong result for empty list
    return sum(numbers) / len(numbers)
