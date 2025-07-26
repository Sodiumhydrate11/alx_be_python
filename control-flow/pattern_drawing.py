def draw_square_pattern():
    """
    Prompts the user for a positive integer (size) and then prints
    a square pattern of asterisks (*) of that size using nested loops.
    """
    print("Welcome to the Pattern Drawing Program!")

    try:
        # Prompt user for pattern size
        size_str = input("Enter the size of the pattern (a positive integer): ").strip()
        size = int(size_str) # Convert input to an integer

        # Validate input: ensure it's a positive integer
        if size <= 0:
            print("Error: Please enter a positive integer for the pattern size.")
            return # Exit the function if input is invalid

        print(f"\nHere is your {size}x{size} square pattern:")
        print("-" * (size + 2)) # Simple border for visual appeal

        # Use a while loop for rows
        row_count = 0
        while row_count < size:
            # Inside the while loop, use a for loop to print asterisks for each column
            for _ in range(size): # Iterate 'size' times for each column
                print("*", end="") # Print asterisk without a newline

            # After completing each row, print a newline character to move to the next row
            print() # This prints a newline

            row_count += 1 # Increment row counter

        print("-" * (size + 2))

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    draw_square_pattern()
