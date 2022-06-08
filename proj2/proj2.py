# File: proj2.py
# Author: Muhammed Muktar
# Date: 10/31/2018
# Section: 30
# E-mail: mmuktar1@umbc.edu
# Description: Connect 4 Game, re-creation. The file is meant to be a re-creation
#of the game connect 4; using a gameboard and user input this program is to allow
#the user to play. The game also allows the option to play against a computer,
#instead of anoher player.

from random import randint

#constants for the lowest value of the game board height and width
MIN_WIDTH = 5
MIN_COL = 5

#constant for the lowest column player can pick
MIN_VAL_TURN = 1

#constants for the pieces used on the game board
PLAYER1_PIECE = "X"
PLAYER2_PIECE = "O"
EMPTY_SPACE = "-"

#constant for the total amount of peices needed to win
TOTAL_PIECE_WIN = 4

#constanst for answering yes or no
ANSWER_YES = "y"
ANSWER_NO = "n"

#printBoard() displays the current game board to the user
#Input:       gameGrid; current game board.
#Output:      no output


def printBoard(gameGrid):

    #prints out the gameboard
    row = 0
    while row < len(gameGrid):
        col = 0
        while col < len(gameGrid[row]):
            print(gameGrid[row][col], end=" ")
            col += 1
        print("")
        row += 1


#askWidth() asks the user to input a valid width to use for the game board
#Input:     no input
#Output:    width; valid width entered by user


def askWidth():
    width = int(input("Enter a width: "))

    #if the width is not large enough
    if width < MIN_WIDTH:
        width = int(input("Enter a valid width(5 or greater): "))

    return width


#askHeight() asks the user to input a valid height to use for the game board
#Input:      no input
#Output:     height; valid height entered by user


def askHeight():
    height = int(input("Enter a col: "))

    #if the height is not large enough
    if height < MIN_COL:
        height = int(input("Enter a valid col(5 or greater): "))

    return height


#makeGrid() creates the starting 2d array to represent the game board
#Input:     col; the width given by the user. row; the height given by the user
#Output:    gameGrid; starting version of the game board


def makeGrid(col, row):
    gameGrid = []

    #creates the game board given the row and column
    while len(gameGrid) < row:
        gameRow = []

        while len(gameRow) < col:
            gameRow.append(EMPTY_SPACE)

        gameGrid.append(gameRow)

    return gameGrid


#updateGrid() updates the game board to add the player's piece to the column
#they picked
#Input:       piece; current player's piece("X"/"O"). userChoice; the column
#             the player picked. gameGrid; the current game board
#Output:      gameGrid; updated version of the gameboard


def updateGrid(piece, userChoice, gameGrid):

    row = len(gameGrid) - 1

    #startes from the bottom of the grid and moves up
    while row >= 0:

        #if there is an empty space
        if gameGrid[row][userChoice - 1] == EMPTY_SPACE:

            gameGrid[row][userChoice - 1] = piece
            return gameGrid

        row -= 1

    return gameGrid


#checkIfWon() checks if a player has won with 4 of their pieces in a row
#             horizontally, vertically, or diagonally
#Input:       gameGrid; current game board. piece; player piece.
#             userChoice; last column player has picked
#Output:      True; if a player has 4 pieces in a row.
#             False; if they dont have 4 pieces in  row.


