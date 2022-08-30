"""
Input a dog's age in human years: 15
The dog's age in dog's years is 73
"""

a=int(input("enter the value of age of human: ")) #use input function, make sure input is an integer

if a<3:
    d = int(a*10.5)                               #if else function
else:
    d=2*10.5 + (a-2)*4
print("the value you already entered is ",int(d))


"""
Input the name of Month: February
No. of days: 28/29 days 
"""

month_name = input("Enter each month of the year: ") # such as January February...

if month_name == "January" or month_name == "March" or month_name == "May" or month_name == "July" or month_name == "August" or month_name == "October" or month_name== "December":   
    month_days = 31
    
elif month_name == "February" :
    month_days = "28 / 29"
    
elif month_name == "April" or month_name == "June" or month_name == "September" or month_name == "November":
    month_days = 30

else:
    print("wrong input!") 

print(month_days, "days")




#I relized that I could shorten my code as below

month_name = input("Enter the name of Month: ") # such as January February...

month_name = month_name.lower()    #learn a new function on line, user no need to pay attention to the input case

if month_name == "february" :
    print("No. of days 28 / 29 days") 
elif month_name == "april" or month_name == "june" or month_name == "september" or month_name == "november":
    print("No. of days: 30 days")
else:
    print("No. of days: 31 days")  #it works, exciting




"""
Write a Python program to check a string represent an integer or not.
Your program should look as follows:
Input a string: Python
The string is not an integer.
"""


str = input('Enter any value: ')  #use "".isdigit" function to determine "integer"
if str.isdigit():
    print('The string is an integer')
else:
    print('The string is not an integer')



"""
Write a Python program that takes 10 numbers as input from user and find their sum and average.
"""

i = 0                  #learn "loop" function 
total = 0
while i <= 10:
    total = total + i    #total add next number
    average = total / 10
    i += 1
print(f'Sum of the Integers is {total}')
print(f'Average of the Integers is {average}')


"""
Enter an Integer number (Table to be calculated): 15
 15 X 1 = 15
...
...
...
15 X 10 = 150
"""


num = int(input("enter the number= "))  #use "loop" function
i = 1

while i<=10:
    print(num, "X", i, "=", num * i)
    i = i+1
