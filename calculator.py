"""
Calculator Desktop Application
A minimalist calculator app built with PyQt5
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QGridLayout, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from calculator_logic import Calculator


class CalculatorApp(QMainWindow):
    """Main calculator application window"""
    
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.current_input = ""
        self.first_operand = None
        self.operator = None
        self.reset_display = False
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Create display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        self.display.setFont(QFont('Arial', 20))
        self.display.setText("0")
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 10px;
            }
        """)
        main_layout.addWidget(self.display)
        
        # Create button grid
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        main_layout.addLayout(button_layout)
        
        # Define button layout
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)  # Clear button spans full width
        ]
        
        # Create buttons
        for btn_data in buttons:
            if len(btn_data) == 3:
                text, row, col = btn_data
                button = self.create_button(text)
                button_layout.addWidget(button, row, col)
            else:
                text, row, col, row_span, col_span = btn_data
                button = self.create_button(text)
                button_layout.addWidget(button, row, col, row_span, col_span)
    
    def create_button(self, text):
        """Create a styled button"""
        button = QPushButton(text)
        button.setFixedHeight(60)
        button.setFont(QFont('Arial', 16))
        
        # Style based on button type
        if text in '0123456789.':
            # Number buttons - light gray
            button.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                }
                QPushButton:pressed {
                    background-color: #e0e0e0;
                }
            """)
        elif text in '+-*/':
            # Operator buttons - light blue
            button.setStyleSheet("""
                QPushButton {
                    background-color: #e3f2fd;
                    border: 1px solid #90caf9;
                    border-radius: 5px;
                }
                QPushButton:pressed {
                    background-color: #bbdefb;
                }
            """)
        elif text == '=':
            # Equals button - blue
            button.setStyleSheet("""
                QPushButton {
                    background-color: #2196f3;
                    color: white;
                    border: 1px solid #1976d2;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:pressed {
                    background-color: #1976d2;
                }
            """)
        elif text == 'C':
            # Clear button - red
            button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: 1px solid #d32f2f;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:pressed {
                    background-color: #d32f2f;
                }
            """)
        
        # Connect button click to handler
        button.clicked.connect(lambda: self.on_button_click(text))
        return button
    
    def on_button_click(self, text):
        """Handle button click events"""
        if text in '0123456789':
            self.handle_number(text)
        elif text == '.':
            self.handle_decimal()
        elif text in '+-*/':
            self.handle_operator(text)
        elif text == '=':
            self.handle_equals()
        elif text == 'C':
            self.handle_clear()
    
    def handle_number(self, number):
        """Handle number button press"""
        if self.reset_display:
            self.current_input = ""
            self.reset_display = False
        
        if self.current_input == "0":
            self.current_input = number
        else:
            self.current_input += number
        
        self.display.setText(self.current_input)
    
    def handle_decimal(self):
        """Handle decimal point button press"""
        if self.reset_display:
            self.current_input = "0"
            self.reset_display = False
        
        if '.' not in self.current_input:
            if not self.current_input:
                self.current_input = "0"
            self.current_input += '.'
            self.display.setText(self.current_input)
    
    def handle_operator(self, op):
        """Handle operator button press"""
        if self.current_input:
            if self.first_operand is not None and self.operator is not None:
                # Chain operations
                self.handle_equals()
            
            self.first_operand = float(self.current_input)
            self.operator = op
            self.reset_display = True
    
    def handle_equals(self):
        """Handle equals button press"""
        if self.first_operand is not None and self.operator is not None and self.current_input:
            try:
                second_operand = float(self.current_input)
                result = self.calculator.calculate(
                    self.first_operand, 
                    self.operator, 
                    second_operand
                )
                
                # Format result to remove unnecessary decimals
                if result == int(result):
                    self.display.setText(str(int(result)))
                    self.current_input = str(int(result))
                else:
                    self.display.setText(str(result))
                    self.current_input = str(result)
                
                self.first_operand = result
                self.operator = None
                self.reset_display = True
                
            except ValueError as e:
                self.display.setText(f"Error: {str(e)}")
                self.first_operand = None
                self.operator = None
                self.current_input = ""
                self.reset_display = True
    
    def handle_clear(self):
        """Handle clear button press"""
        self.current_input = ""
        self.first_operand = None
        self.operator = None
        self.reset_display = False
        self.calculator.clear()
        self.display.setText("0")


def main():
    """Main entry point for the application"""
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
