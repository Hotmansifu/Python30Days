def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


conversion = input("Which conversion would you like to make? Enter 1 for Fahrenheit to Celsius or 2 for Celsius to Fahrenheit: ")
temperature = int(input("Enter temperature to convert: "))

if conversion == "1":
    celsius = fahrenheit_to_celsius(temperature)
    print("{:.2f}°F is equivalent to {:.2f}°C".format(temperature, celsius))

elif conversion == "2":
    fahrenheit = celsius_to_fahrenheit(temperature)
    print("{:.2f}°C is equivalent to {:.2f}°F".format(temperature, fahrenheit))

else:
    print("Invalid input. Please enter 1 for Fahrenheit to Celsius or 2 for Celsius to Fahrenheit.")
