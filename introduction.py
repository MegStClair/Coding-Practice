##### EASY #####
""" 
Task:
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format: A single line containing a positive integer, .

Output Format: Print Weird if the number is weird. Otherwise, print Not Weird. """

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2:
        print("Weird")
    elif 2 <= n <= 5: 
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


'''
Task:
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. 
Round the result to the nearest integer.
'''

def solve(meal_cost, tip_percent, tax_percent):
    
    tip_amount = (tip_percent/100) * meal_cost
    tax_amount = (tax_percent/100) * meal_cost
    
    total = meal_cost + tip_amount + tax_amount
    
    print(round(total))


'''
Task
Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:

1. Declare  variables: one of type int, one of type double, and one of type String.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the  operator to perform the following operations:
4. Print the sum of  plus your int variable on a new line.
5. Print the sum of  plus your double variable to a scale of one decimal place on a new line.
6. Concatenate  with the string you read as input and print the result on a new line.
'''
# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank '
# Read and save an integer, double, and String to your variables.
a = int(input())
b = float(input())
c = input()
# Print the sum of both integer variables on a new line.
print(i + a)
# Print the sum of the double variables on a new line.
print(d + b)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + c)