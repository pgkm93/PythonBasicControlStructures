#Tute dude
#Assignment 2

# Task - 1
# Checking Even or Odd number

#Taking input from the user
numbers = float(input("Enter the number:"))

# using if condition to find numbers is even or odd
if numbers % 2 == 0:
    print(f"{numbers} is an even number.")
else:
    print(f"{numbers} is an odd number.")


#Task -2
# Sum of integers from 1 to 50 using a loop

for _ in range(1,51):
    # Using range 1,51 to sum but number 51 is not include
    total_sum = sum(range(1,51))
    print(f"the sum of numbers from 1 to 50 is :{total_sum}")
    break



