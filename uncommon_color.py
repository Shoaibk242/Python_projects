'''def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()'''
def details(n,a,ad):
    print("Name:{}\n Age:{}\nAddress:{}".format(n,a,ad))
name=input("Enter your Name")
age=input("Enter your age")
address=input("Enter your Address")
print("Your details are ",details(name,age,address))