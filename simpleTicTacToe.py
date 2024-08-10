board = ['Garbage','','','','','','','','','',]


def showHint():

    print('--------------------------------- Tic Tac Toe ----------------------------------\n')

    print('You need to select the position according to this hint,\n' )
    print('\t\t1  2  3' )
    print('\t\t4  5  6' )
    print('\t\t7  8  9\n' )


def showBoard(boardVal):
    print(f"\t\t{'-' if boardVal[1] == '' else boardVal[1]} {'-' if boardVal[2] == '' else boardVal[2]} {'-' if boardVal[3] == '' else boardVal[3]}")
    print(f"\t\t{'-' if boardVal[4] == '' else boardVal[4]} {' -' if boardVal[5] == '' else boardVal[5]} {'-' if boardVal[6] == '' else boardVal[6]}")
    print(f"\t\t{'-' if boardVal[7] == '' else boardVal[7]} {'-' if boardVal[8] == '' else boardVal[8]} {'-' if boardVal[9] == '' else boardVal[9]}")



def isBoardFull():
    if '' in board:
        return False
    else:
        return True



def changeTurn(currentTurn):
    if currentTurn == 'X':
        return 'O'
    elif currentTurn == 'O':
        return 'X'


def winner(player, board):
    return (board[1] == board[2] == board[3] == player or 
            board[4] == board[5] == board[6] == player or 
            board[7] == board[8] == board[9] == player or 
            board[1] == board[4] == board[7] == player or 
            board[2] == board[5] == board[8] == player or 
            board[3] == board[6] == board[9] == player or 
            board[1] == board[5] == board[9] == player or 
            board[7] == board[5] == board[3] == player)
def placeMark(player, board):
    while True:
        showBoard(board)
        print(f'\nIt\'s {player}\'s turn,\n')
        position = int(input('Select your desired position:'))
        
        if position >= 10 or position <= 0 or position == '':
            print('\nInput should be 1 - 9')

        elif board[position] != '':
            print('\nThe position is already taken')


        elif isBoardFull():
            print('\nMatch Drawn')
            showBoard(board)
            break

        else:
            board[position] = player
            player = changeTurn(player)
            
            if(winner('X', board)):
                print('\n----------- X is the winner -------------\n')
                showBoard(board)
                break
                    
            elif(winner('O', board)):
                print('\n----------- O is the winner -------------\n')
                showBoard(board)
                break
            
            
            
    again = input("Wanna try again? (y/n): ")
    while True:
        if again == 'y':
            main()
        elif again == 'n':
            break
        else:
            continue


def main(board = board):
    board = ['Trash','','','','','','','','','',]
    player = 'X'
    showHint()
    placeMark(player, board)

main(board)
