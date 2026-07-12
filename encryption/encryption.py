# Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

# print(f"Chars: {chars}")
# print(f"Keys: {keys}")

# Encryption
plain_text = input("Enter a text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")

# Decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {cipher_text}")
print(f"Original Message: {plain_text
                           }")