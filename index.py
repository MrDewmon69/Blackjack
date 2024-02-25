from tkinter import *
import random as r


startWindow = Tk()
cardDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = []

class Player:
    def __init__(self, *hand) -> None:
        self.hand = hand
        
    def startGame(self):
        mainWindow = Tk()
        mainWindow.geometry("600x600")
        startWindow.destroy()
        hitButton = Button(mainWindow, text="Hit", command=player1.hit)
        hitButton.pack()
        playerCardLabel = Label(mainWindow, text="0")
        playerCardLabel.pack()
        mainWindow.mainloop()
        
        deck = cardDeck
        for e in range(2):
            card = r.choice(deck)
            cards.append(card)

        player1.hand = cards
        cardTotal = cards[0] + cards[1]
        print(cardTotal)
        convertedList = str(player1.hand)
        playerCardLabel["text"] = convertedList

    def hit(self):
        print(player1.hand)
        playerCards = player1.hand
        newCard = r.choice(cardDeck)
        playerCards.append(newCard)

        print(playerCards)

        if sum(playerCards) > 21:
            print("Bust")

    def stand(self):
        pass

class Dealer(Player):
    pass

player1 = Player()
startGameButton = Button(startWindow, text="Start Game", command=player1.startGame)
startGameButton.pack()

if __name__ == '__main__':
    startWindow.mainloop()
