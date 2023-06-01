# Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.
def difference(number):
    if number > 17:
        return (number-17)*2
    else:
        return 17-number


print(difference(22))
print(difference(10))
