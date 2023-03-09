#!/usr/bin/python

# Write a function to print out the multiplication tables for a given number up to a default maximum of 12
# (but let this be easily configurable).

# Set a default value for max to be 12 so if no value provided for the maximum it uses 12
def print_times_tables(x, maximum=12):
    print(f'Printing the {x} times table from 1 to {maximum}')
    # Create a range to iterate over from 1 to the maximum + 1 as we use the end + 1
    for i in range(1, maximum + 1):
        # Use an f string to print out each line of our times table formatting each number as a 2 digit integer
        print(f'{i:2d} x {x} = {i * x:2d}')


print_times_tables(5)
print_times_tables(12, 3)
