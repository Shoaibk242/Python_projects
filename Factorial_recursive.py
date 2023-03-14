#recursive function factorial
n=input("Enter a non negative number")
n=int(n)
def factorial(x):
    if x < 1 :
        return 1
    else:
        return (x*factorial(x-1))
print("the factorial of the given number is ",factorial(n))'''
import calc
x=calc.add(6,5)
print(x)
