
user_string = input("Please enter string: ")
stride = int(input("Please enter and integer for the stride: "))
newstring = ""

for index in range(0, len(user_string), strinde):
    if (index / stride) % 2 == 0:
        newstring += user_string[index : index + stride].lower()
    else
        newstring += user_string[index: index + stride].upper()
print(newstring)
