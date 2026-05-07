def convert_temperature(fahrenheit, unit):
    if unit == "c":
        celsius = (fahrenheit - 32) * 5 / 9
        print(str(fahrenheit) + "F = " + str(celsius) + "C")
    elif unit == "k":
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        print(str(fahrenheit) + "F = " + str(kelvin) + "K")
    else:
        print("Invalid input: The temperature can only be converted to Kelvin or Celsius.")

def main():
    fahrenheit = float(input("Enter a Fahrenheit temperature: "))
    if fahrenheit < -459.67:
        print("Invalid input: A Fahrenheit temperature must not be lower than -459.67.")
        print("Program terminated.")
        return
    unit = input("Convert to k (for Kelvin) or c (for Celsius): ")
    convert_temperature(fahrenheit, unit)

main()
