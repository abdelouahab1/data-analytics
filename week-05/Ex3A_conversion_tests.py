# Description: This script tests various numeric conversion techniques
# Author: Abdelouahab Bendanoune

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a = float(a)
b = int(b)
# c = int(c) it gives an error because we can't convet the string Stevens to integer.
# d = int(d) it gives an error because we can't convet the string Stevens to integer.
a = int(float(a))
c_number = int(c[0:3])
d_number = int(d[7:8])

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(c_number, type(c_number))
print(d_number, type(d_number))
print(d, type(d))