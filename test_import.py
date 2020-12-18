
# Function to print Tic Tac Toe 3x3

def print_tic_tac_toe3x3(values):
    
    # Print the sample board

    print("\n")
    print("\t     |     |")
    print("\t  1  |  2  |  3")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  4  |  5  |  6")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  7  |  8  |  9")
    print("\t     |     |")
    print("\n")
    
    # Print the game board

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

#Function to print Tic Tac Toe 4x4

def print_tic_tac_toe4x4(values):
 
    #Print the sample board

    print("\n")
 
    print("\t     |     |     |")
 
    print("\t  1  |  2  |  3  |  4  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  5  |  6  |  7  |  8  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  9  |  10  |  11  |  12  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  13  |  14  |  15  |  16  ")
 
    print("\t     |     |     |")
 
    print("\n")
    
    #Print the game board
    
    print("\n")
 
    print("\t     |     |     |")
 
    print("\t  {}  |  {}  |  {}  |  {}  ".format(values[0], values[1], values[2],values[3]))
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  {}  |  {}  |  {}  |  {}  ".format(values[4], values[5], values[6], values[7]))
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  {}  |  {}  |  {}  |  {}  ".format(values[8], values[9], values[10],values[11]))
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  {}  |  {}  |  {}  |  {}  ".format(values[12], values[13], values[14],values[15]))
 
    print("\t     |     |     |")
 
    print("\n")

#Function to print Tic Tac Toe 5x5

def print_tic_tac_toe5x5(values):

    #Print the sample board

    print("\n")

    print("\t     |     |     |     |")

    print("\t  1  |  2  |  3  |  4  |  5  ")

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  6  |  7  |  8  |  9  |  10  ")

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  11 |  12 |  13 |  14 |  15  ")

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  16 |  17 |  18 |  19 |  20  ")

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  21 |  22 |  23 |  24 |  25  ")

    print("\t     |     |     |     |")

    print("\n")
  
    #Print the game board  
    
    print("\n")

    print("\t     |     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}  |  {}  ".format(values[0], values[1], values[2],values[3],values[4]))

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}  |  {}  ".format(values[5], values[6], values[7],values[8],values[9]))

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}  |  {}  ".format(values[10], values[11], values[12],values[13],values[14]))

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}  |  {}  ".format(values[15], values[16], values[17],values[18],values[19]))

    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")

    print("\t  {}  |  {}  |  {}  |  {}  |  {}  ".format(values[20], values[21], values[22],values[23],values[24]))

    print("\t     |     |     |     |")

    print("\n")

    

# Function to print the score-board

def print_scoreboard(score_board):

    print("\t--------------------------------")

    print("\t              SCOREBOARD       ")

    print("\t--------------------------------")

    players = list(score_board.keys())

    print("\t   ", players[0], "\t    ", score_board[players[0]])

    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Function to check if any player has won (3x3)

def check_win3x3(player_pos, cur_player):

    # All possible winning combinations

    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    # Loop to check if any winning combination is satisfied

    for x in soln:

        if all(y in player_pos[cur_player] for y in x):

            # Return True if any winning combination satisfies

            return True

    # Return False if no combination is satisfied       

    return False       

#Function to check if any player has won (4x4)

def check_win4x4(player_pos, cur_player):
    
    # All possible winning combinations
 
    soln = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16],[13, 10, 7, 4]]
 
    # Loop to check if any winning combination is satisfied
 
    for x in soln:
 
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
 
            return True

#Function to check if any player has won (5x5)

def check_win5x5(player_pos, cur_player):

    # All possible winning combinations
 
    soln = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25],[1, 7, 13, 19, 25],[21, 17, 13, 9, 5]]
 
    # Loop to check if any winning combination is satisfied
 
    for x in soln:
 
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
 
            return True
 
    # Return False if no combination is satisfied       


# Function to check if the game is drawn (3x3)

def check_draw3x3(player_pos):

    if len(player_pos['X']) + len(player_pos['O']) == 9:

        return True

    return False       

#Function to check if the game is drawn (4x4)

def check_draw4x4(player_pos):

    if len(player_pos['X']) + len(player_pos['O']) == 16:

        return True

    return False       

#Function to check if the game is drawn (5x5)

def check_draw5x5(player_pos):

    if len(player_pos['X']) + len(player_pos['O']) == 25:

        return True

    return False       


# Function for a single game of Tic Tac Toe (3x3)

def single_game3x3(cur_player):

    # Represents the Tic Tac Toe

    values = [' ' for x in range(9)]

     

    # Stores the positions occupied by X and O

    player_pos = {'X':[], 'O':[]}

     

    # Game Loop for a single game of Tic Tac Toe

    while True:

        print_tic_tac_toe3x3(values)

         

        # Try exception block for MOVE input

        try:

            print("Player ", cur_player, " turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input!!! Try Again")

            continue

        # Sanity check for MOVE inout

        if move < 1 or move > 9:

            print("Wrong Input!!! Try Again")

            continue

        # Check if the box is not occupied already

        if values[move-1] != ' ':

            print("Place already filled. Try again!!")

            continue

        # Update game information

        # Updating grid status

        values[move-1] = cur_player

        # Updating player positions

        player_pos[cur_player].append(move)

        # Function call for checking win

        if check_win3x3(player_pos, cur_player):

            print_tic_tac_toe3x3(values)

            print("Player ", cur_player, " has won the game!!")     

            print("\n")

            return cur_player

        # Function call for checking draw game

        if check_draw3x3(player_pos):

            print_tic_tac_toe3x3(values)

            print("Game Drawn")

            print("\n")

            return 'D'

        # Switch player moves

        if cur_player == 'X':

            cur_player = 'O'

        else:

            cur_player = 'X'

