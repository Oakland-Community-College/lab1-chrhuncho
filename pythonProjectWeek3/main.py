#Project 1
#Chris Cooper



print('Welcome to Fence Calculator Wizard')
print('Lets start with the dimensions of your fence')
#function to check user input
def check_int(prompt):
    user_input = input(prompt)
    while(True):
        try:
            user_input = int(user_input)
        except:
            print ("Input not recognized. Please enter an integer")
            user_input = input(prompt)
        if user_input < 0:
            print ("Cannot have a negative dimension. Please enter an integer.")
            user_input = input(prompt)
        else:
            return user_input

#user puts information such as length, width, and cost of fence
length = check_int("What is the length of your fence in feet?\n")
width = float(input("What is the width of your fence in feet?\n"))
post_distance = float(input("How far apart (in inches) do you want your posts to be?\n"))
print('Ok, can we now calculate how much of supplies you will need')
#user chooses how much of fence boarding to set price
boards = float(input("Please choose how many boards you will need:\n"))
#calcuating cost of fence
price = float(input("Please enter price of fence per foot\n"))
print ("The total cost of your fence is $" + str(boards*(length + width * post_distance)*price) + ".")
print('Thank you for using Fence Calculator Wizard')

