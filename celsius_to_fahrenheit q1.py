#!/usr/bin/python

# 1. Write a program using a function to convert from Celsius to Fahrenheit,
# print out what -5, 30 and 100 degrees Celsius are in Fahrenheit

# Convert a given temperature in degrees Celsius to degrees Fahrenheit
def to_fahrenheit(deg_c):
    return deg_c * (9 / 5) + 32


# Print out in Fahrenheit the values for -5, 30 and 100 degrees Celsius
print(to_fahrenheit(-5))
print(to_fahrenheit(30))
print(to_fahrenheit(100))
