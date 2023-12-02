list = []

# open a text file and read it line by line
with open("1/input.txt") as f:
    for line in f:
        # strip the letters
        line = "".join(c for c in line if  c.isdecimal())
        # if the line length is 1
        if len(line) == 1:
            line = line + line
            list.append(int(line))
        else:
            # add the first and last numbers
            line = line[0] + line[-1]
            list.append(int(line))

# add the numbers in the list together
print(sum(list))