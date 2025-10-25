import random as rn

# Empty board
lst = ['Trash', '-', '-', '-', '-', '-', '-', '-', '-', '-']


# To show guide of the game
def showHint():
    print('------------- Tic Tac Toe ------------\n\n')

    print('Enter your desired position according to this hint,\n')
    print('\t\t1  2  3')
    print('\t\t4  5  6')
    print('\t\t7  8  9')


# Prints the current state of board
def showBoard():
    print(f'\n\t\t{lst[1]}  {lst[2]}  {lst[3]}')
    print(f'\t\t{lst[4]}  {lst[5]}  {lst[6]}')
    print(f'\t\t{lst[7]}  {lst[8]}  {lst[9]}')


# Changes player turns
def swapPlayer(turn):
    if turn == 'X':
        return 'O'
    if turn == 'O':
        return 'X'


# Checks if anyone won
def checkWinner(currentPlayer):
    return (lst[1] == lst[2] == lst[3] == currentPlayer or
            lst[4] == lst[5] == lst[6] == currentPlayer or
            lst[7] == lst[8] == lst[9] == currentPlayer or
            lst[1] == lst[4] == lst[7] == currentPlayer or
            lst[2] == lst[5] == lst[8] == currentPlayer or
            lst[3] == lst[6] == lst[9] == currentPlayer or
            lst[1] == lst[5] == lst[9] == currentPlayer or
            lst[3] == lst[5] == lst[7] == currentPlayer)


# Prevents user from winning the match
def isAboutToWin():
    return (
        1 if lst[2] == 'X' and lst[3] == 'X' else 0 or
        1 if lst[4] == 'X' and lst[7] == 'X' else 0 or
        1 if lst[5] == 'X' and lst[9] == 'X' else 0 or

        2 if lst[1] == 'X' and lst[3] == 'X' else 0 or
        2 if lst[8] == 'X' and lst[5] == 'X' else 0 or

        3 if lst[1] == 'X' and lst[2] == 'X' else 0 or
        3 if lst[6] == 'X' and lst[9] == 'X' else 0 or
        3 if lst[7] == 'X' and lst[5] == 'X' else 0 or

        4 if lst[5] == 'X' and lst[6] == 'X' else 0 or
        4 if lst[1] == 'X' and lst[7] == 'X' else 0 or

        5 if lst[2] == 'X' and lst[8] == 'X' else 0 or
        5 if lst[4] == 'X' and lst[6] == 'X' else 0 or
        5 if lst[1] == 'X' and lst[9] == 'X' else 0 or
        5 if lst[3] == 'X' and lst[7] == 'X' else 0 or

        6 if lst[3] == 'X' and lst[9] == 'X' else 0 or
        6 if lst[4] == 'X' and lst[5] == 'X' else 0 or

        7 if lst[1] == 'X' and lst[4] == 'X' else 0 or
        7 if lst[8] == 'X' and lst[9] == 'X' else 0 or
        7 if lst[3] == 'X' and lst[5] == 'X' else 0 or

        8 if lst[2] == 'X' and lst[5] == 'X' else 0 or
        8 if lst[7] == 'X' and lst[9] == 'X' else 0 or

        9 if lst[3] == 'X' and lst[6] == 'X' else 0 or
        9 if lst[7] == 'X' and lst[8] == 'X' else 0 or
        9 if lst[1] == 'X' and lst[5] == 'X' else 0)


# Checks if the given input already taken
def alreadyTaken(position):
    return True if lst[position] != '-' else False


# Bot chooses random position if the user is not about to win
def randomMark():
    while True:
        pos = rn.randint(1, 9)
        if lst[pos] == '-':
            return pos
        else:
            continue

# Turn of the bot
def computerMark():
    # Runs until the bot chooses a valid position
    while True:
        position = randomMark()

        if isAboutToWin() != 0:
            print(isAboutToWin())
            position = isAboutToWin()
            if alreadyTaken(position):
                position = randomMark()
                lst[position] = 'O'
                showBoard()
                break

            else:
                lst[position] = 'O'
                showBoard()
                break

        if alreadyTaken(position):
            continue

        if lst[position] == '-':
            lst[position] = 'O'
            showBoard()
            break

# Turn of the player
def playerMark(player):
    # Runs until the player chooses a valid position
    while True:
        print(f'\nPlayer {player}\'s turn')
        position = int(input('Choose here: '))

        if position > 9 or position < 1:
            print('\nInput should be between 1 - 9')

        if lst[position] != '-':
            print('\nThe position is Already taken,')
            print('Choose wisely,')
            showBoard()

        else:
            lst[position] = player
            showBoard()
            if checkWinner(player):
                print(f'\n------- Player {player} is the winner -------')
                exit()
            break

        if checkWinner(player):
            break


# Puts mark in the given position
def placeMark():
    player = 'X'
    while True:
        if checkWinner(player):
            print(f'\n------- Player {player} is the winner -------')
            break

        elif '-' not in lst and checkWinner(player) is False:
            print("Match drawn!!")
            break

        elif player == 'O':
            print(f'\nPlayer {player}\'s turn')
            computerMark()

        elif player == 'X':
            playerMark(player)

        player = swapPlayer(player)


if __name__ == '__main__':
    showHint()
    placeMark()

