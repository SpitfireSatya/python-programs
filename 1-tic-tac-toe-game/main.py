
game_states = None
player1 = None
player2 = None
count = None


def print_grid():
    print(f' {game_states[0]} | {game_states[1]} | {game_states[2]}')
    print('-----------')
    print(f' {game_states[3]} | {game_states[4]} | {game_states[5]}')
    print('-----------')
    print(f' {game_states[6]} | {game_states[7]} | {game_states[8]}')


def check_rows():
    for i in range(0, 3):
        if game_states[3 * i] == game_states[3 * i + 1] == game_states[3 * i + 2]:
            return game_states[3 * i]
    return ''


def check_cols():
    for i in range(0, 3):
        if game_states[i] == game_states[i + 3] == game_states[i + 6]:
            return game_states[i]
    return ''


def check_diagonal():
    if game_states[0] == game_states[4] == game_states[8]:
        return game_states[0]
    elif game_states[2] == game_states[4] == game_states[6]:
        return game_states[2]
    else:
        return ''


def has_won():
    if check_rows() != '':
        return check_rows()

    if check_cols() != '':
        return check_cols()

    if check_diagonal() != '':
        return check_diagonal()


def initialize():
    global count, player1, player2, game_states
    game_states = [x for x in range(0, 9)]
    player1 = input('Will player 1 be X or O?')
    count = 0
    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'
        player1 = 'O'


def play_game():
    global count, player1, player2, game_states
    while count < 9 and not has_won():
        is_input_valid = False
        print_grid()
        while not is_input_valid:
            if count % 2 == 0:
                pos = int(input("Player 1, make your move"))
                char = player1
            else:
                pos = int(input("Player 2, make your move"))
                char = player2

            if type(game_states[pos]) is int and -1 < pos < 9:
                print(char)
                game_states[pos] = char
                is_input_valid = True
                count += 1
            else:
                print("Invalid position")

    print_grid()

    if has_won() == '' and count == 9:
        print("It was a tie")
    else:
        if has_won() == player1:
            print("Player 1 won!")
        elif has_won() == player2:
            print("Player 2 won!")
        else:
            print("The game was a tie")

    play_again = input("Would you like to play another game?(y/n)")
    if play_again.lower() == 'y':
        initialize_and_start()


def initialize_and_start():
    initialize()
    play_game()


initialize_and_start()
