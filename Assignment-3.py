# Strategy Classes
class CreditCard:
    def pay(self, amount):
        print("Payment of ₹", amount, "done using Credit Card")

class UPI:
    def pay(self, amount):
        print("Payment of ₹", amount, "done using UPI")

class Cash:
    def pay(self, amount):
        print("Payment of ₹", amount, "done using Cash")

# Context Class
class Payment:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)

# Main Program
amount = int(input("Enter Amount: "))

print("1. Credit Card")
print("2. UPI")
print("3. Cash")

choice = int(input("Enter Choice: "))

if choice == 1:
    method = CreditCard()
elif choice == 2:
    method = UPI()
elif choice == 3:
    method = Cash()
else:
    print("Invalid Choice")
    exit()

payment = Payment(method)
payment.process(amount)
