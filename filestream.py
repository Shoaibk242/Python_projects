'''20.Write a Python program to write all file content into new file by skipping line 5 from the following
file:
i=open("test1.txt","w")
i.close()'''
# open file in read mode
fn = open('test1.txt', 'r')
# open other file in write mode
fn1 = open('test2.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
	if (i < 4):
		fn1.write(cont[i])
	elif (i > 4):
		fn1.write(cont[i])
	else:
		pass

# close the file
fn1.close()

# open file in read mode
fn1 = open('test2.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()


















