# Experiment 12
# RSA Digital Signature for Authentication and Non-Repudiation

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


# Generate RSA Keys
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()


# Read Message
message = input("Enter the Message: ")
message = message.encode()


# Generate SHA-256 Hash
hash_value = SHA256.new(message)


# Generate Digital Signature
signature = pkcs1_15.new(private_key).sign(hash_value)

print("\nDigital Signature (Hex):")
print(signature.hex())


# Verify Digital Signature
try:
    hash_for_verification = SHA256.new(message)

    pkcs1_15.new(public_key).verify(
        hash_for_verification,
        signature
    )

    print("\nSignature Verification : SUCCESS")
    print("Sender Authentication : VERIFIED")
    print("Message Integrity : VERIFIED")
    print("Non-Repudiation : ACHIEVED")

except (ValueError, TypeError):
    print("\nSignature Verification : FAILED")
    print("Sender Authentication : FAILED")
    print("Message Integrity : FAILED")
    print("Non-Repudiation : NOT VERIFIED")
