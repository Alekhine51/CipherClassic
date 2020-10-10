# CipherClassic
A suite of CLI classical encryption tools. This repo is intended as a resource for students of cryptography. Each file is a self-contained encryption tool with comments explaining how it works, and are written in Python, without Libraries. Python was chosen since it's a very common language.

List of tools:

Caesar Shift (Monoalphabetic substitution cipher)

Vignere Cipher (Polyalphabetic substitution cipher)

Enigma Machine emulator

Simple frequency analyzer to crack whatever encryptions you make. The program comes with tables of the most common letters in multiple languages, and will attempt to crack any ciphertext by outputting it's 'guess' at the cipher alphabet as a text file in the present working directory, and it's decrypted text. You'll have to help it along by filling in the gaps. In the future it will intelligently crack the cipher without as much user hand-holding.

If you're curious about the history of these ciphers, I recommend Simon Singh's *The Code Book*.
