# lab 5

year_input = 0
month_input = 0
day_input = 0

def day_function(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 28

while True:
    try:
        year_input = int(input('Please enter a year between 2024 and 2099:'))
    except:
        print('Please enter a valid year.')
    if year_input < 2024 or year_input > 2099:
        print('Please enter a valid year.')
    else:
        break

while True:
    try:
        month_input = int(input('Please enter a month between 1 and 12:'))
    except:
        print('Please enter a valid month.')
    if month_input < 1 or month_input > 12:
        print('Please enter a valid month.')
    else:
        break

while True:
    try:
        day_input = int(input('Please enter a day between 1 and 31'))
    except:
        print('Please enter a valid amount of days')
    month_valid = day_function(month_input)
    if day_input > month_valid:
        print('Day amount exceeds the month selected')
    else:
        break



def day_calc():
    current_day = 11
    current_month = 2
    current_year = 2024
    calc_full_year = (year_input - current_year) * 365
    day_valid = day_function(month_input)
    calc_day = day_valid -day_input
    month_calc = month_input *30.44
    total_day = calc_full_year + calc_day + month_calc
    print(total_day)

day_calc()