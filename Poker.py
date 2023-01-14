##Texas hold em with a single deck no jokers, atleast 3 players required
import random

class Player:

    number_of_players = 0
    def __init__(self, name, chips = 100):
        Player.number_of_players += 1
        self.name = name
        self.id = Player.number_of_players
        self.hand = []
        self.chips = chips
        self.is_all_in == False
        self.max_win = False
        self.is_dealer = False
        self.is_small_blind = False
        self.is_big_blind = False
        self.current_bet = 0

    def recieve(self, card):
        self.hand.append(card)

    def call(self, game, bet):
        if self.chips <= bet:
            print("Player: "+self.name+" ("+self.id+") "+" has not got enough chips to call, going all in.")
            self.all_in(game)
        else:
            self.chips -= bet
            game.pot += bet
            print("Player: "+self.name+" ("+self.id+") "+" has called "+bet+" chips.")
            self.current_bet = bet

    def raise_to(self, game, bet):
        if self.chips <= ((game.current_highest_bet + bet) - self.current_bet):
            print("Player: "+self.name+" ("+self.id+") "+" has not got enough chips to raise, going all in.")
            self.all_in(game)
        else:
            self.chips -= ((game.current_highest_bet + bet) - self.current_bet)
            game.pot += ((game.current_highest_bet + bet) - self.current_bet)
            game.current_highest_bet += bet
            game.current_highest_bet = self.current_bet
            print("Player: "+self.name+" ("+self.id+") "+"has raised to"+game.current_highest_bet+" chips.")
    
    def fold(self, game):
        game.players.remove(self)
        print("Player: "+self.name+" ("+self.id+") "+"has folded.")

    def all_in(self, game):
        self.max_win = game.pot
        if game.current_lowest_bet < self.chips:
            game.current_lowest_bet = self.chips
        game.pot += self.chips
        #WAY TO HANDLE ALL IN /// SIDE POTS 
        game.current_highest_bet = self.chips
        self.current_bet = game.current_highest_bet
        self.chips = 0
        self.is_all_in == True
        print("Player: "+self.name+" ("+self.id+") "+"is all in with: "+str(game.current_highest_bet)+" chips!")

class Deck:

    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def deal(self):
        random.shuffle(self.deck)
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        if self.value == 1:
            self.face = "Ace"
        elif self.value == 11:
            self.face = "Jack"
        elif self.value == 12:
            self.face = "Queen"
        elif self.value == 13:
            self.face = "King"

    def __repr__(self): 
        return self.face+" of "+self.suit

