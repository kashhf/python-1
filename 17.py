# Write a Python program to test whether a number is within 100 of 1000 or 2000.
def within_ranges(number):
    if abs(1000-number) <= 100 or abs(2000-number) <= 100:
        return True
    else:
        return False


number1 = 900
result = within_ranges(number1)
print(result)
