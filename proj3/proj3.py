# File:    proj3.py
# Author:  Muhammed Muktar
# Date:    12/7/2018
# Section: Section 30
# E-mail:  mmuktar1@umbc.edu
# Description: Project 3

#costants for answering questions
PLAY_GAME = "p"
SAVE_GAME = "s"
SOLVE_GAME = "s"
UNDO_TURN = "u"
QUIT_GAME = "q"
ANSWER_YES = "y"
ANSWER_NO = "n"

#costants for valid number inputs for locations and number input
MIN_INPUT = 1
MAX_INPUT = 9


#prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[:len(rowStr) - 1] + "\n")
    ofp.close()


#createBoard() turns the puzzle txt into a 2D array to work with in code
#Input:        fileName; the txt file of the puzzle
#Output:       board; final board turned into a 2d array
def createBoard(fileName):

    #opens file
    boardFile = open(fileName, "r")
    boardStr = boardFile.readlines()
    boardFile.close()

    #creates a board
    newBoard = []
    for r in range(len(boardStr)):

        #removes comma
        removeComma = boardStr[r].split(",")
        newBoard.append(removeComma)

    #makes board
    for r in range(len(newBoard)):
        for c in range(len(newBoard[r])):
            newBoard[r][c] = int(newBoard[r][c])

    return newBoard


#updatePuzzle() adds the user's turn to the board
#Input:         row; row user wants to add number.
#               col; col user wants to add number.
#               number; number the user wants to add in Sudoku
#Output:        board; updated board
def updatePuzzle(row, col, board, number):

    #adds number to the board
    board[row][col] = number

    return board


#wonPuzzle() checks if the user has won the sudoku game
#Input:      board; current board. solvedBoard; solved board
#Output:     True; if boards are the same. False; if boards are not the same.
def wonPuzzle(board, solvedBoard):

    for r in range(len(board)):
        for c in range(len(board[r])):

            #if a number does not match up
            if board[r][c] != solvedBoard[r][c]:
                return False
    return True


#solvePuzzle() uses recursion to solve the puzzle
#Input:        board; the board to continue solving
#              row; row cord of space to slove
#              col; col cord of space to solve
#Output:       solvedPuzzle; solved puzzle
def solvePuzzle(board, row, col):

    #array of possible numbers
    possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #base case if the board is full at this point
    if row == 8 and col == 9:
     return True

    #if you get to the end of the col
    elif col == 9:
        return solvePuzzle(board, row + 1, 0)

    #if the space is filled
    elif board[row][col] != 0:
        return solvePuzzle(board, row, col + 1)

    else:
        #array of possible number
        workingNumbers = []

        #creates a list of valid numbers
        for checkNum in range(len(possibleNumbers)):

            #if the number is a valid add to list
            if isValidNumber(possibleNumbers[checkNum], row, col, board):
                workingNumbers.append(possibleNumbers[checkNum])

        #back tracks and tries possible combinations of valid numbers
        for addNum in range(len(workingNumbers)):

            board[row][col] = workingNumbers[addNum]
            if (solvePuzzle(board, row, col + 1)):
                return True
            board[row][col] = 0

    return False


#getRow() asks user for a row, makes sure the input is valid
#Input:   None;
#Output:  row; valid row
def getRow():

    #asks for a row
    askRow = int(input("Enter a row (1-9): "))

    #makes sure row is valid
    while askRow < MIN_INPUT or askRow > MAX_INPUT:
        askRow = int(input("Enter a valid row (1-9): "))

    return askRow


#getCol() asks user for a col, makes sure the input is valid
#Input:   None;
#Output:  col; valid col
def getCol():

    #asks for a col
    askCol = int(input("Enter a col (1-9): "))

    #makes sure col is valid
    while askCol < MIN_INPUT or askCol > MAX_INPUT:
        askCol = int(input("Enter a valid col (1-9): "))

    return askCol


#getNum() asks user for a Sudoku Number to add to board, makes sure the input is valid
#Input:   None;
#Output:  sudokuNumber; valid number
def getNum():

    #asks for number
    askNum = int(input("Enter a number (1-9): "))

    #makes sure the number is valid
    while askNum < MIN_INPUT or askNum > MAX_INPUT:
        askNum = int(input("Enter a valid number (1-9): "))

    return askNum


def isValidNumber(number, row, col, board):

    #numbers that corralate with the box sections
    boxOne = [0, 1, 2]
    boxTwo = [3, 4, 5]
    boxThree = [6, 7, 8]

    #gets the top left corner of box
    if row in boxOne:
        checkRow = boxOne[0]
    elif row in boxTwo:
        checkRow = boxTwo[0]
    elif row in boxThree:
        checkRow = boxThree[0]

    #gets the top left corner of box
    if col in boxOne:
        checkCol = boxOne[0]
    elif col in boxTwo:
        checkCol = boxTwo[0]
    elif col in boxThree:
        checkCol = boxThree[0]

    #array of numbers in the box
    boxSectionNumbers = []
    for r in range(checkRow, checkRow + 3):
        for c in range(checkCol, checkCol + 3):
            if board[r][c] != 0:
                boxSectionNumbers.append(board[r][c])

    #array of col numbers
    boardColNumbers = []
    for r in range(len(board)):
        if board[r][col] != 0:
            boardColNumbers.append(board[r][col])

    possibleHorizontal = False
    possibleVertical = False
    possibleBox = False

    #checks if its possible in the row
    if number not in board[row]:
        possibleHorizontal = True

    #check if its possible in the box section
    if number not in boxSectionNumbers:
        possibleVertical = True

    #checks if its possible in the col
    if number not in boardColNumbers:
        possibleBox = True

    if possibleHorizontal and possibleVertical and possibleBox:
        return True

    return False


