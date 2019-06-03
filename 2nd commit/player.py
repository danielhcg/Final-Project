class Player:

    # Creates 1st instance of Player class
    def __init__(self, name, obp, slg):
        self.name = name
        self.obp = obp
        self.slg = slg


# Assigns values to first player object through
# user input
p1 = Player(
    str(input("Player name: ")),
    (float(input("Please enter OBP: "))),
    (float(input("Please enter SLG: ")))
)


# Constant variable that are used for each players'
# calculation.
LG_OBP = 0.363
LG_SLG = 0.397


# OPS+ calculation
ops_plus1 = 100 * (p1.obp/LG_OBP + p1.slg/LG_SLG - 1)
print(p1.name + "'s OPS+:", round(ops_plus1))
print('\n')


# Creates second instance of Player class
def player2(self, name, obp, slg):
    self.name = name
    self.obp = obp
    self.slg = slg


# Assigns values to second player object through
# user input
p2 = Player(
    str(input("Player name: ")),
    (float(input("Please enter OBP: "))),
    (float(input("Please enter SLG: ")))
)


# OPS+ calculation
ops_plus2 = 100 * (p2.obp/LG_OBP + p2.slg/LG_SLG - 1)
print(p2.name + "'s OPS+:", round(ops_plus2))
print('\n')


# Creates third instance of player class
def player3(self, name, obp, slg):
    self.name = name
    self.obp = obp
    self.slg = slg


# Assigns values to third player object through
# user input
p3 = Player(
    str(input("Player name: ")),
    (float(input("Please enter OBP: "))),
    (float(input("Please enter SLG: ")))
)


# Calculation for OPS+ and prints the result
ops_plus3 = 100 * (p3.obp/LG_OBP + p3.slg/LG_SLG - 1)
print(p3.name + "'s OPS+:", round(ops_plus3))
print('\n')


# Creates an array than can be referenced later in the for loop
# to print the results.
# Uses round() function to round the results from the OPS+
# calculations.
ops_plus = [round(ops_plus1), round(ops_plus2), round(ops_plus3)]


# Prints the title of the leader board
print("OPS+ Leaderboard")


# Sorts the array items in descending order using the
# sort() function
ops_plus.sort(reverse=True)


# For loop that displays the OPS+'s of all three players
# and uses the enumerate function to attach a counter
# to the the list.
for count, value in enumerate(ops_plus, 1):
    print(count, value)
