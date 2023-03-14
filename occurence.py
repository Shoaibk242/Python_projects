# program to concatenate all elements of a list into a string
def lstr(l1):
    str1=" "
    for x in l1:
        str1=str1+x
    return str1
l2=["hello","friend",'54',"king"]
print(lstr(l2))
