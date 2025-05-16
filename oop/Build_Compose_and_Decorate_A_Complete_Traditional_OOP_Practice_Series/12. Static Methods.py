# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.




class TemperatureConverter():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Celsius ko Fahrenheit mein convert karte hain



print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
print(TemperatureConverter.celsius_to_fahrenheit(0))   # Output: 32.0