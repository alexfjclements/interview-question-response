import math

# Request number of asterisks in pattern
r = int(input("How many asterisks do you want in the pattern?"))
root_r = math.sqrt(r)

# Check validity of entry
if root_r.is_integer():

    # 1/2 height = max width
    # max width = sqrt(r)
    # Initilise output
    n = 1
    m = 0
    line = "*"
    diagram = []

    # Populate first half of list
    while n <= root_r:
        o = n
        spacer = ""
        # Set inset of astrisks
        while o < root_r:
            spacer = spacer + " "
            o += 1
        diagram.append(spacer + line)
        line = line + " *"
        print(diagram[n-1])
        n += 1

    # Populate second half of list
    while n > root_r and n < 2 * root_r:
        o = int(root_r - 2 - m)
        diagram.append(diagram[o])
        print(diagram[n-1])
        n += 1
        m += 1

else:
    print("Error. Please enter a number with an integer root.")