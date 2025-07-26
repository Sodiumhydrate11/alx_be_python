def generate_multiplication_table():
    """
    Prompts the user for a number and then prints its multiplication
    table from 1 to 10 using a for loop.
    """
    print("Welcome to the Multiplication Table Generator!")

    try:
        # Prompt user for a number
        number_str = input("Enter a number to see its multiplication table: ").strip()
        number = int(number_str) # Convert input to an integer

        print(f"\nMultiplication Table for {number}:")
        print("-" * 30)

        # Generate and Print the Multiplication Table
        # Use a for loop to iterate from 1 to 10 (inclusive)
        for i in range(1, 11): # range(1, 11) generates numbers from 1 up to (but not including) 11
            product = number * i
            print(f"{number} * {i} = {product}")

        print("-" * 30)

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to generate the table
if __name__ == "__main__":
    generate_multiplication_table()

