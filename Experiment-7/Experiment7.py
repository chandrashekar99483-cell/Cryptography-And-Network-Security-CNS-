# Experiment 7
# RSA Key Generation, Encryption, Decryption and Digital Signing

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


# Generate RSA Keys
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

print("\n" + "=" * 50)
print("             RSA KEY GENERATION")
print("=" * 50)

print("\nPublic Key:")
print(public_key.export_key().decode())

print("\nPrivate Key:")
print(private_key.export_key().decode())


# Get plaintext
message = input("\nEnter the Plaintext: ")
message = message.encode("utf-8")


# Encryption
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)

print("\nCiphertext (Hex):")
print(ciphertext.hex())


# Decryption
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(ciphertext)

print("\nDecrypted Message:")
print(decrypted_message.decode("utf-8"))


# SHA-256 Hash
hash_value = SHA256.new(message)

print("\nSHA-256 Hash:")
print(hash_value.hexdigest())


# Digital Signature
signature = pkcs1_15.new(private_key).sign(hash_value)

print("\nDigital Signature (Hex):")
print(signature.hex())


# Signature Verification
hash_for_verification = SHA256.new(message)

try:
    pkcs1_15.new(public_key).verify(
        hash_for_verification,
        signature
    )
    print("\nSignature Verification: VALID")

except (ValueError, TypeError):
    print("\nSignature Verification: INVALID")



