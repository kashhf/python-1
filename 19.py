#  Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# #  Return the string unchanged if the given string already begins with "Is".
def come_back(stro):
    if stro.startswith("Is"):
        return stro
    else:
        return "Is"+stro


stro1 = "Going"
result = come_back(stro1)
print(result)
