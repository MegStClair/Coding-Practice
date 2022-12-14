##### EASY #####
""" WARM UP
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


''' DAY 1
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


''' DAY 2
Task:
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


''' DAY 3
Task:
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
'''

if __name__ == '__main__':
    N = int(input().strip())

    if N % 2:
        print("Weird")
    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    if (N % 2 == 0) and 2 <= N <= 5:
        print("Not Weird")
    # If n is even and in the inclusive range of 6 to 20, print Weird
    if (N % 2 == 0) and 6 <= N <= 20:
        print("Weird")
    # If n is even and greater than 20, print Not Weird
    if (N % 2 == 0) and N > 20:
        print("Not Weird")

''' DAY 4
Task:
Write a Person class with an instance variable, age , and a constructor that takes an integer, initialAge , as a parameter. 
The constructor must assign initalAge to age after confirming the argument passed as initialAge is not negative; 
if a negative argument is passed as initalAge, the constructor should set age to 0 and print Age is not valid, setting age to 0.. 
In addition, you must write the following instance methods:

1. yearPasses() should increase the age instance variable by 1.
2. amIOld() should perform the following conditional actions:
    If age < 13, print You are young..
    If  age >= 13 and age < 18, print You are a teenager..
    Otherwise, print You are old..
'''

class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")
        else: 
            self.initialAge = initialAge
            
    def amIOld(self):
        if self.initialAge < 13:
            print("You are young.")
            
        elif self.initialAge < 18:
            print("You are a teenager.")
            
        else:
            print("You are old.")
            
    def yearPasses(self):
        self.initialAge += 1


'''DAY 5
Task:
Given an integer, n, print its first 10 multiples. 
Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.'''

if __name__ == '__main__':
    n = int(input().strip())

for i in range(1, 11):
    res = (n * i)
    print(n, "x", i,"=", res)


''' DAY 6
Task:
Given a string, s, of length n that is indexed from 0 to n -1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example:
s = adbecf
Print abc def

Input Format:
The first line contains an integer, t (the number of test cases).
Each line i of the t subsequent lines contain a string, s.'''

t = int(input()) 

for x in range(t):
    s = input()
    n = len(s)

    evens = ''
    odds = ''
        
    for i in range(n):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]
            
    print(f'{evens} {odds}')


''' DAY 7
Task:
Given an array, a, of n integers, print a's elements in reverse order as a single line of space-separated numbers.

Example:
a = [1, 2, 3, 4]
Print 4 3 2 1. Each integer is separated by one space.

Input Format:
The first line contains an integer, n (the size of our array).
The second line contains arr, n space-separated integers that describe array a's elements.'''

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
for i in reversed(arr):
    print(f'{i} ', end='')
    
    