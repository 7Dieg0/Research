# Research

Recently I start to explore how does Python work, and tried to do some coding through the course as below:

"""Write a Python program to convert month name to a number of days.
Your program should look as follows: 
Input the name of Month: February 
No. of days: 28/29 days"""

month_name = input("Enter each month of the year: ") # such as January February...
#just tried to use "if else" function to coding

if month_name == "January" or month_name == "March" or month_name == "May" or month_name == "July" or month_name == "August" or month_name == "October" or month_name== "December":   
    month_days = 31
    
elif month_name == "February" :
    month_days = "28 / 29"
    
elif month_name == "April" or month_name == "June" or month_name == "September" or month_name == "November":
    month_days = 30

else:
    print("wrong input!") 

print(month_days, "days")

And then, I 

