import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

    
def mod_inverse(e, phi_n):
    for d in range(3, phi_n):
        if(d * e) % phi_n == 1:
            return d
    raise ValueError("Mod Inverse does not exist")


"""Generate public and private key"""
def generate_keypair():
    p = generate_prime(1000, 5000)
    q = generate_prime(1000, 5000)
    while p == q:
        q = generate_prime(1000, 5000)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_n - 1) 
    while gcd(e, phi_n) != 1:   
        e = random.randint(3, phi_n - 1)

    d = mod_inverse(e, phi_n)

    return (p, q, phi_n, (e, n), (d, n))


def encrypt(msg, e, n):
    # Encrypt each character to an integer
    cipher_msg = [pow(ord(c), e, n) for c in msg]
    return cipher_msg

def decrypt(cipher_msg, d, n):
    # Decrypt each integer back to a character
    plain_msg = ''.join([chr(pow(c, d, n)) for c in cipher_msg])
    return plain_msg


# public_key = (50851, 18973)
# private_key = (50851, 18037)
p, q, phi_n, public_key, private_key = generate_keypair()

print("\n")
msg = "Abdullah Al Ghalib"
# msg = input("Enter your message : ") 
encrypted_msg = encrypt(msg, public_key[0], public_key[1])
decrypted_msg = decrypt(encrypted_msg, private_key[0], private_key[1])

print("\n")

print("Public Key : ", public_key)
print("Private Key : ", private_key)
print("n : ", p * q)
print("Phi_n : ", phi_n)
print("p : ", p)
print("q : ", q)

print("Encrypted Message : ", encrypted_msg)
print("Decrypted Message : ", decrypted_msg)


