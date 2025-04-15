#normal gcd without function
a = 60
b = 48

while b!=0:
    temp = a%b
    a = b 
    b = temp

print(a)