import random

class Game():
    def __init__(self):
        self.new_deck = self.construct_deck()
        self.dealer_hand = []
        self.player_hand = []

    def construct_deck(self):
        suit = ["H","D","C","S"]
        royal = ["J","Q","K"]
        deck = []
        for s in suit:
            for n in range(2,11):
                deck.append({str(n)+s:n})
            for r in royal:
                deck.append({r+s:10})
            deck.append({"A"+s:11})
        random.shuffle(deck)
        return deck

    def deal(self):
        print(len(self.new_deck))
        draw_deal = self.new_deck.pop() #do rand len deck for more randomness
        draw_player = self.new_deck.pop()
        draw_deal2 = self.new_deck.pop()
        draw_player2 = self.new_deck.pop()
        print(f"\n{draw_deal} ## \n\n{draw_player} {draw_player2}")
        print(len(self.new_deck))

if __name__ == "__main__":
    game_one = Game()
    game_one.deal()


"""
When runing main create a new game class
The game will start with a new shuffled deck
There will be a player class that will have wins ( in the future chips) and a hand
There will be a dealer class that will have wins and a hand.

"""