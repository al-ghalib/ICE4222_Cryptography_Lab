def is_primitive_root(a, n):
    residues = set()
    for powers in range(1, n):
        residues.add(pow(a, powers, n))
    return len(residues) == n - 1


def find_primitive_roots(n):
    primitive_roots = []
    for a in range(1, n):
        if is_primitive_root(a, n):
            primitive_roots.append(a)

    return primitive_roots


n = int(input("Enter value of n: "))

primitive_roots = find_primitive_roots(n)
print("Primitive roots of n:", primitive_roots)
