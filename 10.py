# User
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
n = int(input("enter an integer:"))
result = n+(n*11)+(n*111)
print(result)
