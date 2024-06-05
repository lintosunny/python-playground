# Write a convertToFahrenheit() function with a degreesCelsius parameter. 
# This function returns the number of this temperature in degrees Fahrenheit. 
# Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius.
# Fahrenheit = Celsius × (9 / 5) + 32
# Celsius = (Fahrenheit - 32) × (5 / 9)

def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32

def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * ( 5 / 9)
