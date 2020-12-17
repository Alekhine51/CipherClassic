#!/usr/bin/python3

# Simple Caesar Cipher

import string

plaintext = input("Enter plaintext or path to plaintext file:")
#add file access later

mod = input("Enter shift number):")

numbers = list(plaintext)

for number in range(len(numbers)):
    numbers[number] = string.ascii_lowercase.index(numbers[number])

for number in range(len(numbers)):
        numbers[number] = (numbers[number] + mod) % 26

print(numbers)
