try:
    n1,n2=eval(input('Please enter two numbers to divide ( seperate them with a comma ):  '))
    r=n1/n2
    print('The result of this division is',r,'.')
except ValueError:
    print('Error! Please remember to enter a number.')
except SyntaxError:
    print('Error! Please remember to add a comma.')
except ZeroDivisionError:
    print('Error! Please do not make one of your numbers zero.')
else:
    print('Nothing went wrong. Are you satisfied?')
finally:
    print('\n--The Calculator-- Made by Ishaan --')