# Function for a single game of Tic Tac Toe (4x4)

def single_game4x4(cur_player):

    # Represents the Tic Tac Toe

    values = [' ' for x in range(16)]

     

    # Stores the positions occupied by X and O

    player_pos = {'X':[], 'O':[]}

     

    # Game Loop for a single game of Tic Tac Toe

    while True:

        print_tic_tac_toe4x4(values)

         

        # Try exception block for MOVE input

        try:

            print("Player ", cur_player, " turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input!!! Try Again")

            continue

        # Sanity check for MOVE inout

        if move < 1 or move > 16:

            print("Wrong Input!!! Try Again")

            continue

        # Check if the box is not occupied already

        if values[move-1] != ' ':

            print("Place already filled. Try again!!")

            continue

        # Update game information

        # Updating grid status

        values[move-1] = cur_player

        # Updating player positions

        player_pos[cur_player].append(move)

        # Function call for checking win

        if check_win4x4(player_pos, cur_player):

            print_tic_tac_toe4x4(values)

            print("Player ", cur_player, " has won the game!!")     

            print("\n")

            return cur_player

        # Function call for checking draw game

        if check_draw4x4(player_pos):

            print_tic_tac_toe4x4(values)

            print("Game Drawn")

            print("\n")

            return 'D'

        # Switch player moves

        if cur_player == 'X':

            cur_player = 'O'

        else:

            cur_player = 'X'

# Function for a single game of Tic Tac Toe (5x5)

def single_game5x5(cur_player):

    # Represents the Tic Tac Toe

    values = [' ' for x in range(25)]

     

    # Stores the positions occupied by X and O

    player_pos = {'X':[], 'O':[]}

     

    # Game Loop for a single game of Tic Tac Toe

    while True:

        print_tic_tac_toe5x5(values)

         

        # Try exception block for MOVE input

        try:

            print("Player ", cur_player, " turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input!!! Try Again")

            continue

        # Sanity check for MOVE inout

        if move < 1 or move > 25:

            print("Wrong Input!!! Try Again")

            continue

        # Check if the box is not occupied already

        if values[move-1] != ' ':

            print("Place already filled. Try again!!")

            continue

        # Update game information

        # Updating grid status

        values[move-1] = cur_player

        # Updating player positions

        player_pos[cur_player].append(move)

        # Function call for checking win

        if check_win5x5(player_pos, cur_player):

            print_tic_tac_toe5x5(values)

            print("Player ", cur_player, " has won the game!!")     

            print("\n")

            return cur_player

        # Function call for checking draw game

        if check_draw5x5(player_pos):

            print_tic_tac_toe5x5(values)

            print("Game Drawn")

            print("\n")

            return 'D'

        # Switch player moves

        if cur_player == 'X':

            cur_player = 'O'

        else:

            cur_player = 'X'

if __name__ == "__main__":

    print("Player 1")

    player1 = input("Enter the name : ")

    print("\n")

    print("Player 2")

    player2 = input("Enter the name : ")

    print("\n")

     

    # Stores the player who chooses X and O

    cur_player = player1

    # Stores the choice of players

    player_choice = {'X' : "", 'O' : ""}

    # Stores the options

    options = ['X', 'O']

    # Stores the scoreboard

    score_board = {player1: 0, player2: 0}

    print_scoreboard(score_board)

    # Game Loop for a series of Tic Tac Toe

    # The loop runs until the players quit

    while True:

        # Player choice Menu

        print("Turn to choose for", cur_player)

        print("Enter 1 for X")

        print("Enter 2 for O")

        print("Enter 3 to Quit")

        # Try exception for CHOICE input

        try:

            choice = int(input())   

        except ValueError:

            print("Wrong Input!!! Try Again\n")

            continue

        # Conditions for player choice  

        if choice == 1:

            player_choice['X'] = cur_player

            if cur_player == player1:

                player_choice['O'] = player2

            else:

                player_choice['O'] = player1

        elif choice == 2:

            player_choice['O'] = cur_player

            if cur_player == player1:

                player_choice['X'] = player2

            else:

                player_choice['X'] = player1

         

        elif choice == 3:

            print("Final Scores")

            print_scoreboard(score_board)

            break  

        else:

            print("Wrong Choice!!!! Try Again\n")

        # Player choice of difficulties (3x3,4x4,5x5)
        
        print("Turn to choose the difficulty for", cur_player)

        print("Enter 1 for 3x3 (Easy)")

        print("Enter 2 for 4x4 (Medium)")

        print("Enter 3 for 5x5 (Hard)")

        #Try exception for player level choice
        
        try:

            level_choice = int(input())   

        except ValueError:

            print("Wrong Input!!! Try Again\n")

            continue

        # Conditions for player choice  

        if level_choice == 1:

            winner = single_game3x3(options[choice-1])

        elif level_choice == 2:

            winner = single_game4x4(options[choice-1])

        elif level_choice == 3:

            winner = single_game5x5(options[choice-1])
         

        # Edits the scoreboard according to the winner

        if winner != 'D' :

            player_won = player_choice[winner]

            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)

        # Switch player who chooses X or O

        if cur_player == player1:

            cur_player = player2

        else:

            cur_player = player1
