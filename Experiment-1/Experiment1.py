from collections import Counter
import string

ALPHABET = string.ascii_uppercase

# ---------------- Caesar Cipher ---------------- #

def caesar_encrypt(text, shift):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ---------------- Vigenere Cipher ---------------- #

def generate_key(text, key):
    key = key.upper()
    key_list = []
    j = 0

    for ch in text:
        if ch.isalpha():
            key_list.append(key[j % len(key)])
            j += 1
        else:
            key_list.append(ch)

    return "".join(key_list)


def vigenere_encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)

    cipher = ""

    for t, k in zip(text, key):
        if t.isalpha():
            cipher += chr((ord(t) + ord(k) - 130) % 26 + 65)
        else:
            cipher += t

    return cipher


def vigenere_decrypt(cipher, key):
    key = generate_key(cipher, key)

    text = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            text += chr((ord(c) - ord(k) + 26) % 26 + 65)
        else:
            text += c

    return text


# ---------------- Rail Fence Cipher ---------------- #

def rail_fence_encrypt(text, rails):
    text = text.upper()

    rail = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(rail)


# ---------------- Monoalphabetic Cipher ---------------- #

SUBSTITUTION_KEY = "QWERTYUIOPASDFGHJKLZXCVBNM"

encrypt_map = dict(zip(ALPHABET, SUBSTITUTION_KEY))
decrypt_map = dict(zip(SUBSTITUTION_KEY, ALPHABET))


def mono_encrypt(text):
    text = text.upper()

    return ''.join(
        encrypt_map.get(ch, ch)
        for ch in text
    )


def mono_decrypt(text):
    return ''.join(
        decrypt_map.get(ch, ch)
        for ch in text
    )


# ---------------- Frequency Analysis ---------------- #

def frequency_analysis(text):
    letters = [c for c in text if c.isalpha()]

    count = Counter(letters)

    total = len(letters)

    print("\nLetter Frequency")

    for letter in sorted(count):
        print(f"{letter} : {count[letter]} ({count[letter]/total*100:.2f}%)")


# ---------------- Main Program ---------------- #

plaintext = input("Enter Plaintext: ").upper()

print("\n=========== Caesar Cipher ===========")

shift = 3

caesar = caesar_encrypt(plaintext, shift)

print("Ciphertext :", caesar)
print("Decrypted  :", caesar_decrypt(caesar, shift))

print("\n=========== Vigenere Cipher =========")

keyword = "LEMON"

vig = vigenere_encrypt(plaintext, keyword)

print("Keyword    :", keyword)
print("Ciphertext :", vig)
print("Decrypted  :", vigenere_decrypt(vig, keyword))

print("\n=========== Rail Fence Cipher =======")

rails = 3

rail = rail_fence_encrypt(plaintext, rails)

print("Rails      :", rails)
print("Ciphertext :", rail)

print("\n=========== Monoalphabetic ==========")

mono = mono_encrypt(plaintext)

print("Key        :", SUBSTITUTION_KEY)
print("Ciphertext :", mono)
print("Decrypted  :", mono_decrypt(mono))

print("\n=========== Frequency Analysis ======")

print("\nCaesar")
frequency_analysis(caesar)

print("\nVigenere")
frequency_analysis(vig)

print("\nRail Fence")
frequency_analysis(rail)

print("\nMonoalphabetic")
frequency_analysis(mono)

print("\n========== Comparison ==========")
print("Caesar          : Very Low Resistance")
print("Rail Fence      : Low Resistance")
print("Monoalphabetic  : Medium Resistance")
print("Vigenere        : High Resistance")
