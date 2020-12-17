#!/usr/bin/python3

# Simple Caesar Cipher

import string

plaintext = input("Enter plaintext or path to plaintext file:")
#add file access later

mod = input("Enter shift number:")

mod = int(mod)

cipher = list(plaintext)

for number in range(len(cipher)):
    cipher[number] = string.ascii_lowercase.index(cipher[number])

for number in range(len(cipher)):
        cipher[number] = (cipher[number] + mod) % 26

for number in range(len(cipher)):
    cipher[number] += 97
    cipher[number] = chr(cipher[number])

ciphertext = ''

for letter in range(len(cipher)):
    ciphertext += cipher[letter]

print(ciphertext)


