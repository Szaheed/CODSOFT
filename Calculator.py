# Simple Calculator

# input the data
First_number=int(input("Enter First Number:"))
Second_number=int(input("Enter Second Number:"))
operator=input('Select Operator: +, -, *, /:')

# if-else statement to perform operations
if operator == '+':
    print(First_number + Second_number)
elif operator == '-':
        print(First_number - Second_number)
elif operator == '*':
    print(First_number * Second_number)
elif operator == '/':
    print(First_number / Second_number)
else:
    print("Invalid Operator")