#getFileName() asks user for puzzle txt to solve
#Input:        None;
#Output:       fileName; file name given by user
def getFileName():

    #gets file name
    fileName = input("What is the puzzle's file name: ")
    return fileName


#correctChecking() allows the program to correct the user if a number they
#                  entered is wrong.
#Input:            row; row to check. col; col to check
#                  solvedBoard; solved puzzle
#Ouput:            True; if user's input is correct.
#                  Flase; if user's input is incorrect.
def correctChecking(number, solvedBoard, row, col):

    #if number added does not match with the solved board
    if number != solvedBoard[row][col]:

        print("I would not put that over there")
        return False

    return True


#undoPuzzle() serves as an undo for the the last change in the board
#Input:       rowLoc; array of row locations, colLoc; array of col locations
#             board; current board
#Output:      updated and fixed board
def undoPuzzle(rowLoc, colLoc, board):

    #if there is nothing to undo
    if len(rowLoc) == 0 and len(colLoc) == 0:
        print("Nothing to undo")
    else:

        #removes number
        print("You removed",
              board[rowLoc[len(rowLoc) - 1]][colLoc[len(colLoc) - 1]], "at",
              str(rowLoc[len(rowLoc) - 1] + 1), ",",
              str(colLoc[len(colLoc) - 1] + 1))
        board[rowLoc.pop()][colLoc.pop()] = 0
        #rowLoc.remove(board[rowLoc])
        #colLoc.remove(board[colLoc])


#deepCopyBoard() creates a copy of an array
#Input         board; board to copy
#Output        newBoard; copied board.
def deepCopyBoard(board):

    #creates a deep copy of each row
    newBoard = []
    for r in range(len(board)):
        copyRow = list(board[r])
        newBoard.append(copyRow)

    return newBoard


def main():

    #asks for file name
    askFileName = getFileName()

    #creates board
    currentBoard = createBoard(askFileName)
    prettyPrint(currentBoard)

    #creates solved boards
    solvedBoard = deepCopyBoard(currentBoard)
    solvePuzzle(solvedBoard, 0, 0)

    #asks if they want to play or solve
    askPlayOrSolve = input("play(p) or solve(s)? ")

    #if they want to solve
    if askPlayOrSolve == SOLVE_GAME:
        prettyPrint(solvedBoard)

    #if they want to play
    elif askPlayOrSolve == PLAY_GAME:

        askCorrectCheck = input("Do you want correctness checking (y/n): ")

        undoRow = []
        undoCol = []
        keepPlaying = True
        while not (wonPuzzle(currentBoard, solvedBoard)) and keepPlaying:

            #prints board
            prettyPrint(currentBoard)
            askPlayOptions = input(
                "play number(p), save(s), undo(u), quit(q): ")

            #if they want to play
            if askPlayOptions == PLAY_GAME:
                askRow = getRow()
                askCol = getCol()
                askNumber = getNum()

                correctValue = True

                #if there is already a number
                if currentBoard[askRow - 1][askCol - 1] != 0:
                    print("You cannot replace values")
                    correctValue = False

                #if correct checking is not
                elif askCorrectCheck == ANSWER_YES:

                    if (correctChecking(askNumber, solvedBoard, askRow - 1,
                                        askCol - 1)):

                        print(
                            "OOPS", askNumber,
                            "does not belong in position (" + str(askRow) +
                            ", " + str(askCol) + ")")
                        correctValue = False

                else:
                    #if it follows sudoku rules
                    if not (isValidNumber(askNumber, askRow - 1, askCol - 1,
                                          currentBoard)):

                        print("There already a", askNumber, "there.")
                        correctValue = False

                #if they are allow to add the number
                if correctValue:

                    undoRow.append(askRow - 1)
                    undoCol.append(askCol - 1)
                    currentBoard = updatePuzzle(askRow - 1, askCol - 1,
                                                currentBoard, askNumber)
                    prettyPrint(currentBoard)

            #undoes turn
            elif askPlayOptions == UNDO_TURN:
                undoPuzzle(undoRow, undoCol, currentBoard)

            #saves game
            elif askPlayOptions == SAVE_GAME:
                savePuzzle(currentBoard, "savedPuzzle.txt")
                keepPlaying = False

            #quits game
            elif askPlayOptions == QUIT_GAME:
                print("Good Bye! Here is the final board!")
                prettyPrint(currentBoard)
                keepPlaying = False

            #if player won
            if wonPuzzle(currentBoard, solvedBoard):
                print("You won")
                prettyPrint(currentBoard)


main()
