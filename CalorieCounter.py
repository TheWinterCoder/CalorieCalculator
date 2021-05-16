"""
@Author: TheWinterCoder
@time: 16/05/2021 15:14
"""

from Functions import calc_schofield_multiplier
from Functions import calc_schofield_calories

height = ''
while True:
    try:
        height = float(input('Please enter your height in cms: '))
    except ValueError:
        print('Sorry, the height you entered is invalid. Please enter a valid number')
        continue
    else:
        break

weight = ''
while True:
    try:
        weight = float(input('Please enter your weight in kgs: '))
    except ValueError:
        print('Sorry, the weight you entered is invalid. Please enter a valid number')
        continue
    else:
        break

age = ''
while True:
    try:
        age = int(input('Please enter your age: '))
    except ValueError:
        print('Sorry, the age you entered is invalid. Please enter a valid number')
        continue
    else:
        break

gender = ''
while True:
    try:
        gender = input('Please enter your gender (male or female): ')
    except ValueError:
        print('Sorry, the gender you inputted was invalid')
        continue
    if gender.lower() != 'male' and gender.lower() != 'female':
        print('Sorry, the gender you inputted was invalid')
        continue
    else:
        break

occupation_activity = ''
while True:
    try:
        occupation_activity = int(input('Please enter your occupational activity level, 1 for light, 2 for moderate,'
                                        '3 for heavy: '))
    except ValueError:
        print('Sorry, the value you entered is invalid. Please enter a valid number')
        continue
    if occupation_activity < 1 or occupation_activity > 3:
        print('Sorry, the value you entered is invalid. Please enter a valid number')
        continue
    else:
        break

non_occupation_activity = ''
while True:
    try:
        non_occupation_activity = int(input('Please enter your non-occupational activity level, 1 for light, '
                                            '2 for moderate, 3 for heavy: '))
    except ValueError:
        print('Sorry, the value you entered is invalid. Please enter a valid number')
        continue
    if non_occupation_activity < 1 or non_occupation_activity > 3:
        print('Sorry, the value you entered is invalid. Please enter a valid number')
        continue
    else:
        break


schofield_multiplier = calc_schofield_multiplier(gender, occupation_activity, non_occupation_activity)

schofield_calories = calc_schofield_calories(gender, age, weight, schofield_multiplier)

print('Your daily calorie intake according to Schofield is ' + str(schofield_calories))
input('Press enter to close: ')
