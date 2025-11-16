v=False
while not v:
    try:
        x=int(input('Please enter a number:  '))
        while x%2==0:
            print('Your number is divisible by 2')
    except:
        print('Something went wrong.')
