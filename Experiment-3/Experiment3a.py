# Experiment 3a
# DES Encryption using ECB, CBC, CFB and OFB Modes


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import time

# DES requires an 8-byte key
key = b"8bytekey"

# DES requires an 8-byte IV for CBC, CFB and OFB
iv = b"12345678"


# ---------------- Main Program ---------------- #

plaintext = input("Enter Plaintext: ").encode()

# Pad plaintext to DES block size
padded_text = pad(plaintext, DES.block_size)


# ---------------- ECB Mode ---------------- #

start = time.perf_counter()

ecb_cipher = DES.new(key, DES.MODE_ECB)
ecb_encrypted = ecb_cipher.encrypt(padded_text)

ecb_time = time.perf_counter() - start


# ---------------- CBC Mode ---------------- #

start = time.perf_counter()

cbc_cipher = DES.new(key, DES.MODE_CBC, iv)
cbc_encrypted = cbc_cipher.encrypt(padded_text)

cbc_time = time.perf_counter() - start


# ---------------- CFB Mode ---------------- #

start = time.perf_counter()

cfb_cipher = DES.new(key, DES.MODE_CFB, iv)
cfb_encrypted = cfb_cipher.encrypt(padded_text)

cfb_time = time.perf_counter() - start


# ---------------- OFB Mode ---------------- #

start = time.perf_counter()

ofb_cipher = DES.new(key, DES.MODE_OFB, iv)
ofb_encrypted = ofb_cipher.encrypt(padded_text)

ofb_time = time.perf_counter() - start


# ---------------- Display Results ---------------- #

print("\n" + "=" * 60)
print("                 DES ENCRYPTION RESULTS")
print("=" * 60)

print("\nECB Ciphertext :")
print(ecb_encrypted.hex())

print("\nCBC Ciphertext :")
print(cbc_encrypted.hex())

print("\nCFB Ciphertext :")
print(cfb_encrypted.hex())

print("\nOFB Ciphertext :")
print(ofb_encrypted.hex())


# ---------------- Execution Time ---------------- #

print("\n" + "=" * 60)
print("                 EXECUTION TIME")
print("=" * 60)

print(f"\nECB : {ecb_time:.6f} seconds")
print(f"CBC : {cbc_time:.6f} seconds")
print(f"CFB : {cfb_time:.6f} seconds")
print(f"OFB : {ofb_time:.6f} seconds")


# ---------------- Security Comparison ---------------- #

print("\n" + "=" * 60)
print("                 SECURITY COMPARISON")
print("=" * 60)

print("\nECB : Least Secure")
print("CBC : Secure")
print("CFB : Secure for Streaming")
print("OFB : Secure for Noisy Channels")
