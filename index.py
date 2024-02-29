from tkinter import *
import random as r

mainWindow = Tk()
mainWindow.title("Blackjack")
cardDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = []

class Player:
    def __init__(self, *hand, balance) -> None:
        self.hand = hand
        self.balance = balance
        
    def startGame(self):
        playerBet = betEntry.get()
        if not playerBet:
            print("Player bet not found")
        elif playerBet:
            if int(playerBet) > int(player1.balance):
                print("Not engouh money")
            elif int(playerBet) <= int(player1.balance):
                print("You have engouh money")

                global hitButton, standButton, dealerLabel, dealerCards
                hitButton = Button(mainWindow, text="Hit", command=player1.hit)
                hitButton.grid(row=1, column=3)

                standButton = Button(mainWindow, text="Stand", command=player1.stand)
                standButton.grid(row=1, column=2)
                startGameButton.destroy()

                for e in range(2):
                    card = r.choice(cardDeck)
                    cards.append(card)
                dealerLabel["text"] = dealerCards
                player1.hand = cards
                convertedList = str(player1.hand)
                playerCardLabel["text"] = convertedList

       

    def hit(self):
        global playerCards
        playerCards = player1.hand
        newCard = r.choice(cardDeck)
        playerCards.append(newCard)
        convertedList = str(playerCards)
        playerCardLabel["text"] = convertedList

        if sum(playerCards) > 21:
            loserLabel = Label(mainWindow, text="You busted")
            loserLabel.grid(row=5, column=2)
            hitButton.destroy()
            standButton.destroy()

    def stand(self):
        global dealerLabel, dealerCards
        dealerBustLabel = Label(mainWindow, text="Game in progress")
        dealerBustLabel.grid(row=5, column=2) 
        hitButton.destroy()
        standButton.destroy()

        while sum(dealerCards) <= 17:
            newDealCard = r.choice(cardDeck)
            dealerCards.append(newDealCard)
            dealerLabel["text"] = dealerCards

        if sum(dealerCards) > 21:
            dealerBustLabel["text"] = "Dealer Busts, You win"
        elif sum(dealerCards) > sum(cards):
            dealerBustLabel["text"] = "Dealer Wins"
        elif sum(dealerCards) < sum(cards):
            dealerBustLabel["text"] = "Player Wins"
        elif sum(dealerCards) == sum(cards):
            dealerBustLabel["text"] = "Draw"

class Dealer:
    def __init__(self, *hand):
        self.hand = hand

    def deal(self):
        global dealerLabel, dealerCards
        dealerCards = []
        dealerFirstCard = r.choice(cardDeck)
        dealerCards.append(dealerFirstCard)
        dealer.hand = dealerCards

        dealerText = Label(mainWindow, text="Dealer's Cards: ")
        dealerText.grid(row=4, column=2, columnspan=1)
        dealerLabel = Label(mainWindow, text="0")
        dealerLabel.grid(row=4, column=3)
        
player1 = Player(balance=1000)
dealer = Dealer()
dealer.deal()

startGameButton = Button(mainWindow, text="Deal", command=player1.startGame)
startGameButton.grid(row=1, column=3)
playerCardLabel = Label(mainWindow, text="0")
playerCardLabel.grid(row=2, column=3)
playerLabel = Label(mainWindow, text="Player Cards")
playerLabel.grid(row=2, column=2)
betEntry = Entry(mainWindow)
betEntry.grid(row=2, column=5)
betEntryLabel = Label(mainWindow, text="Bet: ")
betEntryLabel.grid(row=2, column=4)

if __name__ == '__main__':
    mainWindow.mainloop()
