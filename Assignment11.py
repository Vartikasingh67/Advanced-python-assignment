import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

# Display the original Series
print("Original Series:")
print(s)

# Indexing
print("\nFirst element:", s[0])

print("First three elements:")
print(s[:3])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
