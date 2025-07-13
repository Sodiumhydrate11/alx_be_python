def calculate_future_age(): 
    """
    Calculates and prints the user's age in the year 2050.
    Assumes the current year is 2023.
    """
    try:
        # Prompt the user for their current age
        current_age_str = input("How old are you? ")
        print("You entered:", current_age_str)

        # Convert the input string to an integer
        current_age = int(current_age_str)

        # Calculate the age in 2050
        # The difference between 2050 and 2023 is 27 years
        future_age = current_age + 27

        # Print the result in the specified format
        print(f"In 2050, you will be {future_age} years old.")
    except ValueError:
        print("Please enter a valid integer for your age.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An error occurred: {e}")