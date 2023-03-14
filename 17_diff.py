'''7. Write a Python program to get a new string from a given string where "Is" has been added to
the front. If the given string already begins with "Is" then return the string unchanged.'''
str1=input("enter your string")
def Is_str(strc):
    str_Is="Is "
    x=strc.index("Is")
    if x < 1:
        return strc
    else:
        strc=str_Is+strc
        return strc
str2=Is_str(str1)
print(str2)

