def calculate_finance():
    """
    Calculates monthly savings and projected annual savings with interest
    based on user input for income and expenses.
    """
    try:
        # Prompt the user for their monthly income
        monthly_income_str = input("Enter your monthly income: ")
        monthly_income = float(monthly_income_str)

        # Prompt the user for their total monthly expenses
        monthly_expenses_str = input("Enter your total monthly expenses: ")
        monthly_expenses = float(monthly_expenses_str)

        # Calculate monthly savings
        monthly_savings = monthly_income - monthly_expenses

        # Assume a simple annual interest rate of 5% (0.05)
        annual_interest_rate = 0.05

        # Calculate projected annual savings
        # First, calculate savings over 12 months without interest
        savings_before_interest = monthly_savings * 12
        # Then, add the interest earned on those savings
        projected_annual_savings = savings_before_interest + (savings_before_interest * annual_interest_rate)

        # Display the user's monthly savings
        print(f"\nYour monthly savings: ${monthly_savings:.2f}")

        # Display the projected annual savings after including interest
        print(f"Your projected annual savings after one year (with 5% interest): ${projected_annual_savings:.2f}")

    except ValueError:
        # Handle cases where the input is not a valid number
        print("Invalid input. Please enter valid numerical values for income and expenses.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")