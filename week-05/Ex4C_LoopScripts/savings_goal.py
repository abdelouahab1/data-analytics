starting_balance = 30000
goal_balance = 40000
weekly_savings = 1000
treat = 100

while starting_balance < goal_balance:
    starting_balance += weekly_savings
    print(f'This week my balance increased to {starting_balance}')

    if starting_balance > goal_balance / 2:
        print(f'Almost there! This week my balance is up to {starting_balance}')
    if starting_balance >= goal_balance * 0.75:
        starting_balance -= treat
        print(f'So close! After treating myself, my balance is up to {starting_balance}')

print(f'Goal met! My current balance is {starting_balance}')