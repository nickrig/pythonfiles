import random
sum = 0
for i in range(1000):
    p = [[random.randint(1,80) for j in range(5)] for j in range(100)]
    w = False
    pinakas = []
    while w == False:
        R = random.randint(1,80)
        if R not in pinakas:
            pinakas.append(R)
            for player in p:
                if R in player:
                    player.remove(R)
                    if player == []:
                        w = True
                        break
    sum = sum + len(pinakas)
print(int(sum/1000))
