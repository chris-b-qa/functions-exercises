#!/usr/bin/python

# 4. Find palindromic numbers within a given range

# Enforce only named arguments, no positional arguments
def palindromic_numbers_in_range(*, start=1, stop=100):
    # Guard clauses to ensure we have values that we can work with
    # Check both our values are integers
    if type(start) != int or type(stop) != int:
        return None
    # Check we're not meant to stop before we've started
    elif stop < start:
        return None

    # Create an empty set
    palindromic_numbers = set()

    # Iterate through our range
    for i in range(start, stop + 1):
        # If the stringified version of i equal to the reverse of stringified then add i to our set
        # We're using the defaults for the first 2 values of our slice to get the entire string
        # and then setting the 3rd value of our slice, known as the step, to -1 to reverse it
        if str(i) == str(i)[::-1]:
            palindromic_numbers.add(i)

    return palindromic_numbers


# Find our palindromic numbers in various ranges
print(palindromic_numbers_in_range())
print(palindromic_numbers_in_range(start=3000, stop=4000))
print(palindromic_numbers_in_range(start=12030, stop=194000))

# Test some edge cases
print(palindromic_numbers_in_range(start=-5, stop=-1))
print(palindromic_numbers_in_range(start=12, stop=21))
print(palindromic_numbers_in_range(start=22, stop=20))
print(palindromic_numbers_in_range(start='a', stop=[]))
