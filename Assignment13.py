import threading
import time

# Task 1: Display numbers
def display_numbers():
    for i in range(1, 6):
        print("\nNumber:", i)
        time.sleep(4)

# Task 2: Display squares
def display_squares():
    for i in range(1, 6):
        print("\nSquare of", i, "=", i * i)
        time.sleep(4)

# Task 3: Display messages
def display_messages():
    for i in range(1, 6):
        print("\nPython Thread", i)
        time.sleep(4)

# Create threads
t1 = threading.Thread(target=display_numbers)
t2 = threading.Thread(target=display_squares)
t3 = threading.Thread(target=display_messages)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll tasks completed")
