import numpy as np
import pandas as pd
import os

# Ensure the output directory exists
os.makedirs('../data', exist_ok=True)

# Number of samples
n_samples = 1000

# Generate random leg lengths
a = np.random.uniform(1, 100, n_samples)
b = np.random.uniform(1, 100, n_samples)

# Calculate hypotenuse using Pythagoras' theorem
c = np.sqrt(a**2 + b**2)

# Create DataFrame and save to CSV
df = pd.DataFrame({'a': a, 'b': b, 'c': c})
df.to_csv('../data/triangles.csv', index=False)

print("Dataset saved to ../data/triangles.csv")
