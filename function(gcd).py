#gcd of numbers
def gcd(a,b):
    while b!=0:
        temp = a%b
        a = b 
        b = temp
    return a
        
print(gcd(60,48))

