def lower(key):
    key = key.lower()
    key.replace('j','i')
    return key

def remove_space(plaintext):
    text = ""
    for i in plaintext:
        if i != " ":
            text += i
    return text

def generate_key_square(key,letters):
    key_list = []
    for i in key:
        if i not in key_list:
            key_list.append(i)
    for i in letters:
        if i not in key_list:
            key_list.append(i)
    matrix = []
    while key_list != []:
        matrix.append(key_list[:5])
        key_list = key_list[5:]
    return matrix

letters = "abcdefghiklmnopqrstuvwxyz"
key = input("Enter the key : ")
key = lower(key)
matrix = generate_key_square(key,letters)

#encryption
def repeat_letter(text):
    for i in range(len(text)-1):
        if text[i] == text [i+1]:
            temp = i
            break
    return text[:i+1]+'x'+text[i+1:]

def get_coord(char1, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char1:
                return i,j

def encryption(plaintext):
    ciphertext = ""
    plaintext = remove_space(lower(plaintext))
    plaintext = repeat_letter(plaintext)
    if len(plaintext) % 2 != 0:
        plaintext += 'x'
    print(plaintext)
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1]
        row1, col1 = get_coord(char1,matrix)
        row2, col2 = get_coord(char2,matrix)
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

plaintext = input("Enter the input message : ")
ciphertext = encryption(plaintext)
print("Ciphertext : ",ciphertext)


#decryption
def decryption(ciphertext):
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        
        row1, col1 = get_coord(char1,matrix)
        row2, col2 = get_coord(char2,matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:
           plaintext += matrix[row1][col2] + matrix[row2][col1]
    plaintext = plaintext.replace('x','')
      
    return plaintext

recoveredtext = decryption(ciphertext)
print("PlainText : ",recoveredtext)
