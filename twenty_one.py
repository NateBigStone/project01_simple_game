import random
import time

class Game():
    def __init__(self):
        #Initiates a new game with a new shuffled deck empty hands and no score. Then deals and plays
        self.new_deck = self.construct_deck()
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_score = 0
        self.player_score = 0
        self.player_stay = False
        self.new_hand()
        self.play_hands()

    def construct_deck(self):
        #An attempt at creating a deck of cards
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
        #Resets the hands and scores to empty and deals two new cards each and plays
        self.dealer_hand = []
        self.player_hand = []
        self.dealer_score = 0
        self.player_score = 0
        self.player_stay = False
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.play_hands()

    def play_hands(self):
        #Ensure there are enough cards left to play
        if len(self.new_deck) < 14:
            print("Shuffling Deck...")
            self.new_deck = self.construct_deck()
        #Prints the dealers hand
        dealer_string = "Dealer's Hand:\n"
        for card in self.dealer_hand:
            for key, value in card.items():
                dealer_string += f"{key} "
                self.dealer_score += value
        if len(self.dealer_hand) == 2 and not self.player_stay:
            #Obfuscates the dealers hand and score at first
            print(f"{dealer_string[:17]} ##")
        else:
            print(f"{dealer_string} \t\t\t\tTotal:{str(self.dealer_score)}")
        time.sleep(1)
        #Prints the players hand
        player_string = "Your Hand:\n"
        for card in self.player_hand:
            for key, value in card.items():
                player_string += f"{key} "
                self.player_score += value
        print(f"{player_string} \t\t\t\tTotal:{str(self.player_score)}")
        time.sleep(1)
        #Various rules for scores
        if self.dealer_score == 21 & self.player_score == 21:
            print("Push!")
            self.another_hand()
            return None
        elif self.dealer_score > 21:
            print("Dealer Busts!\nYou Win!")
            self.another_hand()
            return None
        elif self.dealer_score == 21:
            print(f"{dealer_string} \t\t\t\tTotal:{str(self.dealer_score)}")
            print("Dealer Wins!")
            self.another_hand()
            return None
        elif self.player_score == 21:
            print("Good Luck!")
            self.player_stay = True
        elif self.player_score > 21:
            print("BUSTED!")
            self.another_hand()
            return None
        elif self.player_stay:
            if self.dealer_score > 16:
                if self.player_score > self.dealer_score:
                    print("You Win!")
                else:
                    print("You Lose!")
                self.another_hand()
                return None
        self.hit()

    def deal_card(self,hand):
        draw = self.new_deck.pop()
        hand.append(draw)

    def hit(self):
        hit = "n"
        if not self.player_stay:
            hit = input("Hit? y/n:\n")
        if hit.strip().lower() == "y":
            self.deal_card(self.player_hand)
        else:
            self.player_stay = True
            if self.dealer_score < self.player_score:
                self.deal_card(self.dealer_hand)
        self.dealer_score = 0
        self.player_score = 0
        self.play_hands()

    def another_hand(self):
        another = input("Another Hand? y/n:\n")
        if another.strip().lower() == "y":
            self.new_hand()
        else:
            quit()


if __name__ == "__main__":
    game = Game()


"""
TODO: Have A's equal 11 or 1
Stretch goal: betting
"""