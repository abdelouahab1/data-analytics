# Inputs
pay_rate = float(input('Enter your pay rate: '))
hours_worked = float(input('Enter how many hours you worked: '))
filing_status = input("Enter your filing status ('single' or 'joint'): ").strip().lower()

# Weekly gross pay (from pay_rules.py, with overtime)
if hours_worked <= 40:
    weekly_gross = pay_rate * hours_worked
else:
    weekly_gross = (pay_rate * 40) + (pay_rate * 1.5 * (hours_worked - 40))

# Annual gross pay (52 weeks in a year)
annual_gross = weekly_gross * 52

# Tax rate based on filing status and annual income
if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print("Filing status must be 'single' or 'joint'.")
    raise SystemExit

# Tax withheld from the WEEKLY pay, then net pay
tax_withheld = weekly_gross * tax_rate
net_pay = weekly_gross - tax_withheld

# Output
print(f'You worked {hours_worked} hours this period.')
print(f'Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross:.2f}')
print(f'Your filing status is {filing_status}')
print(f'Your tax withholding for the week is ${tax_withheld:.2f}')
print(f'Your net pay is ${net_pay:.2f}')