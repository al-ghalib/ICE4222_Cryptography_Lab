def caesar_bruteforce(ciphertext):
    for shift in range(26):
        plaintext = ""
        for char in ciphertext:
            if char == " ":
                plaintext += char
            else:
                shifted_char = chr((ord(char) - shift - 128) % 128) 
                plaintext += shifted_char

        print(f"Shift {shift}: {plaintext}")

# Example usage
ciphertext = "Kl$ Wklv lv Degxoodk Do Jkdole1 L dp d vwxghqw ri LFH1 L dp ohduqlqj Fu|swrjudsk|1"
caesar_bruteforce(ciphertext)