red = 12
green = 13
blue = 14

successful_games = []
game_fail = False

# open a text file and read it line by line
with open("2/input.txt") as f:
    for line in f:
        game_fail = False
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
                    if int(colour_value) > red:
                        game_fail = True
                elif "green" in colour:
                    if int(colour_value) > green:
                        game_fail = True
                elif "blue" in colour:
                    if int(colour_value) > blue:
                        game_fail = True
        if game_fail == True:
            print("Game " + game_number + " failed")
        else:
            print("Game " + game_number + " passed")
            successful_games.append(int(game_number))
    # total all the numbers in the list
    print(sum(successful_games))

