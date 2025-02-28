import math

class BinaryCalculator:
    def binary_to_decimal(self, binary_str):
        return int(binary_str, 2)

    def decimal_to_binary(self, decimal_num):
        return bin(decimal_num)[2:]

    def is_valid_binary(self, binary_str):
        return all(digit in '01' for digit in binary_str)

    def bitwise_operations(self, num1, num2, operator):
        result = {
            "&": num1 & num2,
            "|": num1 | num2,
            "^": num1 ^ num2,
            "%": num1 % num2,
            "**": num1 ** num2
        }.get(operator, None)
        
        if result is not None:
            max_length = max(len(bin(num1)[2:]), len(bin(num2)[2:]))
            return format(result, f'0{max_length}b')  # Ensure fixed-width binary output

    def calculate(self, *args):
        if len(args) == 1:  # Handle unary operations like NOT (~)
            bin1 = args[0][1:]  # Remove '~'
            if not self.is_valid_binary(bin1):
                raise ValueError("Invalid binary number format.")
            num1 = self.binary_to_decimal(bin1)
            result = ~num1 & ((1 << len(bin1)) - 1)  # Mask to ensure same bit length
            return self.decimal_to_binary(result).zfill(len(bin1))  # Ensure correct padding

        elif len(args) == 2:
            bin1, operation = args
            if not self.is_valid_binary(bin1):
                raise ValueError("Invalid binary number format.")
            num = self.binary_to_decimal(bin1)
            
            if operation == "fact":
                if num < 0:
                    raise ValueError("Factorial is not defined for negative numbers.")
                return math.factorial(int(num))
            
            elif operation == "log":
                if num <= 0:
                    raise ValueError("Logarithm is undefined for non-positive numbers.")
                return round(math.log2(num), 3)  # Ensure decimal rounding
            
            elif operation == "sin":
                return round(math.sin(math.radians(num)), 3)
            
            elif operation == "cos":
                return round(math.cos(math.radians(num)), 3)
            
            elif operation == "tan":
                return round(math.tan(math.radians(num)), 3)
        
        elif len(args) == 3:
            bin1, operator, bin2 = args
            if operator in ["&", "|", "^", "%", "**"]:
                if not self.is_valid_binary(bin1) or not self.is_valid_binary(bin2):
                    raise ValueError("Invalid binary number format.")
                num1, num2 = self.binary_to_decimal(bin1), self.binary_to_decimal(bin2)
                return self.bitwise_operations(num1, num2, operator)
            
            elif operator in ["<<", ">>"]:
                if not self.is_valid_binary(bin1) or not bin2.isdigit():
                    raise ValueError("Invalid binary number format.")
                num1 = self.binary_to_decimal(bin1)
                shift = int(bin2)  # Convert shift amount from string to integer
                result = num1 << shift if operator == "<<" else num1 >> shift
                return self.decimal_to_binary(result)

        raise ValueError("Invalid operation or input format.")
