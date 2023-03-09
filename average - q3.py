#!/usr/bin/python

# 3. Write a function to return the average of any number of values passed into it
# (for bonus points, allow the configuring of which sort of average  to use all within the same function)

# Define constants for the different types of average
# A constant is just a variable whose value never changes
MEAN = 'mean'
MODE = 'mode'
MEDIAN = 'median'


# Allow passing in any number of values
# Set the default type of average to be the mean of the values passed in
def average(*values, average_type=MEAN):
    # These are what are known as guard clauses, where we test the input values to ensure
    # that they are applicable to what we want to do. We'd normally throw an exception but
    # As we haven't covered those in the course yet, we will just return None

    # Can't average an empty set of values!
    if len(values) == 0:
        return None
    # If not all of our values are numeric, again, return None
    elif not all(str(element).isnumeric() for element in values):
        return None

    # Return our mean
    # One note, in python 2, when we divide a float by an int, we get an int back
    # Python 3 will return a float when dividing however so no need to do any casting here
    # If we wanted to return an int when dividing (so 5 ÷ 2 = 2) we would do sum(values) // len(values)
    if average_type == MEAN:
        return sum(values) / len(values)

    # Cast values from a tuple to a set, so we only have each value once.
    # Then count the number of times each value in the set occurs in the values tuple
    # And return the maximum. This is not very efficient code but gets the job done!
    elif average_type == MODE:
        return max(set(values), key=values.count)

    # Sort our values, then if there is an odd number of values (so a remainder when divided by 2)
    # then return the middle value. Otherwise, return a slice of the one before the middle and
    # the one after the middle and return the mean of those two values
    elif average_type == MEDIAN:
        sorted_values = sorted(values)
        quotient, remainder = divmod(len(values), 2)
        if remainder:
            return sorted_values[quotient]
        return sorted_values[quotient - 1: quotient + 1] / 2

    # We would throw an exception here as we don't know this type of average
    # but as we haven't covered that just return None for now
    else:
        return None


# Define a tuple with our numbers in and then use unpacking to pass it into our average function each time
numbers = 4, 2, 1, 3, 3
print(f'The mean of {numbers} is: {average(*numbers)}')
print(f'The mode of {numbers} is: {average(*numbers, average_type=MODE)}')
print(f'The median of {numbers} is: {average(*numbers, average_type=MEDIAN)}')
print()

# Test out some edge cases too
print(f'An unknown sort of average gives: {average(*numbers, average_type="Unknown")}')
print(f'The mean of an empty list is: {average([])}')
print(f'The mean of values of mixed types is: {average(*numbers, "5a")}')