def checkIfWon(gameGrid, userChoice, piece):

    #checks vertical win
    verticalRow = 0
    totalPieces = 0

    #starts from the top and moves down the board
    while (verticalRow < len(gameGrid)):

        #checks if the index has the user's piece
        if (gameGrid[verticalRow][userChoice - 1] == piece):
            totalPieces += 1

            #check is player has won
            if totalPieces == TOTAL_PIECE_WIN:

                return True
        else:
            totalPieces = 0

        verticalRow += 1

    #gets the row location of the last piece placed by user
    rowLocation = -1
    checkRow = True

    #checks the each row from the top
    while rowLocation < len(gameGrid) and checkRow:

        rowLocation += 1

        #if the index matches the piece of the player
        if gameGrid[rowLocation][userChoice - 1] == piece:

            getPieceRowLocation = rowLocation
            checkRow = False

    #checks horizontal win
    horizontalRow = getPieceRowLocation
    horizontalCol = 0
    totalPieces = 0

    #starts from the row and moves through the cloumn
    while (horizontalCol < len(gameGrid[horizontalRow])):

        #checks if the index has the user's piece
        if (gameGrid[horizontalRow][horizontalCol] == piece):

            totalPieces += 1

            #check if player won
            if totalPieces == TOTAL_PIECE_WIN:

                return True
        else:
            totalPieces = 0

        horizontalCol += 1

    #current location
    topLeftDiagRow = getPieceRowLocation
    topLeftDiagCol = userChoice - 1

    #gets the location of the very possible top diagnal index to check diag win
    #from the left
    while topLeftDiagRow != 0 and topLeftDiagCol != 0:

        topLeftDiagRow -= 1
        topLeftDiagCol -= 1

    totalPieces = 0

    #checks for diagonal win from the left
    while topLeftDiagRow < len(gameGrid) and \
          topLeftDiagCol < len(gameGrid[topLeftDiagRow]):

        #if current index equal the player piece
        if (gameGrid[topLeftDiagRow][topLeftDiagCol] == piece):

            totalPieces += 1

            #player has enough pieces to win
            if totalPieces == TOTAL_PIECE_WIN:

                return True
        else:
            totalPieces = 0

        topLeftDiagCol += 1
        topLeftDiagRow += 1

    #current location
    topRightDiagRow = getPieceRowLocation
    topRightDiagCol = userChoice - 1

    #gets the location of the very possible top diagnal index to check diag win
    #from the right
    while topRightDiagRow != 0 and \
          topRightDiagCol != len(gameGrid[topRightDiagRow]) - 1:

        topRightDiagRow -= 1
        topRightDiagCol += 1

    totalPieces = 0

    #checks for diagonal win from the right
    while topRightDiagRow < len(gameGrid) and topRightDiagCol >= 0:

        #if current index equals the player piece
        if (gameGrid[topRightDiagRow][topRightDiagCol] == piece):

            totalPieces += 1

            #if the player has enough pieces
            if totalPieces == TOTAL_PIECE_WIN:

                return True
        else:
            totalPieces = 0

        topRightDiagCol -= 1
        topRightDiagRow += 1

    #none of the pieces were four in a row
    return False


#getComputerTurn() chooses a random column for the computer's AI to play
#Input:            width; value of the total amount of columns on the board.
#                  gameGrid; current game board
#Output:           computerPick; random value chosen


def getComputerTurn(width, gameGrid):

    #gets a random number in a valid range
    randomPick = randint(1, width)

    #makes sure the chosen column isnt full
    while (gameGrid[0][randomPick - 1] != EMPTY_SPACE):
        randomPick = randint(1, width)

    return randomPick


#getPlayerTurn(width) asks the user for a valid column space to put their piece
#Input:               width; value of the total amount of columns on the board
#Output:              playerTurn; valid column number picked by user


def getPlayerTurn(width):

    #asks user to enter a column
    playerTurn = int(input("Enter a column to place your piece (1 - " + \
                           str(width) + "): "))

    #makes sure the chosen column is valid
    while (playerTurn < MIN_VAL_TURN or playerTurn > width):

        playerTurn = int(input("Enter a valid column to place your piece (1 - " \
                         + str(width) + "): "))

    return playerTurn


