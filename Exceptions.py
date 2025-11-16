try:
    x=int(input('Please enter your age:  '))
    y=2*x
    print('Double your age is',y,)
except ValueError:
    print('Something went wrong. Please try again.')