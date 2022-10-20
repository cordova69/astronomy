#!/bin/env python3
#ask for user input for string
# Store user input in a variable
user_string = input("Please enter a string: ")

# Ask for user input for a stride
stride = int(input("Please enter a stride:"))

# Loop over the string
#    Start at position 0
#    Increment by strident * 2 each iteration
# Extract two strides from the string
#    First stride - current position to current position + stride
#    Uppercase first stride, and add to result
#    Second stride - current position + stride to current position + 2 * stride
#    Lowercase the second stride, and add to result
# After loop, print out the result

result = ''
for position in range(0, len(user_string), stride * 2):
    first_chunk = user_string[position:position + stride].upper()
    second_chunk = user_string[position + stride:position + stride *2].lower()
    result += first_chunk + second_chunk
print(result)


