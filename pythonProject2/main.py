#Chris Cooper
#Lab 4 - Function
import random
import math
#User will create a random # generator, add numbers such as 1 through 5.
def affirmation_generator():
    number = random.randint(1, 5)
    if number == 1:
        print("Everything is going to be ok. Keep up the good work.")
    elif number == 2:
        print("Hard times never last forever.")
    elif number == 3:
        print("I am liberating myself from fear, judgment, and doubt.")
    elif number == 4:
        print("My body is healthy, my mind is brilliant, and my soul is tranquil.")
    else:
        print("My time is just around the corner.")
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()

#Lab 4 - Quadratic Function Calculator
def quadratic_equation_intercept_finder(a,b,c):
    determinant =b**2 - 4 * a * c

    if determinant < 0:
        return "No intercepts have been found."
    if determinant > 0:
        return "Intercepts have been found."

    first_x_intercept =(-b + math.sqrt(determinant)) / (2 * a)
    second_x_intercept = (-b - math.sqrt(determinant)) / (2 * a)

    return "x intercepts of " + str(first_x_intercept) + " and " + str(second_x_intercept)
#User puts in numbers here
a = float(input("Please put in value for a\n"))
b = float(input("Please put in value for b\n"))
c = float(input("Please put in value for c\n"))
result = quadratic_equation_intercept_finder(a,b,c)
print(result)
