def encrypt_text(plain_text, shift_key):
    ans = ""
    for i in range(len(plain_text)):
        ch = plain_text[i]
        if ch == " ":
            ans += " "
        else:
            ans += chr((ord(ch) + shift_key - 128) % 128)
    return ans


def decrypt_text(encrypted_ans, shift_key):
    ans = ""
    for i in range(len(encrypted_ans)):
        ch = encrypted_ans[i]
        if ch == " ":
            ans += " "
        else:
            ans += chr((ord(ch) - shift_key - 128) % 128)
    return ans

plain_text = "Hi! This is Abdullah Al Ghalib. I am a student of ICE. I am learning Cryptography."
#plain_text = input("Enter Plain Text : ")
shift_key = int(input("Enter the shifting key : "))

encrypted_ans = encrypt_text(plain_text, shift_key)
decrypted_ans = decrypt_text(encrypted_ans, shift_key)

print(f"Encrypted Cipher Text : {encrypted_ans}")
print(f"Decrypted Original Text : {decrypted_ans}")

