# Experiment 4
# Secure Random Number Generator and Statistical Testing

import secrets
import numpy as np
from scipy.stats import chisquare

# Generate 1000 secure random numbers from 0 to 9
numbers = [secrets.randbelow(10) for _ in range(1000)]

# Convert to NumPy array
numbers = np.array(numbers)

# Calculate mean and variance
mean = np.mean(numbers)
variance = np.var(numbers)

# Calculate observed frequency
observed = np.bincount(numbers, minlength=10)

# Expected frequency
expected = np.full(10, len(numbers) / 10)

# Chi-Square test
chi_square, p_value = chisquare(observed, expected)

# Display results
print("\n" + "=" * 45)
print("     SECURE RANDOM NUMBER GENERATOR")
print("=" * 45)

print("\nGenerated Random Numbers:")
print(numbers[:20], "...")

print("\nStatistical Analysis")
print("-" * 25)

print("Mean:", round(mean, 3))
print("Variance:", round(variance, 3))

print("\nObserved Frequency:")
print(observed)

print("\nExpected Frequency:")
print(expected.astype(int))

print("\nChi-Square Statistic:", round(chi_square, 2))
print("P-value:", round(p_value, 4))

print("\nResult:")
if p_value > 0.05:
    print("The generated numbers pass the randomness test.")
else:
    print("The generated numbers do not pass the randomness test.")
