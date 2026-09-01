# Experiment 5
# Implementation of Modular Arithmetic Algorithms

from math import gcd


# ---------------- Euclid's Algorithm ---------------- #

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# ---------------- Extended Euclidean Algorithm ---------------- #

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_euclid(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


# ---------------- Euler's Totient Function ---------------- #

def phi(n):
    count = 0

    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1

    return count


# ---------------- Chinese Remainder Theorem ---------------- #

def crt(moduli, remainders):
    product = 1

    for m in moduli:
        product *= m

    result = 0

    for m, r in zip(moduli, remainders):
        partial = product // m

        # Find modular inverse
        inverse = pow(partial, -1, m)

        result += r * partial * inverse

    return result % product


# ---------------- Main Program ---------------- #

# Part A - Euclid's Algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nEuclid's Algorithm")
print("GCD =", euclid(a, b))


# Part B - Extended Euclidean Algorithm

g, x, y = extended_euclid(a, b)

print("\nExtended Euclid")
print("GCD =", g)
print("x =", x)
print("y =", y)

if g == 1:
    print("Modular Inverse of", a, "mod", b, "=", x % b)
else:
    print("Modular inverse does not exist.")


# Part C - Fermat's Little Theorem

p = int(input("\nEnter a prime number: "))

if gcd(a, p) == 1:
    fermat_result = pow(a, p - 1, p)

    print("\nFermat's Theorem")
    print("a^(p-1) mod p =", fermat_result)
else:
    print("\na and p must be coprime for Fermat's Theorem.")


# Part D - Euler's Theorem

n = int(input("\nEnter n for Euler's Theorem: "))

if gcd(a, n) == 1:
    phi_value = phi(n)
    euler_result = pow(a, phi_value, n)

    print("\nEuler's Theorem")
    print("phi(n) =", phi_value)
    print("Euler Result =", euler_result)
else:
    print("\na and n must be coprime for Euler's Theorem.")


# Part E - Chinese Remainder Theorem

moduli = [3, 5, 7]
remainders = [2, 3, 2]

solution = crt(moduli, remainders)

print("\nChinese Remainder Theorem")
print("Moduli =", moduli)
print("Remainders =", remainders)
print("Solution =", solution)
