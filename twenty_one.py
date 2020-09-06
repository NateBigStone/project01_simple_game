import random

class Game():
    def __init__(self):
        self.new_deck = self.construct_deck()
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_score = 0
        self.player_score = 0

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

    def new_hand(self):
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_score = 0
        self.player_score = 0

    def play_hands(self):
        dealer_string = "Dealer's Hand:\n"
        for card in self.dealer_hand:
            for key, value in card.items():
                dealer_string += f"{key} "
                self.dealer_score += value
        print(f"{dealer_string} \t\t\t\tTotal:{str(self.dealer_score)}")
        player_string = "Your Hand:\n"
        for card in self.player_hand:
            for key, value in card.items():
                player_string += f"{key} "
                self.player_score += value
        print(f"{player_string} \t\t\t\tTotal:{str(self.player_score)}")
        if self.dealer_score == 21:
            print("Dealer Wins!")
            return None
        if self.player_score == 21:
            print("Good Luck!")
            return None
        self.dealer_score = 0
        self.player_score = 0
        self.hit()

    def deal_card(self,hand):
        draw = self.new_deck.pop()
        hand.append(draw)

    def hit(self):
        hit = input("Hit? y/n:\n")
        if hit.strip().lower() == "y":
            self.deal_card(game.player_hand)
            self.play_hands()

    def another_hand(self):
        another = input("Another Hand? y/n:\n")
        if another.strip().lower() == "y":
            self.new_hand()

if __name__ == "__main__":
    game = Game()
    game.deal_card(game.dealer_hand)
    game.deal_card(game.player_hand)
    game.deal_card(game.dealer_hand)
    game.deal_card(game.player_hand)
    game.play_hands()

"""
TODO: Game rules
"""