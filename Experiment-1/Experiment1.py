# ============================================================
# Experiment 1
# Classical Encryption Techniques
# Caesar Cipher, Vigenere Cipher,
# Rail Fence Cipher, Monoalphabetic Cipher
# ============================================================

import string

ALPHABET = string.ascii_uppercase
SUBSTITUTION_KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"


# ---------------- Caesar Cipher ---------------- #

def caesar_encrypt(text, shift):
    cipher = ""

    for ch in text.upper():
        if ch.isalpha():
            cipher += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            cipher += ch

    return cipher


# ---------------- Vigenere Cipher ---------------- #

def generate_key(text, key):
    key = key.upper()
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            result += key[j % len(key)]
            j += 1
        else:
            result += ch

    return result


def vigenere_encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)

    cipher = ""

    for p, k in zip(text, key):
        if p.isalpha():
            cipher += chr((ord(p) + ord(k) - 130) % 26 + 65)
        else:
            cipher += p

    return cipher


# ---------------- Rail Fence Cipher ---------------- #

def rail_fence_encrypt(text, rails):
    text = text.upper()

    fence = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


# ---------------- Monoalphabetic Cipher ---------------- #

encrypt_table = dict(zip(ALPHABET, SUBSTITUTION_KEY))


def mono_encrypt(text):
    cipher = ""

    for ch in text.upper():
        if ch.isalpha():
            cipher += encrypt_table[ch]
        else:
            cipher += ch

    return cipher


# ---------------- Main Program ---------------- #

plaintext = input("Enter Plaintext : ").upper()

# Caesar
shift = 3
caesar = caesar_encrypt(plaintext, shift)

# Vigenere
keyword = "LEMON"
vigenere = vigenere_encrypt(plaintext, keyword)

# Rail Fence
rails = 3
rail = rail_fence_encrypt(plaintext, rails)

# Monoalphabetic
mono = mono_encrypt(plaintext)

print("\n")
print("=" * 55)
print("           SAMPLE OUTPUT / RESULT")
print("=" * 55)

print("\nPlaintext")
print(plaintext)

print("\nCaesar Cipher")
print("Shift Key :", shift)
print("Ciphertext :", caesar)

print("\nVigenere Cipher")
print("Keyword :", keyword)
print("Ciphertext :", vigenere)

print("\nRail Fence Cipher")
print("Rails :", rails)
print("Ciphertext :", rail)

print("\nMonoalphabetic Cipher")
print("Key :")
print(SUBSTITUTION_KEY)
print("Ciphertext :", mono)

print("\nFrequency Analysis")
print()

print("{:<20}{}".format("Cipher", "Resistance"))
print("-" * 35)
print("{:<20}{}".format("Caesar", "Very Low"))
print("{:<20}{}".format("Rail Fence", "Low"))
print("{:<20}{}".format("Monoalphabetic", "Medium"))
print("{:<20}{}".format("Vigenere", "High"))

print("\nExperiment Completed Successfully.")
