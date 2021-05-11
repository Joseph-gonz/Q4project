import random 

humanHand = list()
CPUHand = list() 
HumanPairs = 0
CPUPairs = 0 
deck = [
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "Ace"
]

random.shuffle(deck)


for i in range(5):
    card = deck.pop()
    humanHand.append(card)
for i in range(5):
    card = deck.pop()
    CPUHand.append(card)    

def check_pairs(hand):
    points = 0 
    for card in hand:
        if hand.count(card) > 1:
            hand.remove(card)
            hand.remove(card)
            points += 1
    return points





humanPairs = check_pairs(humanHand)
CPUPairs = check_pairs(CPUHand)



print("Go fish V1.0")
while True:
    if len(humanHand) < 1 or len(CPUHand) < 1:
        break
    while True:
        print("Your deck is ", humanHand)
        askedCard = input("Ask for a card:\n")

        if askedCard in CPUHand :
            print("Good job! CPU has that card")
            CPUHand.remove(askedCard)
            humanHand.remove(askedCard)
            humanPairs += 1
            continue
        else:
            print("Go fish!")
            humanHand.append(deck.pop())
            break
    humanPairs += check_pairs(humanHand)

    while True:
        askedCard = random.choice(deck)
        print("CPU asks for ", askedCard)
        if askedCard in humanHand:
            print("CPU gets ", askedCard)
            humanHand.remove(askedCard)
            CPUHand.remove(askedCard)
            CPUPairs += 1
            continue 
        else:
            print("CPU Goes fishing")
            CPUHand.append(deck.pop())
            break 
    CPUPairs += check_pairs(CPUHand)