import random 

humanHand = list()
CPUHand = list() 
humanPairs = 0
CPUPairs = 0 

class deck():
    def __init__(self, deck):
        self.deck = deckList
        
    deckList = [
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
    "1C",
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
    random.shuffle(deckList)


def assign_deck():
    for i in range(5):
        card = deck.deckList.pop()
        humanHand.append(card)
    for i in range(5):
        card = deck.deckList.pop()
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
    
    print("Go fish V1.0\n" + "This game ignores suits. You're looking for matching pairs decided by rank alone.")
    while True:
        if len(humanHand) < 1 or len(CPUHand) < 1:
            print("Game over!\n" + "Here are the scores:\n" + "Human: ")
            print(humanPairs)
            print("CPU: ")
            print(CPUPairs)
            break
        while True:
            print("Your deck is ", humanHand)
            askedCard = input("Ask for a card:\n")

            if askedCard in CPUHand :
                print("Good job! CPU has that card\n" + "You got a matching pair!")
                while askedCard in CPUHand:
                    CPUHand.remove(askedCard)
                while askedCard in humanHand:
                    humanHand.remove(askedCard)
                humanPairs += 1
                continue
            else:
                print("Go fish!")
                humanHand.append(deck.deckList.pop())
                break
        humanPairs += check_pairs(humanHand)

        while True:
            askedCard = random.choice(CPUHand)
            print("CPU asks for ", askedCard)
            if askedCard in humanHand:
                print("CPU gets ", askedCard)
                while askedCard in CPUHand:
                    CPUHand.remove(askedCard)
                while askedCard in humanHand:
                    humanHand.remove(askedCard)
                CPUPairs += 1
                continue 
            else:
                print("CPU Goes fishing")
                CPUHand.append(deck.deckList.pop())
                break 
        CPUPairs += check_pairs(CPUHand)
       
assign_deck()
main()


   
