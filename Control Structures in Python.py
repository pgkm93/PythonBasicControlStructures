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

#variable for the sum
total_count = 0

#loop and sum of all integers in this range
for number in range(1,51):
    total_count += number

#Displays the final sum
print(f"The sum of numbers form 1 to 50 is:{total_count}")


