"""
Calculator class implementation with intentional bugs for Linear testing
"""

class Calculator:
    """A simple calculator class with basic arithmetic operations"""
    
    def __init__(self):
        """Initialize calculator with history tracking"""
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Raise base to the power of exponent"""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def calculate_average(self, numbers):
        """Calculate average of a list of numbers"""
        # BUG: Returns wrong result for empty list
        result = sum(numbers) / len(numbers)
        self.history.append(f"avg({numbers}) = {result}")
        return result
    
    def get_history(self):
        """Return calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
    
    def get_last_result(self):
        """Get the last calculation from history"""
        # BUG: No check for empty history
        return self.history[-1]
