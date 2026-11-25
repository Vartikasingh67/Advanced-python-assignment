import numpy as np

# 1. Create an array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# 2. Slicing operations
print("\nSLICING")

print("\nFirst 5 elements:")
print(arr[:5])

print("\nElements from index 2 to 6:")
print(arr[2:7])

print("\nLast 3 elements:")
print(arr[-3:])

# 3. Statistical operations
print("\nSTATISTICAL OPERATION")

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting - add 5 to every element
print("\nBROADCASTING")

arr = arr + 5

print("\nArray after Broadcasting:")
print(arr)
