import sys
# Read the contents of the file specified in the command line argument
D = open(sys.argv[1]).read().strip()
# Initialize variables to store the sums of the first and last digits
p1 = 0
p2 = 0
# Iterate through each line in the file
for line in D.split('\n'):
    # Initialize lists to store digits for p1 and p2 calculations
    p1_digits = []
    p2_digits = []
    # Iterate through each character in the line
    for i, c in enumerate(line):
        # If the character is a digit, add it to both p1_digits and p2_digits
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        # Check if the substring from the current position matches textual representations of numbers
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                # If there's a match, add the corresponding digit to p2_digits
                p2_digits.append(str(d + 1))
    # Calculate the sum of the first and last digits for p1 and p2
    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])
# Print the results
print(p1)
print(p2)


## to run the code, python3 test.py input.txt