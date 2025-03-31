import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(b):
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")

def get_winner(board):
    #Check rows
    x_count = 0
    o_count = 0
    for i in range(0, len(board), 3):
        for j in range(i, i+3):
            if not board[j].isdigit():
                if board[j] == 'X':
                    x_count += 1
                else:
                    o_count += 1
        if x_count == 3:
            return 'X'
        if o_count == 3:
            return 'O'
        x_count = 0
        o_count = 0

    #Check columns
    for i in range(0, 3):
        x_count = 0
        o_count = 0
        for j in range(i, i+7, 3):
            if not board[j].isdigit():
                if board[j] == 'X':
                    x_count += 1
                else:
                    o_count += 1
        if x_count == 3:
            return 'X'
        if o_count == 3:
            return 'O'
        x_count = 0
        o_count = 0

    #Check diagonals
    increment = 4
    for i in range(0, 3, 2):
        for j in range(i, 9-i, increment):
            if not board[j].isdigit():
                if board[j] == 'X':
                    x_count += 1
                else:
                    o_count += 1
        if x_count == 3:
            return 'X'
        if o_count == 3:
            return 'O'
        increment -= 2
        x_count = 0
        o_count = 0
    return None

#Gets the position to put the player's letter on the board based on player input.
def get_pos():
    while True:
        pos = input("Pick a spot (0-8): ")
        if pos.isdigit():
            if -1 < int(pos) < 9:
                return int(pos)
            print("Spot too big or small. Spot needs to be (0-8).")
        print("Invalid input. Try again.")
            

def play():
    board = [str(i) for i in range(9)] #Initialize board
    player = "X"
    while any(cell.isdigit() for cell in board): #Repeat while there is still empty space on the board
        clear_screen()
        print("Tic-Tac-Toe\n")
        print_board(board)
        print(f"\n{player}'s turn!")
        pos = get_pos() #Get position to play on the board
        if board[pos].isdigit():
            board[pos] = player
            winner_result = get_winner(board)
            #A player wins is this statement is true
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                print_board(board)
                print(f"\n{winner_result} wins!")
                return
            if player== "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Spot is taken. Try again.")

    #No players won.
    clear_screen()
    print("Tic-Tac-Toe\n")
    print_board(board)
    print("\nIt's a draw!")

play()