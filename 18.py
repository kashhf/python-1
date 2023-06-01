# Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.
def summer(x, y, z):
    sum1 = x + y + z
    if x == y == z:
        sum1 = sum1 * 3
    return sum1


print(summer(1, 2, 3))  # Output: 6
print(summer(6, 3, 6))  # Output: 45
