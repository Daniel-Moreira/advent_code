# Initialize a counter to 0
count = 0
prev = None

# Open the file with 'r' mode for reading
with open('input.txt', 'r') as file:
    # Read each line of the file
    for line in file:
        # Convert the line to an integer
        num = int(line)
        # Check if the number is greater than the previous number
        if prev and num > prev:
            # If it is, increment the counter
            count += 1
        # Update the previous number
        prev = num

# Print the count
print(count)
