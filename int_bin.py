#18.Write a Python program to convert an integer to binary keep leading zeros.
def leadzero(x):
  str1=str(x)
  z=""
  for i in str1:
   if i == '0':
     z=z+i #to add zero into a empty string 
   else:
     break
  return z
def int_bin(x):
    str2=leadzero(x)
    x=int(x)
    str1=""
    while x > 0:
      rem =(x % 2) # to store remainder 
      x = x // 2   # floor division operator
      rem=str(rem)
      str1+=rem    # to concatenate remainder into a string
    str1=str1[::-1]
    return str2+str1
z=input("enter decimal number")
print(int_bin(z))
y=input()