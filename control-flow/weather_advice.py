def get_clothing_recommendation():
    """
    Prompts the user for current weather conditions and provides
    clothing recommendations based on the input using if/elif/else statements.
    """
    # Prompt the user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Provide clothing recommendations based on the user's input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the function to get the recommendation
if __name__ == "__main__":
    get_clothing_recommendation()
