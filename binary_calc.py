import math
import re

class BinaryCalculator:
    def __init__(self):
        """Initialize memory for storing the last result and history log."""
        self.memory = None
        self.history = []

    def is_valid_binary(self, binary):
        """Check if a string is a valid binary number (supports floating points and negatives)."""
        return bool(re.fullmatch(r"-?[01]+(\.[01]+)?", binary))

    def decimal_to_binary(self, num):
        """Convert decimal to binary (supports floating points)."""
        if isinstance(num, int):  # Integer case
            return bin(num)[2:] if num >= 0 else "-" + bin(abs(num))[2:]

        # Floating-point case
        integer_part = int(num)
        fractional_part = abs(num - integer_part)
        binary_integer = bin(abs(integer_part))[2:]

        # Convert fractional part
        binary_fraction = ""
        max_precision = 15  # Set precision limit
        while fractional_part and len(binary_fraction) < max_precision:
            fractional_part *= 2
            bit = int(fractional_part)
            binary_fraction += str(bit)
            fractional_part -= bit

        binary_result = binary_integer + ("." + binary_fraction if binary_fraction else "")
        return binary_result if num >= 0 else "-" + binary_result

    def binary_to_decimal(self, binary):
        """Convert binary to decimal (supports floating points)."""
        if not self.is_valid_binary(binary):
            raise ValueError("Invalid binary number format.")

        negative = binary.startswith("-")
        if negative:
            binary = binary[1:]

        if "." in binary:
            integer_part, fractional_part = binary.split(".")
            decimal_integer = int(integer_part, 2)
            decimal_fraction = sum(int(bit) * (1 / (2 ** (i + 1))) for i, bit in enumerate(fractional_part))
            result = decimal_integer + decimal_fraction
        else:
            result = int(binary, 2)

        return -result if negative else result

    def add_to_history(self, operation, result):
        """Store operation and result in history."""
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self):
        """Display previous calculations."""
        print("\nCalculation History:")
        if not self.history:
            print("No previous calculations.")
        else:
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")

    def scientific_operations(self, operation, num):
        """Perform scientific functions including exponentiation, factorial, and hyperbolic functions."""
        functions = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "sqrt": math.sqrt,
            "exp": math.exp,
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh
        }

        if operation in functions:
            if operation == "log" and num <= 0:
                raise ValueError("Logarithm is undefined for non-positive numbers.")
            if operation == "sqrt" and num < 0:
                raise ValueError("Square root of a negative number is not supported.")
            return functions[operation](num)
        elif operation == "fact":
            if num < 0 or not num.is_integer():
                raise ValueError("Factorial is only defined for non-negative integers.")
            return math.factorial(int(num))
        else:
            raise ValueError("Unsupported scientific operation.")

    def binary_calculator(self):
        print("Binary Calculator with Floating-Point Arithmetic & Scientific Operations")
        print("Operations: +, -, *, /, &, |, ^, ~, <<, >>, sin, cos, tan, log, sqrt, exp, sinh, cosh, tanh, fact, HIST")

        bin1 = input("Enter first binary number (or 'M' for memory, 'HIST' for history): ").strip().upper()

        if bin1 == "HIST":
            self.show_history()
            return

        if bin1 == "M":
            if self.memory is None:
                print("Error: No previous result stored in memory.")
                return
            num1 = self.memory
        else:
            if not self.is_valid_binary(bin1):
                print("Error: Invalid binary number format.")
                return
            num1 = self.binary_to_decimal(bin1)

        operator = input("Enter operation (+, -, *, /, &, |, ^, ~, <<, >>, sin, cos, tan, log, sqrt, exp, sinh, cosh, tanh, fact): ").strip()

        if operator in {"+", "-", "*", "/", "&", "|", "^", "<<", ">>"}:
            bin2 = input("Enter second binary number: ").strip()
            if not self.is_valid_binary(bin2):
                print("Error: Invalid binary number format.")
                return
            num2 = self.binary_to_decimal(bin2)
        else:
            num2 = None

        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
            elif operator == '&':
                result = int(num1) & int(num2)
            elif operator == '|':
                result = int(num1) | int(num2)
            elif operator == '^':
                result = int(num1) ^ int(num2)
            elif operator == '~':
                result = ~int(num1)
            elif operator == "<<":
                result = int(num1) << int(num2)
            elif operator == ">>":
                result = int(num1) >> int(num2)
            elif operator in {"sin", "cos", "tan", "log", "sqrt", "exp", "sinh", "cosh", "tanh", "fact"}:
                result = self.scientific_operations(operator, num1)
                print(f"Scientific Result: {result}")
                self.add_to_history(f"{operator}({bin1})", result)
                return
            else:
                print("Error: Unsupported operation.")
                return

            binary_result = self.decimal_to_binary(result)
            print(f"Result in Binary: {binary_result}")

            self.memory = result
            self.add_to_history(f"{bin1} {operator} {bin2}", binary_result)

        except ValueError as e:
            print(f"Error: {e}")

# Run the binary calculator
calculator = BinaryCalculator()
calculator.binary_calculator()
