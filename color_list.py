'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''
from datetime import date
s_date=date(2014,7,2)  # to store starting date 
e_date=date(2014,7,11) # to store end date
difference=e_date-s_date
print("The number of days between the dates is ",difference)