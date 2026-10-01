f1 = open("APP.txt", "r")

lines = f1.readlines()

f1.close()

print("Total No. of lines in file APP1.txt:", len(lines))

print("Contents of list lines:", lines)

two_lines = lines[:2]

print("First two lines:")

for i in two_lines:
    print(i)

f2 = open("Output.txt", "w")

f2.writelines(two_lines)

f2.close()

print("\nFirst two lines from APP.txt are written in Output.txt")
