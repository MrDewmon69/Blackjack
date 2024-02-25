from tkinter import *
import random as r

mainWindow = Tk()
mainWindow.geometry("600x600")
mainWindow.title("Blackjack")
cardDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = []

class Player:
    def __init__(self, *hand) -> None:
        self.hand = hand
        
    def startGame(self):
        global hitButton, standButton, dealerLabel, dealerCards
        hitButton = Button(mainWindow, text="Hit", command=player1.hit)
        hitButton.grid(row=1, column=3)

        standButton = Button(mainWindow, text="Stand", command=player1.stand)
        standButton.grid(row=1, column=2)
        startGameButton.destroy()

        deck = cardDeck
        for e in range(2):
            card = r.choice(deck)
            cards.append(card)
        dealerLabel["text"] = dealerCards
        player1.hand = cards
        cardTotal = cards[0] + cards[1]
        print(cardTotal)
        convertedList = str(player1.hand)
        playerCardLabel["text"] = convertedList

    def hit(self):
        global playerCards
        print(player1.hand)
        playerCards = player1.hand
        newCard = r.choice(cardDeck)
        playerCards.append(newCard)
        convertedList = str(playerCards)
        playerCardLabel["text"] = convertedList

        print(playerCards)

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
            dealerBustLabel["text"] = "Dealer Busts"
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
        print(dealerCards)

        dealerText = Label(mainWindow, text="Dealer's Cards: ")
        dealerText.grid(row=4, column=2, columnspan=1)
        dealerLabel = Label(mainWindow, text="0")
        dealerLabel.grid(row=4, column=3)
        
player1 = Player()
dealer = Dealer()
dealer.deal()

startGameButton = Button(mainWindow, text="Deal", command=player1.startGame)
startGameButton.grid(row=1, column=3)
playerCardLabel = Label(mainWindow, text="0")
playerCardLabel.grid(row=2, column=3)

if __name__ == '__main__':
    mainWindow.mainloop()
