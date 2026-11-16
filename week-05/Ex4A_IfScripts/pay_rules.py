pay_rate = float(input('Enter your pay rate: '))
hours_worked = float(input('Enter how many hours did you work: '))

if hours_worked <= 40:
    print(f'Gross pay is: { pay_rate * hours_worked}')
else:
    print(f'Gross pay is: { (pay_rate * 40) + ((pay_rate * 1.5) * (hours_worked - 40))}')

