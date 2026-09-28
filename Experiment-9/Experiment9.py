# Experiment 9
# ECC Key Generation and Comparison with RSA

import time
import secrets
from tinyec import registry
from cryptography.hazmat.primitives.asymmetric import ec, rsa

# ECC Key Generation
curve = registry.get_curve("secp256r1")

start = time.perf_counter()

ecc_private_key = secrets.randbelow(curve.field.n)
ecc_public_key = ecc_private_key * curve.g

ecc_time = time.perf_counter() - start


# RSA Key Generation
start = time.perf_counter()

rsa_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

rsa_public_key = rsa_private_key.public_key()

rsa_time = time.perf_counter() - start


# Display Results
print("\n" + "=" * 55)
print("       ECC AND RSA KEY GENERATION")
print("=" * 55)

print("\nECC Public Key:")
print("X =", ecc_public_key.x)
print("Y =", ecc_public_key.y)

print("\nECC Key Generation Time:")
print(format(ecc_time, ".8f"), "seconds")

print("\nRSA Public Key:")
print(rsa_public_key.public_numbers())

print("\nRSA Key Generation Time:")
print(format(rsa_time, ".8f"), "seconds")


# Comparison
print("\n" + "-" * 55)
print("              PERFORMANCE COMPARISON")
print("-" * 55)

print("ECC Time:", format(ecc_time, ".8f"), "seconds")
print("RSA Time:", format(rsa_time, ".8f"), "seconds")

if ecc_time < rsa_time:
    print("\nECC key generation is faster than RSA.")
else:
    print("\nRSA key generation is faster than ECC.")
