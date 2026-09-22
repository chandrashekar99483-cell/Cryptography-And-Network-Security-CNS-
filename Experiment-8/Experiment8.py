# Experiment 8
# Diffie-Hellman Key Exchange for Secure Session Key Establishment


# Public parameters
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))


# Private keys
a = int(input("\nEnter User A private key: "))
b = int(input("Enter User B private key: "))


# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)


print("\n" + "=" * 50)
print("        DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 50)

print("\nPublic Parameters")
print("-----------------")
print("Prime number (p):", p)
print("Primitive root (g):", g)


print("\nPrivate Keys")
print("------------")
print("User A Private Key:", a)
print("User B Private Key:", b)


print("\nPublic Keys")
print("-----------")
print("User A Public Key:", A)
print("User B Public Key:", B)


# Calculate shared session keys
shared_key_A = pow(B, a, p)
shared_key_B = pow(A, b, p)


print("\nShared Session Keys")
print("-------------------")
print("User A Shared Key:", shared_key_A)
print("User B Shared Key:", shared_key_B)


print("\nKey Verification")
print("----------------")

if shared_key_A == shared_key_B:
    print("Both shared keys are equal.")
    print("Secure Session Key Established")
    print("Shared Session Key:", shared_key_A)
else:
    print("Shared keys are not equal.")
    print("Key Exchange Failed")
