# Experiment 3b
# AES Encryption using ECB, CBC, CFB and OFB Modes

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time


# 16-byte AES secret key
key = b"16byteaeskey1234"

# 16-byte Initialization Vector
iv = b"1234567890123456"


# ---------------- Main Program ---------------- #

plaintext = input("Enter Plaintext: ").encode()

# Pad plaintext to AES block size
padded_text = pad(plaintext, AES.block_size)


# ---------------- ECB Mode ---------------- #

start = time.perf_counter()

ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_encrypted = ecb_cipher.encrypt(padded_text)

ecb_time = time.perf_counter() - start


# ---------------- CBC Mode ---------------- #

start = time.perf_counter()

cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
cbc_encrypted = cbc_cipher.encrypt(padded_text)

cbc_time = time.perf_counter() - start


# ---------------- CFB Mode ---------------- #

start = time.perf_counter()

cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
cfb_encrypted = cfb_cipher.encrypt(padded_text)

cfb_time = time.perf_counter() - start


# ---------------- OFB Mode ---------------- #

start = time.perf_counter()

ofb_cipher = AES.new(key, AES.MODE_OFB, iv)
ofb_encrypted = ofb_cipher.encrypt(padded_text)

ofb_time = time.perf_counter() - start


# ---------------- Display Results ---------------- #

print("\n" + "=" * 55)
print("              AES Encryption Results")
print("=" * 55)

print("\nECB :")
print(ecb_encrypted.hex())

print("\nCBC :")
print(cbc_encrypted.hex())

print("\nCFB :")
print(cfb_encrypted.hex())

print("\nOFB :")
print(ofb_encrypted.hex())


# ---------------- Execution Time ---------------- #

print("\n" + "=" * 55)
print("              Execution Time")
print("=" * 55)

print(f"\nECB : {ecb_time:.7f} seconds")
print(f"CBC : {cbc_time:.7f} seconds")
print(f"CFB : {cfb_time:.7f} seconds")
print(f"OFB : {ofb_time:.7f} seconds")


# ---------------- Security Comparison ---------------- #

print("\n" + "=" * 55)
print("              Security Comparison")
print("=" * 55)

print("\nECB : Least Secure")
print("CBC : High Security")
print("CFB : High Security (Streaming)")
print("OFB : High Security (No Error Propagation)")


