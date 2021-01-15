# Functions to print the different boards depending on the level

def board3x3(values):
    
    """
    This function will print two boards (3x3 - easy level) : the upper board will show the different positions and the other will be the actual playing boards
    Arguments : values (player selection)
    Returns : two boards (3x3)
    """
    
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


def board4x4(values):
 
    """
    This function will print two boards (4x4 - medium level) : the upper board will show the different positions and the other will be the actual playing boards
    Arguments : values (player selection)
    Returns : two boards (4x4)
    """

    print("\n")
 
    print("\t     |     |     |")
 
    print("\t  1  |  2  |  3  |  4  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  5  |  6  |  7  |  8  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  9  |  10 |  11 |  12  ")
 
    print('\t_____|_____|_____|_____')
 
    print("\t     |     |     |")
 
    print("\t  13 |  14 |  15 |  16  ")
 
    print("\t     |     |     |")
 
    print("\n")
    
    
    
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



def board5x5(values):

    """
    This function will print two boards (5x5 - hard level) : the upper board will show the different positions and the other will be the actual playing boards
    Arguments : values (player selection)
    Returns : two boards (5x5)
    """
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

    

# Function of the score-board

def scoreboard(score_board):

    """
    This function will show the scoreboard, the number of victory of each players 
    Arguments : score_board
    Returns : Scoreboard
    """
    print("\t--------------------------------")

    print("\t           SCOREBOARD           ")

    print("\t--------------------------------")

    players = list(score_board.keys())

    print("\t   ", players[0], "\t    ", score_board[players[0]])

    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Function to check if anyone has won

def winner3x3(player, current_player):

    """
    This function will determine the winner of the actual game, by checking the different winning combinations (3x3 game)
    Arguments : current_player, player
    Returns : Boolean : True --> if there is a winner
                        False --> if there is no winner
                        
    """

    # The possible winning combinations

    combo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    # Loop to check if any winning combination happened

    for x in combo:

        if all(y in player[current_player] for y in x):

            # Return True if any winning combination happens

            return True

    # Return False if no winning combination happens       

    return False       

def winner4x4(player, current_player):
    
    """
    This function will determine the winner of the actual game, by checking the different winning combinations (4x4 game)
    Arguments : player, current_player
    Returns : Boolean : True --> if there is a winner
                        False --> if there is no winner
                        
    """
    # The possible winning combinations
 
    combo = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16],[13, 10, 7, 4]]
 
    # Loop to check if any winning combination happens
 
    for x in combo:
 
        if all(y in player[current_player] for y in x):
 
 
            return True

def winner5x5(player, current_player):
    
    """
    This function will determine the winner of the actual game, by checking the different winning combinations (5x5 game)
    Arguments : player, current_player
    Returns : Boolean : True --> if there is a winner
                        False --> if there is no winner
                        
    """

    # The possible winning combinations
 
    combo = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25],[1, 7, 13, 19, 25],[21, 17, 13, 9, 5]]
 
    # Loop to check if any winning combination is happens
 
    for x in combo:
 
        if all(y in player[current_player] for y in x):
 
 
            return True
    


# Function to check if there is a draw

def draw3x3(player):

    """
    This function will determine if the game ends in a draw : all positions are filled (without a winner) (3x3 game)
    Arguments : player
    Returns : Boolean : True --> if there is a draw
                        False --> if there is no draw
                        
    """
    if len(player['X']) + len(player['O']) == 9:

        return True

    return False       

def draw4x4(player):
    """
    This function will determine if the game ends in a draw : all positions are filled (without a winner) (4x4 game)
    Arguments : player
    Returns : Boolean : True --> if there is a draw
                        False --> if there is no draw
                        
    """

    if len(player['X']) + len(player['O']) == 16:

        return True

    return False       

def draw5x5(player):
    
    """
    This function will determine if the game ends in a draw : all positions are filled (without a winner) (5x5 game)
    Arguments : player
    Returns : Boolean : True --> if there is a draw
                        False --> if there is no draw
                        
    """

    if len(player['X']) + len(player['O']) == 25:

        return True

    return False       


# Function for a single round

def one_round3x3(current_player):

    """
    This function will run a single game (of 3x3 tictactoe)
    Arguments : current_player
    Returns : the winner of the game : current_player
              or when it's a draw : a message to signal the draw
                        
    """

    values = [' ' for x in range(9)]

     
    # Stores the positions of X and O

    player = {'X':[], 'O':[]}

     

    # Loop of a single round

    while True:

        board3x3(values)

         

        # define the limits of input

        try:

            print("Player ", current_player, "'s turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input! Try Again")

            continue

        # check if box number input is possible

        if move < 1 or move > 9:

            print("Wrong Input! Try Again")

            continue

        # Check if the box is not occupied already

        if values[move-1] != ' ':

            print("Place already filled. Try again!")

            continue


        # Updating grid status

        values[move-1] = current_player

        # Updating player positions

        player[current_player].append(move)

        # Function call for checking win

        if winner3x3(player, current_player):

            board3x3(values)

            print("Player ", current_player, " has won the game congratulations!")     

            print("\n")

            return current_player

        # calling the function that checks for a draw

        if draw3x3(player):

            board3x3(values)

            print("it's a Draw")

            print("\n")

            return 'D'

        # distribution of X and O between players

        if current_player == 'X':

            current_player = 'O'

        else:

            current_player = 'X'

