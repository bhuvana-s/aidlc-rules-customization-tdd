# Calculator Desktop App

A minimalist calculator desktop application built with Python and PyQt5.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Decimal Number Support**: Calculate with decimal numbers
- **Error Handling**: Graceful handling of division by zero and invalid operations
- **Clean, Minimalist Design**: Simple and intuitive user interface
- **Sequential Operations**: Chain multiple calculations together

## Requirements

- Python 3.7 or higher
- macOS (primary target platform)
- PyQt5

## Installation

1. **Clone or download this repository**

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the calculator application:

```bash
python calculator.py
```

### How to Use

1. Click number buttons (0-9) to enter numbers
2. Click operator buttons (+, -, *, /) to select an operation
3. Click equals (=) to calculate the result
4. Click clear (C) to reset the calculator
5. Use the decimal point (.) for decimal numbers

### Example Calculations

- **Simple**: `5 + 3 =` → Result: `8`
- **Decimal**: `7 / 2 =` → Result: `3.5`
- **Sequential**: `5 + 3 = * 2 =` → Result: `16`

## Testing

The calculator logic is fully unit tested using pytest.

Run the test suite:

```bash
pytest test_calculator.py -v
```

Expected output: All 15 tests should pass.

## Project Structure

```
calculator-app/
├── calculator.py           # Main GUI application
├── calculator_logic.py     # Calculator logic class
├── test_calculator.py      # Unit tests for calculator logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Architecture

The application follows a clean separation of concerns:

- **calculator_logic.py**: Core calculator logic with no GUI dependencies
  - Handles arithmetic operations
  - Manages calculator state
  - Provides error handling

- **calculator.py**: PyQt5 GUI application
  - Creates the user interface
  - Handles user interactions
  - Integrates with calculator logic

- **test_calculator.py**: Comprehensive unit tests
  - Tests all arithmetic operations
  - Tests error handling
  - Tests edge cases and boundary conditions

## Error Handling

The calculator handles the following error conditions:

- **Division by Zero**: Displays "Error: Cannot divide by zero"
- **Invalid Operations**: Prevents invalid calculations
- **Input Validation**: Ensures proper number formatting

## Design Philosophy

This calculator follows a minimalist design approach:

- Clean, uncluttered interface
- Simple button layout
- Clear visual feedback
- Intuitive operation
- No unnecessary features

## Compatibility

- **Primary Platform**: macOS
- **Python Version**: 3.7+
- **GUI Framework**: PyQt5

## Development

Built using Test-Driven Development (TDD):

1. **RED**: Write failing tests
2. **GREEN**: Implement minimal code to pass tests
3. **REFACTOR**: Improve code quality

All calculator logic is fully tested before GUI implementation.

## License

This project is provided as-is for educational and personal use.
