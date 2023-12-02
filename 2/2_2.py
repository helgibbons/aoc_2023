max_red = 0
max_green = 0
max_blue = 0

successful_games = []

# open a text file and read it line by line
with open("2/input.txt") as f:
    for line in f:
        max_red = 0
        max_green = 0
        max_blue = 0
        # remove \n
        line = line.strip()
        # split on : and take the second part
        game_number = line.split(":")[0]
        # strip out everything but the number
        game_number = game_number.strip("Game ")
        line = line.split(":")[1]
        # split line into a list of rounds
        rounds = line.split(";")
        for round in rounds:
            # split round into a list of colours
            colours = round.split(",")
            for colour in colours:
                colour = colour.strip()
                # split colour
                colour_value, colour = colour.split(" ")
                # check the colours against the highest values
                if "red" in colour:
                    if int(colour_value) > max_red:
                        max_red = int(colour_value)
                if "green" in colour:
                    if int(colour_value) > max_green:
                        max_green = int(colour_value)
                if "blue" in colour:
                    if int(colour_value) > max_blue:
                        max_blue = int(colour_value)
        # add the power of the highest colours to the list
        successful_games.append(max_red * max_green * max_blue)
    # total all the numbers in the list
    print(sum(successful_games))

