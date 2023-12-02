keys = ["_", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list = []

# open a text file and read it line by line
with open("1/input.txt") as f:
    for line in f:
        # scan and replace the first occurrence of a key
        key_found = False
        for x in range(0, len(line)):
            for key in keys:
                if key in line[0:x]:
                    if not key_found:
                        line = line.replace(key, str(keys.index(key)))
                        key_found = True
        # scan and replace the last occurrence of a key
        key_found = False
        for x in range(len(line), 0, -1):
            for key in keys:
                if key in line[x:len(line)]:
                    if not key_found:
                        line = line.replace(key, str(keys.index(key)))
                        key_found = True
        print(line)
        # strip the letters
        line = "".join(c for c in line if c.isdecimal())
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