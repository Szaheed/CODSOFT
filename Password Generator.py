# Password Generator

# input modules which are required
import random

# define data
upper_case= ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower_case=('abcdefghijklmnopqrstuvwxyz')
num= ('0123456789')
symbols= ('!@#$%^&*()[]{}<>')

# input the length of password
length=int(input("Enter the length of password:"))
print(length)

# combine all the data
all=upper_case+lower_case+num+symbols
temp=random.sample(all,length)

# print the password
password="".join(temp)
print("Password is:" + password)
