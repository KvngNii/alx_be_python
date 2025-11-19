# pattern_drawing.py
# A program that draws a square pattern using nested loops

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side
    for col in range(size):
        print("*", end="")
    
    # Print a newline after completing each row
    print()
    
    # Increment the row counter
    row += 1
