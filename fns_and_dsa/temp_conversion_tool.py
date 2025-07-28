FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
# temperature conversion
def celsius_to_fahrenheit(celsius):
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Main logic
def main():
	print("=== temperature conversion ===")

	temp_input = input("Enter the temperature to convert: ")
	unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

	try:
		temperature = float(temp_input)
	except ValueError:
		raise ValueError("Invalid temperature. Please enter a numeric value.")

	if unit == 'C':
		result = celsius_to_fahrenheit(temperature)
		print(f"{temperature}°C is {result:.2f}°F")
	elif unit == 'F':
		result = fahrenheit_to_celsius(temperature)
		print(f"{temperature}°F is {result:.2f}°C")
	else:
		raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
	main()