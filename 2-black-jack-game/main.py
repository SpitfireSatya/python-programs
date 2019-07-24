
from os import system
from models.deck import Deck
from models.player import Player


def initialization():
    deck = Deck()
    deck.shuffle()
    player = Player()
    dealer = Player()

    start_game(deck, player, dealer)


def initial_draw(deck, player, dealer):
    player.hit(deck.draw_card())
    player.hit(deck.draw_card())
    dealer.hit(deck.draw_card())
    dealer.hit(deck.draw_card())


def start_game(deck, player, dealer):
    initial_draw(deck, player, dealer)
    print('Player cards: ' + ' '.join(player.get_cards()))
    print('Total: ' + str(player.get_score()))

    choice = None
    while not player.is_player_bust():
        choice = input('Would you like another card? (h/s) ')
        if choice == 'h':
            player.hit(deck.draw_card())
            print('Player cards: ' + ' '.join(player.get_cards()))
            print('Total: ' + str(player.get_score()))
        else:
            break

    print('Dealer cards: ' + ' '.join(dealer.get_cards()))
    print('Total: ' + str(dealer.get_score()))

    if player.is_player_bust():
        print('Player busted. Dealer Wins!!')
    else:
        while dealer.get_score() <= player.get_score():
            dealer.hit(deck.draw_card())
            print('Dealer cards: ' + ' '.join(dealer.get_cards()))
            print('Total: ' + str(dealer.get_score()))
        print('Player cards: ' + ' '.join(player.get_cards()))
        print('Total: ' + str(player.get_score()))
        if dealer.is_player_bust():
            print('Dealer busted. Player Wins!!')
        elif dealer.get_score() == player.get_score():
            print("Both players have the same score. It's a tie")
        else:
            print("Dealer Wins!!")

    play_again = input("Would you like to play again?(y/n) ")
    if play_again == 'y':
        _ = system('cls')
        initialization()


initialization()
