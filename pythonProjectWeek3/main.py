print('Loading Fence Calculating Program.........')
print('Welcome to Fence Calcualtor Wizard')
print('Lets start with the dimensions of your fence')
#total fence distance is length x width
length = float(input("What is the length of your fence?(in feet)\n"))
width = float(input("What is the width of your fence?(in inches)\n"))
post_distance = float(input("How far apart (in inches) do you want your posts to be?\n"))
print('Ok, can we now calculate how much of supplies you will need')
post_number=length * width
print("Fence Distance is",post_number)

