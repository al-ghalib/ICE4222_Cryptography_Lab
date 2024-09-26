def Double(a):
    s = ""
    s += str(int((a // 10)))
    s += str(int((a % 10)))
    return s

def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x

def minusmodulo(a, p):
    while a < 0:
        a += p
    return a

def same(x1, y1, a, i, p):
    ge_point = (0, 0)
    s = ((3 * (x1**2) + a) % p) * (modInverse((2 * y1), p) % p)

    print(f"For Calculating {i}g :")
    print(f"s = 3 * {x1}^2 + {a} / 2 * {y1}")
    print(f"s = {(3 * (x1**2) + a) % p} / {(2 * y1) % p} mod({p})")
    print(f"So, s = {s % p}")

    ge_point = (
        (s**2 - 2 * x1) % p,
        (-y1 + (s * (x1 - ge_point[0])) % p) % p
    )
    
    print(f"x{i}g = {s**2 % p} - 2 * {x1}")
    print(f"So, x{i}g = {ge_point[0]} mod ({p})")
    
    print(f"y{i}g = -{y1} + {s} * {x1 - ge_point[0]}")
    print(f"So, y{i}g = {ge_point[1]} mod ({p})")
    
    ge_point = (minusmodulo(ge_point[0], p), minusmodulo(ge_point[1], p))
    
    print(f"Hence {i}G = ({ge_point[0]}, {ge_point[1]})\n")
    
    return ge_point

def different(x1, y1, x2, y2, i, p):
    ge_point = (0, 0)
    s = ((y2 - y1) * modInverse((x2 - x1), p)) % p
    
    print(f"For Calculating {i}g :")
    print(f"s = ( {y2 - y1} / {x2 - x1} )^2 mod({p})")
    print(f"So, s = {s % p}")

    ge_point = (
        (s**2 - x1 - x2) % p,
        (-y1 + (s * (x1 - ge_point[0])) % p) % p
    )
    
    print(f"Now x{i}g = {s**2 % p} - {x1} - {x2} mod({p})")
    print(f"So, x{i}g = {ge_point[0]}")
    
    print(f"Now y{i}g = -{y1} + {s * (x1 - ge_point[0])} mod({p})")
    print(f"So, y{i}g = {ge_point[1]}")
    
    print(f"Hence {i}G = ({ge_point[0]}, {ge_point[1]})\n")
    
    if x1 == ge_point[0]:
        print(f"For Calculating {i}g : (0)\n")
        print("Ans to the Q Number 03 : \n")
        print(f"Value of n is : {i + 1}")
        exit(1)
    
    return ge_point

def main():
    roll = input("My roll number is: ")
    
    print("\nAns to the Q Number 01 :")
    print(f"Here p = {roll[0]}{roll[1]}, a = {roll[4]}, b = {roll[9]}")
    
    p = int(roll[0]) * 10 + int(roll[1])
    a = int(roll[4])
    b = int(roll[9])
    
    rhs = []
    lhs = []
    
    print(f"So, our elliptic curve is E{p}({a},{b}).")
    print(f"The equation of elliptic curve: y^2 = x^3 + {a}x + {b}")
    print(f"y^2 = x^3 + {a}x + {b}  where a = {a} and b = {b}\n")
    
    print("  x              RHS              y              LHS")
    
    for x in range(p):
        rhs.append((x**3 + a * x + b) % p)
        lhs.append((x**2) % p)
        print(f" {Double(x)}              {Double(rhs[x])}              {Double(x)}              {lhs[x]}")
    
    x1, y1 = 69, 0
    
    print("\nAll the affine points are:")
    
    for i in range(p):
        for j in range(p):
            if rhs[i] == lhs[j]:
                if x1 == 69:
                    x1, y1 = i, j
                print(f"({i},{j}), ", end="")
    
    print(f"\n\nAns to the Q Number 02 :")
    print(f"Generator point is: ({x1},{y1})\n")
    
    i = 2
    ge_point = same(x1, y1, a, i, p)
    
    while True:
        i += 1
        ge_point = different(x1, y1, ge_point[0], ge_point[1], i, p)

if __name__ == "__main__":
    main()