#same comments for the 4x4 and 5x5 levels 

def one_round4x4(current_player):

    """
    This function will run a single game (of 4x4 tictactoe)
    Arguments : current_player
    Returns : the winner of the game : current_player
              or when it's a draw : a message to signal the draw
                        
    """

    values = [' ' for x in range(16)]

     
    player = {'X':[], 'O':[]}

     

    while True:

        board4x4(values)

         

        try:

            print("Player ", current_player, "'s turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input! Try Again")

            continue


        if move < 1 or move > 16:

            print("Wrong Input! Try Again")

            continue


        if values[move-1] != ' ':

            print("Place already filled. Try again!")

            continue

        # Update game information


        values[move-1] = current_player


        player[current_player].append(move)


        if winner4x4(player, current_player):

            board4x4(values)

            print("Player ", current_player, " has won the game congratulations!")     

            print("\n")

            return current_player


        if draw4x4(player):

            board4x4(values)

            print("it's a draw")

            print("\n")

            return 'D'


        if current_player == 'X':

            current_player = 'O'

        else:

            current_player = 'X'

def one_round5x5(current_player):

    """
    This function will run a single game (of 5x5 tictactoe)
    Arguments : current_player
    Returns : the winner of the game : current_player
              or when it's a draw : a message to signal the draw
                        
    """

    values = [' ' for x in range(25)]


    player = {'X':[], 'O':[]}

     


    while True:

        board5x5(values)


        try:

            print("Player ", current_player, "'s turn. Which box? : ", end="")

            move = int(input())

        except ValueError:

            print("Wrong Input! Try Again")

            continue

        # Sanity check for MOVE inout

        if move < 1 or move > 25:

            print("Wrong Input! Try Again")

            continue

        # Check if the box is not occupied already

        if values[move-1] != ' ':

            print("Place already filled. Try again!")

            continue

        # Update game information


        values[move-1] = current_player


        player[current_player].append(move)


        if winner5x5(player, current_player):

            board5x5(values)

            print("Player ", current_player, " has won the game congratulations!")     

            print("\n")

            return current_player


        if draw5x5(player):

            board5x5(values)

            print("it's a draw")

            print("\n")

            return 'D'


        if current_player == 'X':

            current_player = 'O'

        else:

            current_player = 'X'

if __name__ == "__main__":

    print('---------------------------WELCOME TO THE TIC TAC TOE GAME-----------------------------\n')

    print('---------------------------Created by Oumaima and Sohaib - ESIEE 2020------------------\n')

    print("Player 1")

    player1 = input("Enter your name : ")

    print("\n")

    print("Player 2")

    player2 = input("Enter your name : ")

    print("\n")

     

    # Storing what the players choose from X or O 

    current_player = player1


    player_choice = {'X' : "", 'O' : ""}

    # Storing the options

    options = ['X', 'O']

    # Stores the scoreboard

    score_board = {player1: 0, player2: 0}

    scoreboard(score_board)

    # Game Loop for a bunch of rounds 

    # The loop runs until the players quit

    while True:

        # Player game Menu

        print("Turn to choose for", current_player)

        print("Enter 1 for X")

        print("Enter 2 for O")

        print("Enter 3 to Quit")

        # limit the possible inputs to valid ones

        try:

            choice = int(input())   

        except ValueError:

            print("Wrong Input! Try Again\n")

            continue

        # What happens after each choice by the player  

        if choice == 1:

            player_choice['X'] = current_player

            if current_player == player1:

                player_choice['O'] = player2

            else:

                player_choice['O'] = player1

        elif choice == 2:

            player_choice['O'] = current_player

            if current_player == player1:

                player_choice['X'] = player2

            else:

                player_choice['X'] = player1

         

        elif choice == 3:

            print("Thanks for playing ! Final Score")

            scoreboard(score_board)

            break  

        else:

            print("Wrong Choice! Try Again\n")

        # Player’s choice of difficulty (3x3,4x4,5x5)
        
        print("Turn to choose the difficulty for", current_player)

        print("Enter 1 for 3x3 (Easy)")

        print("Enter 2 for 4x4 (Medium)")

        print("Enter 3 for 5x5 (Hard)")

        try:

            level_choice = int(input())   

        except ValueError:

            print("Wrong Input! Try Again\n")

            continue

        # defining the board after the player's choice  

        if level_choice == 1:

            winner = one_round3x3(options[choice-1])

        elif level_choice == 2:

            winner = one_round4x4(options[choice-1])

        elif level_choice == 3:

            winner = one_round5x5(options[choice-1])
         

        # updating the scoreboard after a win

        if winner != 'D' :

            player_won = player_choice[winner]

            score_board[player_won] = score_board[player_won] + 1

        scoreboard(score_board)

        # Switching between players

        if current_player == player1:

            current_player = player2

        else:

            current_player = player1
