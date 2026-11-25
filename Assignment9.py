import csv
import json

# Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Roll No", "Name", "Branch", "Marks"])
    writer.writerow([1, "Amit", "CSE", 85])
    writer.writerow([2, "Sneha", "CSE", 90])
    writer.writerow([3, "Rahul", "IT", 78])

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Write data into JSON file
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

# Display JSON data
print("CSV data converted successfully.")
print("\nJSON Data:")
print(json.dumps(data, indent=4))
