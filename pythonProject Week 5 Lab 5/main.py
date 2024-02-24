#Lab 5
#Chris Cooper
print("Hello, this program will be asking you the month, date, and year.")
print("Make sure that numbers are within validation range")
#End user puts in data
#Created a function that validates user input and takes user input
while True:
    month=int(input("How much months would you like to go in the future?.(Current month is 02/February) \n"))
    day=int(input("How much days would you like to go in the future?.(Current day is 16) \n"))
    year=int(input("How many years would you like to go in the future?.(Current year is 2024) \n"))
    if (month >= 1 and month <=8 and
        day >= 1 and day <= 14 and
        year >= 1 and year <= 99):
        print('Data is correct')
        break
    else:
        print('Data is incorrect. Please re-enter.')
print('The program below will now calculate the date')
#Created a function that takes user input and then calcualtes what the future date will be.
def future_date_calculator():
    current_month = 2
    current_day = 16
    current_year = 2024
    calculated_day = current_day + day
    calculated_month = current_month + month
    calculated_year = current_year + year
    print(f"Your date is {calculated_month},{calculated_day},{calculated_year}")
    print(f"You have {month} months, {day} days, and {year} years until then.")
future_date_calculator()