import random 

humanHand = list()
CPUHand = list() 
HumanPairs = 0
CPUPairs = 0 
deck = [
    "KingH",
    "QueenH",
    "JackH",
    "10H",
    "9H",
    "8H",
    "7H",
    "6H",
    "5H",
    "4H",
    "3H",
    "2H",
    "AceH",
    "KingS",
    "QueenS",
    "JackS",
    "10S",
    "9S",
    "8S",
    "7S",
    "6S",
    "5S",
    "4S",
    "3S",
    "2S",
    "AceS",
    "KingC",
    "QueenC",
    "JackC",
    "10C",
    "9C",
    "8C",
    "7C",
    "6C",
    "5C",
    "4C",
    "3C",
    "2C",
    "AceC",
    "KingD",
    "QueenD",
    "JackD",
    "10D",
    "9D",
    "8D",
    "7D",
    "6D",
    "5D",
    "4D",
    "3D",
    "2D",
    "AceD"
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

def main():
    humanPairs = check_pairs(humanHand)
    CPUPairs = check_pairs(CPUHand)
    
    print("Go fish V1.0" +\
        "Key: S = Spades, C = Clubs, D = Diamonds, H = Hearts.")
    while True:
        if len(humanHand) < 1 or len(CPUHand) < 1:
            break
        while True:
            print("Your deck is ", humanHand)
            askedCard = input("Ask for a card:\n")

            if askedCard in CPUHand :
                print("Good job! CPU has that card")
                del CPUHand[askedCard]
                del humanHand[askedCard]
                humanPairs += 1
                continue
            else:
                print("Go fish!")
                humanHand.append(deck.pop())
                break
        humanPairs += check_pairs(humanHand)

        while True:
            askedCard = random.choice(CPUHand)
            print("CPU asks for ", askedCard)
            if askedCard in humanHand:
                print("CPU gets ", askedCard)
                del humanHand[askedCard]
                del CPUHand[askedCard]
                CPUPairs += 1
                continue 
            else:
                print("CPU Goes fishing")
                CPUHand.append(deck.pop())
                break 
        CPUPairs += check_pairs(CPUHand)
main()