# Experiment 1
# Implement and Compare Classical Encryption Techniques

import string

# ---------------- Caesar Cipher ---------------- #

def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result


# ---------------- Vigenere Cipher ---------------- #

def generate_key(text, key):
    key = key.upper()
    new_key = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += ch

    return new_key


def vigenere_encrypt(text, key):
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

plain = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

table = dict(zip(plain, key))


def mono_encrypt(text):
    cipher = ""
    for ch in text:
        if ch.isalpha():
            cipher += table[ch]
        else:
            cipher += ch
    return cipher


# ---------------- Main Program ---------------- #

plaintext = input("Enter Plaintext: ").upper()

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

print("\n================ SAMPLE OUTPUT / RESULT ================\n")

print("Plaintext")
print(plaintext)

print("\nCaesar Cipher")
print("Shift Key:", shift)
print("Ciphertext:", caesar)

print("\nVigenère Cipher")
print("Keyword:", keyword)
print("Ciphertext:", vigenere)

print("\nRail Fence Cipher")
print("Rails:", rails)
print("Ciphertext:", rail)

print("\nMonoalphabetic Cipher")
print("Key:")
print(key)
print("Ciphertext:")
print(mono)

print("\nFrequency Analysis")

print("{:<20}{}".format("Cipher", "Resistance"))
print("-" * 35)
print("{:<20}{}".format("Caesar", "Very Low"))
print("{:<20}{}".format("Rail Fence", "Low"))
print("{:<20}{}".format("Monoalphabetic", "Medium"))
print("{:<20}{}".format("Vigenère", "High"))
