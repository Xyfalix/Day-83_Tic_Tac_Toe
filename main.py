board = ([' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] )

players = ['X', 'O']

game_on = True

def print_board():
    row_separator = '   -----------------'
    print('     0     1     2  ')
    print(row_separator)
    for row in range(len(board)):
        print(f"{row}    {board[row][0]}  |  {board[row][1]}  |  {board[row][2]}  ")
        print(row_separator)


def position_selector(player_selection):
    row_input = input(f"Player {player_selection+1}, please select a row (0-2) to place"
                      f" your '{players[player_selection]}': ")

    # check for invalid row inputs
    if row_input not in ['0', '1', '2']:
        print("You have keyed in an invalid row, please try again!")
        return position_selector(player_selection)

    col_input = input(f"Player {player_selection+1}, please select a column (0-2) to place"
                      f" your '{players[player_selection]}': ")

    # check for invalid column inputs
    if col_input not in ['0', '1', '2']:
        print("You have keyed in an invalid column, please try again!")
        return position_selector(player_selection)

    # check that specific row column coordinate has not been filled up
    row_input = int(row_input)
    print(row_input)
    col_input = int(col_input)
    print(col_input)
    if board[row_input][col_input] == ' ':
        board[row_input][col_input] = players[player_selection]
        print_board()
    else:
        print("That row column coordinate has already been filled up, please try again!")
        return position_selector(player_selection)


def win_check():
    global game_on
    # check if any row contains all 'X' or 'O'
    for player in players:
        for row in board:
            if row == [player, player, player]:
                # get index of symbol to determine player that won
                index = players.index(player)
                print(f"Player {index + 1} has won the game!")
                game_on = False

    # check if any column contains all 'X' or 'O'
    for player in players:
        for col_idx in range(3):
            if [row[col_idx] for row in board] == [player, player, player]:
                # get index of symbol to determine player that won
                index = players.index(player)
                print(f"Player {index + 1} has won the game!")
                game_on = False

    # check if diagonal from top left to btm right contains all 'X' or 'O'
    for player in players:
        if [board[i][i] for i in range(3)] == [player, player, player]:
            # get index of symbol to determine player that won
            index = players.index(player)
            print(f"Player {index + 1} has won the game!")
            game_on = False

    # check if diagonal from top right to btm left contains all 'X' or 'O'
    for player in players:
        if [board[i][2 - i] for i in range(3)] == [player, player, player]:
            # get index of symbol to determine player that won
            index = players.index(player)
            print(f"Player {index + 1} has won the game!")
            game_on = False


# check if board is full, indicating a draw.
def stalemate():
    global game_on
    if any(' ' in row for row in board):
        pass
    else:
        print("All spaces on the board are filled, it's a draw!")
        game_on = False


def tic_tac_toe():
    player_selection = 0
    while game_on:
        # run the position_selector function for player to select position to place 'X' or 'O'
        position_selector(player_selection)

        # swap first player to second player
        if player_selection == 0:
            player_selection = 1
        # swap second player to first player
        else:
            player_selection = 0

        # check if either player has won the game
        win_check()

        # check if board is full, indicating a draw.
        stalemate()

print("Welcome to Nicholas's text based version of Tic Tac Toe! The blank board is shown below for reference."
      "\nThe rows and columns are numbered 0 to 2 for subsequent input requests.")
print_board()
tic_tac_toe()

#  TODO 1: Create ASCII Tic Tac Toe Board
#  TODO 2: Set Player 1 as the default and assign either 'X' or 'O'
#  TODO 3: Prompt Player 1 to choose a row (0-2) and column (0-2) to place 'X' or 'O'
#  TODO 4: Check that row and column input is valid, and that it is not already filled up.
#  TODO 4: Switch control over to Player 2 and perform step 3 but for player 2
#  TODO 5: Perform a check to see if either player has won, win condition is to check if
#   the same symbols exist in the same row, same column, or diagonally
#  TODO 6: If game is won or drawn, reset and ask if players want a rematch
