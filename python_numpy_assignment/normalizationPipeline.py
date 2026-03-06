import numpy as np


data = np.array([10, 20, 30, 40])


mean_val = data.mean()
std_val = data.std()
normalized = (data - mean_val) / std_val
reshaped = normalized.reshape(2,2)
print("Original data:", data)
print("Mean:", float(f"{mean_val:.2f}"))
print("Standard Deviation:", float(f"{std_val:.2f}"))
print("Normalized data:", np.round(normalized, 2))
print("Reshaped data shape:", reshaped.shape)