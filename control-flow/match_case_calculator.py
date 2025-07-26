def calculator_with_match_case():
    """
    Prompts the user for two numbers and an operation, then performs
    the calculation using a match-case statement. Handles division by zero.
    """
    print("Welcome to the Match Case Calculator!")

    try:
        # Prompt for user input - two numbers
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str) # Use float to allow decimal numbers

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str) # Use float to allow decimal numbers

        # Ask for the type of operation
        operation = input("Choose the operation (+, -, *, /): ").strip()

        result = None # Initialize result variable

        # Perform the calculation using Match Case
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            case '-':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            case '*':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            case '/':
                # Handle division by zero case gracefully
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
            case _: # Default case for invalid operation
                print("Error: Invalid operation selected. Please choose from +, -, *, /.")

    except ValueError:
        print("Error: Invalid number input. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator function
if __name__ == "__main__":
    calculator_with_match_case()

