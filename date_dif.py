'''Write a Python program to get the difference between a given number and 17, if the number is
greater than 17 return double the absolute difference.'''
x=17
n=input()
n=int(n)
if n > x:
    diff=n-x
    diff=diff*2
    print("Number is greater than 17 so multiplying the difference by 2 we get",diff)
else:
    diff=x-n
    print("Number is not smaller than 17 so te diference is ",diff)
