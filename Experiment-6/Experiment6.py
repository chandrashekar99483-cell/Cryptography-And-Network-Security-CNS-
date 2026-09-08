# Experiment 6
# Primality Testing using Trial Division, Fermat Test and Miller-Rabin Test

import random
import time
import math


# ---------------- Trial Division ---------------- #

def trial_division(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# ---------------- Fermat Test ---------------- #

def fermat_test(n, rounds=5):
    if n <= 1:
        return False

    if n <= 3:
        return True

    for _ in range(rounds):
        a = random.randint(2, n - 2)

        if math.gcd(a, n) != 1:
            return False

        if pow(a, n - 1, n) != 1:
            return False

    return True



# ---------------- Main Program ---------------- #

n = int(input("Enter a number: "))


# Trial Division
start = time.perf_counter()
trial_result = trial_division(n)
trial_time = time.perf_counter() - start


# Fermat Test
start = time.perf_counter()
fermat_result = fermat_test(n)
fermat_time = time.perf_counter() - start


# Miller-Rabin Test
start = time.perf_counter()
miller_result = miller_rabin(n)
miller_time = time.perf_counter() - start


# ---------------- Display Results ---------------- #

print("\nPrimality Test Results")
print("-" * 40)

if trial_result:
    print("Trial Division : Prime")
else:
    print("Trial Division : Composite")

print("Time :", format(trial_time, ".8f"), "seconds")


if fermat_result:
    print("Fermat Test : Probably Prime")
else:
    print("Fermat Test : Composite")

print("Time :", format(fermat_time, ".8f"), "seconds")


