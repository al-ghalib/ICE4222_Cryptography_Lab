def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def countPrimitiveRoots(p):
    result = 1
    for i in range(2, p, 1):
        if (gcd(i, p) == 1):
            result += 1
    return result
 
 
p = 191
print(countPrimitiveRoots(p-1))
 