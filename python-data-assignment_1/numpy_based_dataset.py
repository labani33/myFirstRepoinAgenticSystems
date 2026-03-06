import numpy as np

np.random.seed(42)
data= np.random.rand(100, 3)
mean = np.mean(data, axis=0)
std= np.std(data, axis=0)
normalized_data = (data - mean) / std
print("Mean of each column:", mean)
print("Standard deviation of each column:", std)
train_data = normalized_data[:80]
test_data = normalized_data[80:]
slice_view=data[:5]
slice_view[0, 0] = 999
print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Training data shape:", train_data.shape)
print("Testing data shape:", test_data.shape)
print("Modifying the slice affected the original array")
print("Modified original data (first row):", data[0,0])