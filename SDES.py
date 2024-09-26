P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8  = (6, 3, 7, 4, 8, 5, 10, 9)
IP = (2, 6, 3, 1, 4, 8, 5, 7) # Initial Permutation
EP = (4, 1, 2, 3, 2, 3, 4, 1) # Extended Permutation
P4 = (2, 4, 3, 1)

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]


def generate_inverse_IP(IP):
      inverse_IP = [0] * len(IP)
      for i, val in enumerate(IP):
          inverse_IP[val - 1] = i + 1
      return inverse_IP 

def XOR(bits, key):
    result = ''
    for i in range(len(bits)):
        if bits[i] == key[i]:
            result += '0'
        else:
            result += '1'
    return result

def permutate(key, P):
    return ''.join(key[i-1] for i in P)

def left_half(bits):
    return bits[:len(bits)//2]

def right_half(bits):    
    return bits[len(bits)//2:]

def shift(bits,no_of_shift):
      rotated_left_half = left_half(bits)[no_of_shift:] + left_half(bits)[:no_of_shift]
      rotated_right_half = right_half(bits)[no_of_shift:] + right_half(bits)[:no_of_shift]
      return rotated_left_half + rotated_right_half

# key generation
def key1(key):
    k1 = permutate(shift(permutate(key, P10),1),P8)
    return k1

def key2(key):
    k2 = permutate(shift(permutate(key, P10),3),P8)
    return k2

def Sbox(bit,S):
     row = int(bit[0] + bit[3], 2)
     col = int(bit[1] + bit[2], 2)
     return format(S[row][col],'02b')

def f_k(bits,key):
     L = left_half(bits)
     R = right_half(bits)
     after_EP = permutate(R,EP)
     first_xor = XOR(after_EP, key)
     s0s1 = Sbox(left_half(first_xor),S0) + Sbox(right_half(first_xor),S1)
     after_P4 = permutate(s0s1, P4)
     second_xor = XOR(after_P4, L)
     return second_xor 

# encryption
def encryption(plaintext):
      after_IP = permutate(plaintext, IP)
      # Round 1
      temp1 = f_k(after_IP, k1)
      bits = right_half(after_IP) + temp1
      # Round 2
      temp2 = f_k(bits,k2)
      inverse_IP = generate_inverse_IP(IP)
      cipher = permutate(temp2 + temp1, inverse_IP)
      return cipher

# decryption
def decryption(ciphertext):
     after_IP = permutate(ciphertext, IP)
     # Round 1
     temp1 = f_k(after_IP,k2)
     bits = right_half(after_IP) + temp1
     # Round 2
     temp2 = f_k(bits,k1)
     inverse_IP = generate_inverse_IP(IP)
     plain = permutate(temp2 + temp1, inverse_IP)
     return plain


# SID = 1910977114
# Key = 109
# PT = 114

key = format(109,'010b')
print("Key : ", key)

k1 =  key1(key)
k2 =  key2(key)

print('K1 : ', k1)
print('K2 : ', k2)

plaintext = format(114,'08b')
ciphertext = encryption(plaintext)

print('PlainText : ',plaintext)
print('CipherText : ',ciphertext)

recovered_plaintext = decryption(ciphertext)
print("Recovered plaintext : ",recovered_plaintext)