class Game:

    def __init__(self, players):
        self.deck_in_play =  Deck()
        self.players = players 
        self.pot = 0
        self.current_highest_bet = False
        self.community_cards = []
        self.round1()

    def round1(self):
        for player in self.players:
            player.current_bet = 0
        random.shuffle(self.players)
        for player in self.players:
            for i in range(2):
                player.recieve(self.deck_in_play.deal())
            print("Dealt 2 cards to player: "+player.name+" ("+str(player.id)+") ")
        self.players[0].is_dealer = True
        self.players[1].is_small_blind = True
        self.players[2].is_big_blind = True
        self.players.append(self.players.pop(self.players[0]))
        self.player_decision()
        self.win_check()

    def round2(self):
        for player in self.player:
            player.current_bet = 0
        self.current_highest_bet = False
        for i in range(3):
            self.community_cards.append(self.deck_in_play.deal())
        print("The community cards are: "+str(self.community_cards))
        self.player_decision()
        self.win_check()

    def round3(self):
        for player in self.player:
            player.current_bet = 0
        self.current_highest_bet = False
        self.community_cards.append(self.deck_in_play.deal())
        print("The community cards are: "+str(self.community_cards))
        self.player_decision()
        self.win_check()

    def round4(self):
        for player in self.player:
            player.current_bet = 0
        self.current_highest_bet = False
        self.community_cards.append(self.deck_in_play.deal())
        print("The community cards are: "+str(self.community_cards))
        self.player_decision()
        self.win_check()

    def player_decision(self):
         for player in self.players:

            if player.is_all_in == True:
                print("Player: "+player.name+" ("+str(player.id)+") "+" is all in")
                continue

            if (player.current_bet != self.current_highest_bet):
                for player in self.players:

                    if self.blind_paid == False:
                        if player.is_small_blind == True:
                            print("Player: "+player.name+" ("+str(player.id)+") "+" is the small blind")
                            print("You must place a small blind of 1 chip")
                            player.chips -= 1
                            self.pot += 1
                            self.current_highest_bet = 1
                            continue
                        if player.is_big_blind == True:
                            print("Player: "+player.name+" ("+str(player.id)+") "+" is the big blind")
                            print("You must place a big blind of 2 chips")
                            player.chips -= 2
                            self.pot += 2
                            self.current_highest_bet = 2
                            self.blind_paid = True
                            continue

                    if self.blind_paid == True:
                        if player.is_dealer == True:
                            print("Player: "+player.name+" ("+str(player.id)+") "+" is the dealer")
                        if self.current_highest_bet == player.current_bet:
                            while player.action != "1" or "2" or "3" or "4" or "5":
                                print("Player: "+player.name+" ("+str(player.id)+")"+" please select an action with the number keys.")
                                player.action = input("""Possible actions:
                                                            1: Call
                                                            2: Raise
                                                            3: Check
                                                            4: All in
                                                            5: Fold
                                                            6: View cards
                                                            7: View chips
                                                            8: View current bet
                                                            Enter action:""")
                                if player.action == "6":
                                    print("Player: "+player.name+" ("+player.id+") "+" has the following cards in hand: "+str(player.hand))
                                    print("The community cards are: "+str(self.community_cards))
                                elif player.action == "7":
                                    for player in self.players:
                                        print("Player: "+player.name+" ("+str(player.id)+") "+" has "+str(player.chips)+" chips.")
                                elif player.action == "8":
                                    print("Current bet: "+str(self.current_highest_bet)+"\nTotal pot: "+str(self.pot))
                            action_check(player)
                            
                        else:
                            while player.action != "1" or "2" or "4" or "5":
                                print("Player: "+player.name+" ("+str(player.id)+")"+" please select an action with the number keys.")
                                player.action = input("""Possible actions:
                                                        1: Call
                                                        2: Raise
                                                        3: \u0336C\u0336h\u0336e\u0336c\u0336k 
                                                        4: All in
                                                        5: Fold
                                                        6: View cards
                                                        7: View chips
                                                        8: View current bet
                                                        Enter action:""")
                                if player.action == "6":
                                    print("Player: "+player.name+" ("+str(player.id)+") "+" has the following cards in hand: "+str(player.hand))
                                    print("The community cards are: "+str(self.community_cards))
                                elif player.action == "7":
                                    for player in self.players:
                                        print("Player: "+player.name+" ("+player.id+") "+" has "+str(player.chips)+" chips.")
                                elif player.action == "8":
                                    print("Current bet: "+str(self.current_highest_bet)+"\nTotal pot: "+str(self.pot))
                            action_check(player) 

    def action_check(self, player):
        if player.action == "1":
            player.call(self, self.current_highest_bet)
        elif player.action == "2":
            raise_amount = input("Current bet: "+str(self.current_highest_bet)+"\nEnter amount to raise: ")
            player.raise_to(self, raise_amount)
        elif player.action == "3":
            pass
        elif player.action == "4":
            player.all_in(self)
        elif player.action == "5":
            player.fold(self)

    def win_check(self):
        winner = []
        biggest_hand_value = float(0.0)

        if len(self.players) == 1:
            #self.players[0] is the winner
            pass
        else:
            for player in self.players:
                hand_creater(player)
                if player_hand_value > biggest_hand_value:
                    biggest_hand_value = player.hand_value
                    winner = list(player)
                elif player.hand_value == biggest_hand_value:
                    winner.append(player)

        for player in winner:
            #use floor divison for easier chip numbers
            player.chips += (self.pot // len(winner))
            print("Player: "+player.name+" ("+str(player.id)+") "+" has won "+str(self.pot // len(winner))+" chips.")
            print("For a new total of: "+str(player.chips)+" chips")

    def hand_creater(self, player):


###
###TESTS BELOW###        
###


