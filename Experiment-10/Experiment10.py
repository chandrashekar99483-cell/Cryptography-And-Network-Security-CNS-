# Experiment 10
# Implementation of Cryptographic Hash Algorithms
# MD5, SHA-1, SHA-256 and SHA-512
import hashlib
import time
# Input messages
original_message = input("Enter the original message: ")
modified_message = input("Enter the slightly modified message: ")
# Function to calculate avalanche effect
def avalanche_effect(hash1, hash2):
    binary1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
    binary2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
    different_bits = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            different_bits += 1
    total_bits = len(binary1)
    percentage = (different_bits / total_bits) * 100
    return percentage
print("\n" + "=" * 50)
print("     CRYPTOGRAPHIC HASH ALGORITHM COMPARISON")
print("=" * 50)

# ============================================================
# MD5
# ============================================================

start = time.perf_counter()
md5_original = hashlib.md5(original_message.encode()).hexdigest()
md5_modified = hashlib.md5(modified_message.encode()).hexdigest()
md5_time = time.perf_counter() - start
md5_avalanche = avalanche_effect(md5_original, md5_modified)
print("\n" + "-" * 50)
print("MD5")
print("-" * 50)
print("Original Hash :", md5_original)
print("Modified Hash :", md5_modified)
print("Avalanche Effect :", format(md5_avalanche, ".2f"), "%")
print("Execution Time :", format(md5_time, ".8f"), "seconds")
# ============================================================
# SHA-1
# ============================================================

start = time.perf_counter()
sha1_original = hashlib.sha1(original_message.encode()).hexdigest()
sha1_modified = hashlib.sha1(modified_message.encode()).hexdigest()
sha1_time = time.perf_counter() - start
sha1_avalanche = avalanche_effect(sha1_original, sha1_modified)
print("\n" + "-" * 50)
print("SHA-1")
print("-" * 50)
print("Original Hash :", sha1_original)
print("Modified Hash :", sha1_modified)
print("Avalanche Effect :", format(sha1_avalanche, ".2f"), "%")
print("Execution Time :", format(sha1_time, ".8f"), "seconds")
# ============================================================
# SHA-256
# ============================================================
start = time.perf_counter()
sha256_original = hashlib.sha256(original_message.encode()).hexdigest()
sha256_modified = hashlib.sha256(modified_message.encode()).hexdigest()
sha256_time = time.perf_counter() - start
sha256_avalanche = avalanche_effect(sha256_original, sha256_modified)
print("\n" + "-" * 50)
print("SHA-256")
print("-" * 50)
print("Original Hash :", sha256_original)
print("Modified Hash :", sha256_modified)
print("Avalanche Effect :", format(sha256_avalanche, ".2f"), "%")
print("Execution Time :", format(sha256_time, ".8f"), "seconds")
# ============================================================
# SHA-512
# ============================================================
start = time.perf_counter()
sha512_original = hashlib.sha512(original_message.encode()).hexdigest()
sha512_modified = hashlib.sha512(modified_message.encode()).hexdigest()
sha512_time = time.perf_counter() - start
sha512_avalanche = avalanche_effect(sha512_original, sha512_modified)
print("\n" + "-" * 50)
print("SHA-512")
print("-" * 50)
print("Original Hash :", sha512_original)
print("Modified Hash :", sha512_modified)
print("Avalanche Effect :", format(sha512_avalanche, ".2f"), "%")
print("Execution Time :", format(sha512_time, ".8f"), "seconds")



