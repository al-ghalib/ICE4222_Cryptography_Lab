import random

def generate_key():
    key = []
    key.extend([x for x in range(ord('0'), ord('9')+1)])
    key.extend([x for x in range(ord('A'), ord('Z')+1)])
    key.extend([x for x in range(ord('a'), ord('z')+1)])
    rev_key = [x for x in key]
    random.shuffle(key)
    mod_key = {}
    demod_key = {}
    for i in range(len(key)):
        mod_key[chr(key[i])] = chr(rev_key[i])
        demod_key[chr(rev_key[i])] = chr(key[i])
    return (mod_key, demod_key)


def monoalphabetic_cipher_modulation(text, key):
    modulated_text = ""
    for c in text:
        if not c in key:
            modulated_text += c
        else:
            modulated_text += key[c]
    return modulated_text


def monoalphabetic_cipher_demodulation(modulated_text, key):
    demodulated_text = ""
    for c in modulated_text:
        if not c in key:
            demodulated_text += c
        else:
            demodulated_text += key[c]
    return demodulated_text


plaintext = "I eat an apple"
mod_key, demod_key = generate_key()
print(mod_key)
print(demod_key)

modulated_text = monoalphabetic_cipher_modulation(plaintext, mod_key)
demodulated_text = monoalphabetic_cipher_demodulation(modulated_text, demod_key)

print(f"plaintext : {plaintext}")
print(f"modulated_text : {modulated_text}")
print(f"demodulated_text : {demodulated_text}")

