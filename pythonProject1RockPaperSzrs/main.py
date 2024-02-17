# Kevin Power 01/30/2024
# Program to show working of two functions - affirmation generator and
# quadratic equation solver
# Need to import math and random libraries

import math
import random


# Pseudo code for affirmation generator function
# affirmations = string array["affirmation1, ... affirmation5"]
# index = random(0,4)
# print affirmations[index]

def affirmation_generator():
    affirm = ["You rock!", "Stay positive!", "Just do it", "I am free", "Peace is mine"]
    affirm_number = random.randint(0, 4)
    print("Your affrimation for the day:\n")
    print(affirm[affirm_number], "\n")


# Quadratic function solver that accepts values for a, b, c
# for quadratic equation ax^2 + bx + c = 0 and
# calculates the x intercepts. If no solution, return message saying don't exist
# Quadratic formula will work for any non zero real value of a
# There are no solutions if the discriminant is less than 0

# Pseudo code for function
# If a = 0
#   quit program
# If b^2 - 4ac is negative
#   return "no solution"
# else
#   calculate square root of b^2 - 4ac
# first x intercept = (-b + square root (b^2-4ac)) / 2a
# second x intercept = (-b - square root (b^2-4ac)) / 2a
# return intercepts

def quadratic_equation_intercept_finder(a, b, c):
    if a == 0:
        print("You must enter a non zero value for a")
        quit()

    discriminant = math.pow(b, 2) - 4 * a * c

    if discriminant < 0:
        return ("There is no solution to the quadratic equation")
    else:
        root_dis = math.sqrt(discriminant)

    first_x_intercept = (-1 * b + root_dis) / (2 * a)
    second_x_intercept = (-1 * b - root_dis) / (2 * a)

    return (first_x_intercept, second_x_intercept)


# Pseudo code for main program
# Call affirmation generator
# Prompt user to enter a,b,c
# result = return from quadratic_equation_intercept_finder function
# if result is a string
#   print out no solution
# else
#   print out tuple representing soultions to the quadratic equation

affirmation_generator()
a = float(input("Enter a value for a > "))
b = float(input("Enter a value for b > "))
c = float(input("Enter a value for c > "))
result = quadratic_equation_intercept_finder(a, b, c)

if isinstance(result, str):
    print(result)
else:
    print("First x intercept:", f"{result[0]:.3f}")
    print("Second x intercept:", f"{result[1]:.3f}")