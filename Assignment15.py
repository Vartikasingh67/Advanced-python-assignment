import gc

# Check automatic garbage collection
print("Garbage Collection Enabled:", gc.isenabled())

# Display garbage collection information
print("GC Count:", gc.get_count())
print("GC Threshold:", gc.get_threshold())

# Disable automatic garbage collection
gc.disable()
print("\nAutomatic GC Disabled:", not gc.isenabled())

# Create a circular reference
a = []
a.append(a)

# Delete the reference
del a

print("\nGarbage created by circular reference")

# Manually perform garbage collection
collected = gc.collect()
print("Objects collected:", collected)

# Enable automatic garbage collection
gc.enable()
print("\nAutomatic GC Enabled:", gc.isenabled())

print("Final GC Count:", gc.get_count())
print("Program completed successfully.")
