# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def multiple(string, n):
    if n <= 0:
        return "its invlid a non negative integer"
    else:
        return string*n


jash = 'hlooo'
result = multiple(jash, 3)
print(result)
