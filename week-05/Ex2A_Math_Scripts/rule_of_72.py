savings = 45000
intrest_rate = 4
year = 72 / intrest_rate
total = savings * ((1 + (0.04)) ** 18 )

print(f'Your current savings is {savings} $')
print(f'At a {intrest_rate}% interest rate, your savings account will be worth {total:,.2f} in {year} years')


