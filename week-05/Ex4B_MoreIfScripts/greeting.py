current_hour = int(input('Enter current hour: '))

if current_hour < 0 or current_hour > 23:
    print('Enter a valid hour between 0-23')
else:
    if current_hour < 10:
        print('Good morning!')
    elif current_hour < 17:
        print('Good day!')
    else:
        print('Good evening!')

    if current_hour >= 23 or current_hour <= 4:
        print('What are you doing up so late??')