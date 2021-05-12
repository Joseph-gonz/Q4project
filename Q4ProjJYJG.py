#Jackson Yocham
#5/11/21
#This code represents my own work. I worked on this project with Joseph through github. It was made over the course of 10 days.  
import random 

humanHand = list() #Creates 2 new empty lists for computers hand and players hand
CPUHand = list() 
humanPairs = 0 #Sets an empty variable for the amount of pairs each player has
CPUPairs = 0 

class deck(): #Class that stores the info for the cards used in the game. 
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
    random.shuffle(deckList) #Shuffles the deck so the pattern isn't as recognizable


def assign_deck(): #Assigns 5 cards to both the player and the computer
    for i in range(5):
        card = deck.deckList.pop()
        humanHand.append(card)
    for i in range(5):
        card = deck.deckList.pop()
        CPUHand.append(card)    

def check_pairs(hand): #Checks for pairs in the specified players hand
    points = 0 
    for card in hand:
        if hand.count(card) > 1:
            hand.remove(card)
            hand.remove(card)
            points += 1
    return points #Points is the amopunt of pairs the player has

def main(): #Creates main function for the game
    humanPairs = check_pairs(humanHand)
    CPUPairs = check_pairs(CPUHand)
    
    print("Go fish V1.0\n" + "This game ignores suits. You're looking for matching pairs decided by rank alone.") #Prints basic info
    while True: #Creates a while loop that is only broken by the "break" keyword
        if len(humanHand) < 1 or len(CPUHand) < 1: #Conditions for when the game is over (If either players hand gets below 1 card)
            print("Game over!\n" + "Here are the scores:\n" + "Human: ") #Prints the scoreline at the end
            print(humanPairs)
            print("CPU: ")
            print(CPUPairs)
            break #Breaks the while loop
        while True: #Creates another while loop
            print("Your deck is ", humanHand) #Shows the human player their hand
            askedCard = input("Ask for a card:\n") #Takes users input for requested card

            if askedCard in CPUHand : #If the computer has the requested card:
                print("Good job! CPU has that card\n" + "You got a matching pair!") #Prints a success message
                while askedCard in CPUHand: #Checks for the requested card in the computer and in the humans hand and removes them 
                    CPUHand.remove(askedCard)
                while askedCard in humanHand:
                    humanHand.remove(askedCard)
                humanPairs += 1
                continue
            else:
                print("Go fish!")
                humanHand.append(deck.deckList.pop()) #Forces human to draw a new card
                break
        humanPairs += check_pairs(humanHand) #Runs the check_pairs function to determine the score

        while True:
            askedCard = random.choice(CPUHand) #Same as before except it pulls a random card from the computers hand
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
       
assign_deck() #Calls both primary functions to start the program
main()


   
