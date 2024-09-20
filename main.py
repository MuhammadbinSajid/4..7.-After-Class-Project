# Function to convert decimal to binary
def decimal_to_binary(decimal):
    # Using the built-in bin() function to get binary representation
    binary = bin(decimal).replace("0b", "")
    return binary

# Input from user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary and display result
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")
