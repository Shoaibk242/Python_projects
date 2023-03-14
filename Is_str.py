'''Write a Python program to check whether a specified value is contained in a group of values.
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''


l1 =[1,5,8,3]
#l1=input()
n=input("Enter element to check occurence ")
def occ(list1,i):
    for x in list1:
        if x==i:
            return "True"
            break
        else:
            return "False"
            continue
print(occ(l1,n))