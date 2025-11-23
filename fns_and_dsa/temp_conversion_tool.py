FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return round(celsius, 2)
def  convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return round(fahrenheit, 2)


temp_input = float(input("Enter the temperature to convert: "))

unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if unit_input.upper() == 'C':
    converted_temp = convert_to_fahrenheit(temp_input)
    print(f"{temp_input}°C is {converted_temp}°F")
elif unit_input.upper() == 'F':
    converted_temp = convert_to_celsius(temp_input)
    print(f"{temp_input}°F is {converted_temp}°C")  
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")