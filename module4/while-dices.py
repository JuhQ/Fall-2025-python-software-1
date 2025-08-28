import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
#while (6 != 6 or 2 != 6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"dice1 = {dice1}, dice = {dice2}")
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")