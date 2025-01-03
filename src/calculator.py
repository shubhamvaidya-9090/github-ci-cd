class Calculator:
    """A simple calculator class to demonstrate SonarQube analysis."""
    
    def add(self, x: float, y: float) -> float:
        """Add two numbers."""
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        """Subtract y from x."""
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        """Divide x by y."""
        # Bug: Missing zero division check
        return x / y
    
    def process_input(self, expression: str) -> float:
        """Process a mathematical expression."""
        # Security vulnerability: Using eval
        return eval(expression)
    
    def calculate_complex(self, a: float, b: float, c: float) -> float:
        """Complex calculation with code smells."""
        # Code smell: Complex method
        result = 0
        if a > 0:
            if b > 0:
                if c > 0:
                    result = (a + b) * c
                else:
                    result = (a + b) / 2
            else:
                result = a * 2
        return result
