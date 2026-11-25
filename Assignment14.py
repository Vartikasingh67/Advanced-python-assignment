import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different logging levels
logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

# Demonstrating logging in a program
try:
    a = 10
    b = 0
    result = a / b

except ZeroDivisionError:
    logging.exception("Division by zero is not allowed")

print("Logging demonstration completed.")
