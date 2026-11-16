# prompt the user to enter 3 numbers
a = float(input('Enter the first number: '))
b = float(input('Enter the first number: '))
c = float(input('Enter the first number: '))

if a > b and a > c:
    if b < c :
        print(f'{a} is the the maximum number, and {b} is the minimum')
    elif c < b:
        print(f'{a} is the the maximum number, and {c} is the minimum')
elif b > a and b > c:
    if a < c :
        print(f'{b} is the the maximum number, and {a} is the minimum')
    elif c < a:
        print(f'{b} is the the maximum number, and {c} is the minimum')
elif c > a and c > b:
    if a < b :
        print(f'{c} is the the maximum number, and {a} is the minimum')
    elif b < a:
        print(f'{c} is the the maximum number, and {b} is the minimum')






