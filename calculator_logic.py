"""
Calculator Logic Module
Implements basic arithmetic operations with error handling
"""


class Calculator:
    """
    Calculator class that performs basic arithmetic operations.
    Maintains state for sequential calculations.
    """
    
    def __init__(self):
        """Initialize calculator with zero state"""
        self.current_value = 0
    
    def calculate(self, num1, operator, num2):
        """
        Perform calculation based on operator.
        
        Args:
            num1 (float): First operand
            operator (str): Operator (+, -, *, /)
            num2 (float): Second operand
        
        Returns:
            float: Result of the calculation
        
        Raises:
            ValueError: If operator is invalid or division by zero
        """
        # Convert inputs to float to handle both int and float
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError(f"Invalid operator: {operator}")
        
        # Update current value
        self.current_value = result
        return result
    
    def clear(self):
        """Reset calculator to initial state"""
        self.current_value = 0
    
    def get_current_value(self):
        """
        Get the current calculator value.
        
        Returns:
            float: Current value stored in calculator
        """
        return self.current_value
