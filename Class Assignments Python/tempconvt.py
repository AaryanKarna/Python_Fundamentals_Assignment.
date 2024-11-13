class converter:
    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

converter = converter()
t_value = float(input("Enter the temperature value: "))
t_unit = input("Enter the unit: ")
if t_unit.upper() == "C":
    converted_temp = converter.celsius_to_fahrenheit(t_value)
    print(f"{converted_temp}°F")
elif t_unit.upper() == "F":
    converted_temp = converter.fahrenheit_to_celsius(t_value)
    print(f"{converted_temp}°C")