def main():
    #start of game
    print("Welcome to connect four! \n")

    #makes sure the player wants to keep playing
    keepPlaying = True
    while (keepPlaying):

        #gets the width and height
        getWidth = askWidth()
        getHeight = askHeight()

        #asks if player wants to play with a computer
        playWithComputer = \
            input("Would you like to play with a computer? (y/n): ")

        #makes sure input is correct
        while playWithComputer != ANSWER_YES and playWithComputer != ANSWER_NO:
            playWithComputer = \
                input("Would you like to play with a computer? enter (y/n): ")

        #creates the game baord
        gameBoard = makeGrid(getWidth, getHeight)

        #prints the board
        printBoard(gameBoard)
        playerHasNotWon = True

        #while there are open spaces in the board and a player has not won
        while (EMPTY_SPACE in gameBoard[0] and playerHasNotWon):

            #FIRST PLAYER'S TURN--------

            #asks player1 to enter their choice
            print("Player 1 what is your choice?")
            askPlayerChoice = getPlayerTurn(getWidth)

            #makes sure the column is not full, if so will reprompt them
            while (gameBoard[0][askPlayerChoice - 1] != "-"):

                print("Choose a different column, that one is full")
                askPlayerChoice = getPlayerTurn(getWidth)

            #updates the game board
            gameBoard = updateGrid(PLAYER1_PIECE, askPlayerChoice, gameBoard)
            printBoard(gameBoard)

            #PLAYER'S TURN ENDS---------

            #checks if player won and wants to keep playing
            if (checkIfWon(gameBoard, askPlayerChoice, PLAYER1_PIECE)):

                playerHasNotWon = False
                print("Player 1 won!")

                #asks if player wants to keep playing
                playAgain = input("Would you like to play again? (y/n): ")

                #makes sure input is valid
                while playAgain != ANSWER_YES and playAgain != ANSWER_NO:
                    playAgain = \
                        input("Would you like to play again? enter (y/n): ")

                if playAgain == ANSWER_NO:
                    keepPlaying = False

            #checks if all spaces are taken
            if (EMPTY_SPACE not in gameBoard[0]):

                print("You tied")

                #asks if player wants to keep playing
                playAgain = input("Would you like to play again? (y/n): ")

                #makes sure input is valid
                while playAgain != ANSWER_YES and playAgain != ANSWER_NO:
                    playAgain = \
                        input("Would you like to play again? enter (y/n): ")

                if playAgain == ANSWER_NO:
                    keepPlaying = False

            #SECOND PLAYER'S TURN-------

            #goes to the next turn if player 1 has not won,
            if (playerHasNotWon and EMPTY_SPACE in gameBoard[0]):

                #computer plays instead
                if (playWithComputer == ANSWER_YES):

                    askPlayerChoice = getComputerTurn(getWidth, gameBoard)
                    print("Player 2 picked the", askPlayerChoice, "column")

                elif (playWithComputer == ANSWER_NO):

                    #asks player2 to enter their choice
                    print("Player 2 what is your choice?")
                    askPlayerChoice = getPlayerTurn(getWidth)

                    #makes sure the column is not full, if so will reprompt them
                    while (gameBoard[0][askPlayerChoice - 1] != "-"):

                        print("Choose a different column, that one is full")
                        askPlayerChoice = getPlayerTurn(getWidth)

                #updates the game board
                gameBoard = updateGrid(PLAYER2_PIECE, askPlayerChoice,
                                       gameBoard)
                printBoard(gameBoard)

                #PLAYER'S TURN ENDS---------

                #checks if player won and wants to keep playing

                if checkIfWon(gameBoard, askPlayerChoice, PLAYER2_PIECE):

                    playerHasNotWon = False

                    if playWithComputer == ANSWER_YES:

                        print("The Computer Won!")

                    elif playWithComputer == ANSWER_NO:

                        print("Player 2 won!")

                    #asks if player wants to keep playing
                    playAgain = input("Would you like to play again? (y/n): ")

                    #makes sure input is valid
                    while playAgain != ANSWER_YES and playAgain != ANSWER_NO:
                        playAgain = \
                            input("Would you like to play again? enter (y/n): ")

                    if playAgain == ANSWER_NO:
                        keepPlaying = False

                #IF THE PLAYERS TIE

                #checks if there is no spaces in the board
                if (EMPTY_SPACE not in gameBoard[0]):

                    print("You tied")

                    #asks if player wants to keep playing
                    playAgain = input("Would you like to play again? (y/n): ")

                    #makes sure input is valid
                    while playAgain != ANSWER_YES and playAgain != ANSWER_NO:
                        playAgain = \
                            input("Would you like to play again? enter (y/n): ")

                    if playAgain == ANSWER_NO:
                        keepPlaying = False


main()
