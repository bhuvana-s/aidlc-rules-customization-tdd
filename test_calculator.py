"""
Unit tests for Calculator Logic
Following TDD approach - these tests will initially fail (RED phase)
"""

import pytest
from calculator_logic import Calculator


class TestCalculatorBasicOperations:
    """Test basic arithmetic operations"""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test"""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation"""
        result = self.calc.calculate(5, '+', 3)
        assert result == 8
    
    def test_subtraction(self):
        """Test subtraction operation"""
        result = self.calc.calculate(10, '-', 4)
        assert result == 6
    
    def test_multiplication(self):
        """Test multiplication operation"""
        result = self.calc.calculate(6, '*', 7)
        assert result == 42
    
    def test_division(self):
        """Test division operation"""
        result = self.calc.calculate(15, '/', 3)
        assert result == 5


class TestCalculatorDecimalNumbers:
    """Test calculator with decimal numbers"""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test"""
        self.calc = Calculator()
    
    def test_decimal_addition(self):
        """Test addition with decimal numbers"""
        result = self.calc.calculate(2.5, '+', 3.7)
        assert result == pytest.approx(6.2)
    
    def test_decimal_division(self):
        """Test division resulting in decimal"""
        result = self.calc.calculate(7, '/', 2)
        assert result == pytest.approx(3.5)
    
    def test_decimal_multiplication(self):
        """Test multiplication with decimals"""
        result = self.calc.calculate(2.5, '*', 4)
        assert result == pytest.approx(10.0)


class TestCalculatorErrorHandling:
    """Test error handling"""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test"""
        self.calc = Calculator()
    
    def test_division_by_zero(self):
        """Test division by zero raises appropriate error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.calculate(10, '/', 0)
    
    def test_invalid_operator(self):
        """Test invalid operator raises appropriate error"""
        with pytest.raises(ValueError, match="Invalid operator"):
            self.calc.calculate(5, '%', 2)


class TestCalculatorState:
    """Test calculator state management"""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test"""
        self.calc = Calculator()
    
    def test_clear_resets_state(self):
        """Test clear functionality resets calculator state"""
        self.calc.calculate(5, '+', 3)
        self.calc.clear()
        assert self.calc.get_current_value() == 0
    
    def test_sequential_operations(self):
        """Test sequential operations maintain state"""
        # 5 + 3 = 8
        result1 = self.calc.calculate(5, '+', 3)
        assert result1 == 8
        
        # 8 * 2 = 16
        result2 = self.calc.calculate(result1, '*', 2)
        assert result2 == 16
    
    def test_get_current_value(self):
        """Test getting current calculator value"""
        self.calc.calculate(10, '+', 5)
        assert self.calc.get_current_value() == 15


class TestCalculatorEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test"""
        self.calc = Calculator()
    
    def test_zero_operations(self):
        """Test operations with zero"""
        assert self.calc.calculate(0, '+', 5) == 5
        assert self.calc.calculate(5, '-', 5) == 0
        assert self.calc.calculate(0, '*', 100) == 0
    
    def test_negative_numbers(self):
        """Test operations with negative numbers"""
        assert self.calc.calculate(-5, '+', 3) == -2
        assert self.calc.calculate(5, '-', 10) == -5
        assert self.calc.calculate(-3, '*', -2) == 6
        assert self.calc.calculate(-10, '/', 2) == -5
    
    def test_large_numbers(self):
        """Test operations with large numbers"""
        result = self.calc.calculate(999999, '+', 1)
        assert result == 1000000
