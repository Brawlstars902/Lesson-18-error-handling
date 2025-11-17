try:
    print('This program is to confirm wether your age ables you to drive a car in Singapore.')
    x=int(input('Please enter your age:  '))
    if x >= 18:
        print('You are old enough to drive a car in Singapore.')
    else:
        print('You are too young to drive a car in Singapore.')
except ValueError:
    print('Something went wrong! Make sure you have entered a number.')
finally:
    print('If these age restrictions aren\'t taken seriously, there will be severe consequences.')