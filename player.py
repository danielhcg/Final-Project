class Player:
    pass

player1 = Player()
player2 = Player()
player3 = Player()

print('\n')
player1.name = str(input("Player name: "))
print(player1.name)
player1.obp = float(input("Please enter " + player1.name + "'s OBP: "))
player1.slg = float(input("Please enter " + player1.name + "'s SLG: "))
print('\n')

player2.name = str(input("Player name: "))
print(player2.name)
player2.obp = float(input("Please enter " + player2.name + "'s OBP: "))
player2.slg = float(input("Please enter " + player2.name + "'s SLG: "))
print('\n')

player3.name = str(input("Player name: "))
print(player3.name)
player3.obp = float(input("Please enter " + player3.name + "'s OBP: "))
player3.slg = float(input("Please enter " + player3.name + "'s SLG: "))
print('\n')

LG_OBP = 0.363
LG_SLG = 0.397

ops_plus1 = 100 * (player1.obp/LG_OBP + player1.slg/LG_SLG - 1)
ops_plus2 = 100 * (player2.obp/LG_OBP + player2.slg/LG_SLG - 1)
ops_plus3 = 100 * (player3.obp/LG_OBP + player3.slg/LG_SLG - 1)

lyst = [round(ops_plus1), round(ops_plus2), round(ops_plus3)]
lyst.sort(reverse=True)

print("OPS+ Leaderboard")
for lyst in (ops_plus1, ops_plus2, ops_plus3):
    print(lyst)
