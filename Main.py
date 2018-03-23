import random


numOfCards = int(input("How many cards would you like "))

defenceCards = list()
attackCards = list()
for i in range(numOfCards):
    worth = random.randint(1, numOfCards)
    defenceAbility = random.randint(1, numOfCards)
    defenceCard = (worth, defenceAbility)
    attackAbility = random.randint(1, numOfCards)

    defenceCards.append(defenceCard)
    attackCards.append(attackAbility)

attackCards.sort(reverse = True)
defenceCards.sort(reverse = True)

print(defenceCards)
print("\n")
print(attackCards)

listIndex = list()
attackListIndex = list()
i = 0
temp = 0
while i < numOfCards:
    temp = i
    j = 0
    while j < numOfCards:
        if defenceCards[i][1] == attackCards[j] or defenceCards[i][1] >= attackCards[j]:
            if not j in attackListIndex:
                listIndex.append(i)
                attackListIndex.append(j)
                i = i + 1
                break
            else:
                j = j + 1
        else:
            j = j + 1
    if temp == i:
        i = i + 1
        break


print("\n")
print(listIndex)

