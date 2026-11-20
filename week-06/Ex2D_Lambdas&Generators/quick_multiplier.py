
# Step 1: Create a doubler
doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler("banana"))


# Step 2: Create a tripler
tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler("banana"))


# Step 3: Create a multiplier function
def multiplier(number):
    return lambda n: n * number


# Step 4: Create multipliers from 4 to 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Step 5: Test all multipliers
print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))
