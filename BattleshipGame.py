from Board import *
from Ship import *

###   Initialize Objects   ###
# Create all ships
destroyer = Ship(2, 'v', "D", "Destroyer")
cruiser = Ship(3, 'h', "C", "Cruiser")
submarine = Ship(3, 'v', "S", "Submarine")
battleship = Ship(4, 'h', "B", "Battleship")
carrier = Ship(5, 'v', "R", "Carrier")

# list must be in a descending size-sorted, cuz that's the order the ships will be placed on the board
shipsList = [carrier, battleship, submarine, cruiser, destroyer]
#end

# Create the gameBoard and the answerBoard
gameBoard = Board("jogo")
answerBoard = Board("respostas")
#end



###   Function to set ships on answerBoard   ###
def set_ship_on_board(ship):
    # Define ships' position on the board_answer
    ship_row = ship.getRow()-1
    ship_col = ship.getCol()-1
    if ship.getOrientation() == 'h':
        if answerBoard.tabuleiro[ship_row][ship_col] == "_":
            answerBoard.setMark_on_board(ship_row,ship_col, ship.getMark())
            # To know the position of first piece of ship, uncomment the line below
            #print ("row: ",ship_row, " col: ", ship_col)
        else:
            answerBoard.eraseMark(ship.getMark())
            return False

        for pieces in range(1,ship.getSize()):
            ship_col += 1
            if answerBoard.tabuleiro[ship_row][ship_col] == "_":
                answerBoard.setMark_on_board(ship_row, ship_col, ship.getMark())
                # To know the position of first piece of ship, uncomment the line below
                # print ("row: ",ship_row, " col: ", ship_col)
            else:
                answerBoard.eraseMark(ship.mark)
                return False

    elif ship.getOrientation() == "v":
        if answerBoard.tabuleiro[ship_row][ship_col] == "_":
            answerBoard.setMark_on_board(ship_row, ship_col, ship.getMark())
            # To know the position of first piece of ship, uncomment the line below
            #print ("row: ",ship_row, " col: ", ship_col)
        else:
            answerBoard.eraseMark(ship.getMark())
            return False

        for pieces in range(1,ship.getSize()):
            ship_row += 1
            if answerBoard.tabuleiro[ship_row][ship_col] == "_":
                answerBoard.setMark_on_board(ship_row, ship_col, ship.getMark())
                # To know the position of first piece of ship, uncomment the line below
                # print ("row: ",ship_row, " col: ", ship_col)
            else:
                answerBoard.eraseMark(ship.getMark())
                return False
    return True

def reposition(check, ship):
    # Reset the ship on board in case it was overlaping another ship
    while check != True:
        # If wanna know how many times the ship was overlapping another and had to be reset, uncomment below
        #print("overlapping: ", ship.getName())
        ship.definePosition()
        check = set_ship_on_board(ship)

def setAllShips_onBoard():
    # loop to set ao ships on board
    for ship in shipsList:
        success = set_ship_on_board(ship)
        if success != True:
            reposition(success, ship)
    #answerBoard.printBoard()           # show the position of all ships on board
#end



###   Auxiliary Functions   ###
# Check if rows and columns input are valid
def checkInput(userInput, opt):
    # input must be: (an integer) AND (between 1 and board size)
    while (userInput.isdigit() == False) or (int(userInput) > gameBoard.getSize()) or (int(userInput) < 1):
        if (userInput.isdigit() == False):
            print("Error: You must enter numbers only")
            userInput = input("Pick a %s [1~%d]: " %(opt, gameBoard.getSize()))
        else:
            print("Oops, that's not even in the ocean. Pick a row between 1 and %d" %gameBoard.getSize())
            userInput = input("Pick a %s [1~%d]: " %(opt, gameBoard.getSize()))
    return int(userInput)
#end

# Check which ship was hit and reduce it's 'life'
def shipHit(mark):
    for ship in shipsList:
        if mark == ship.getMark():
            ship.hitTaken()
            if ship.getLife() == 0:
                # if the ship hit gets life to zero, it means it was destroyed
                print("*** Hooyah! %s was destroyed ***" %ship.getName())
#end



###   Main Function to Start the Game   ###
def startGame():
    setAllShips_onBoard()
    print("\n\t\tBattleship: The Game")
    print(" ===== The Battle has Started ===== \n")
    gameBoard.printBoard()

    num_tries = 34
    piecesLeft = 0
    for ship in shipsList:
        piecesLeft += ship.getSize()    # return 17, sum of all ships size

    for turn in range(0,num_tries):
        # find out and inform which ships weren't completely destryoed yet
        shipsAlive = []
        for ship in shipsList:
            if ship.getLife() != 0:
                shipsAlive.append(ship.getName())
        print("Ships remaining: ", shipsAlive)

        print("Turn: %d/%d" %(turn+1,num_tries))
        print("Pieces Left: ", piecesLeft)              # how many pieces os ships weren't hit yet
        rowPicked = input("Pick a row [1~%d]: " %gameBoard.getSize())
        rowPicked = checkInput(rowPicked , "row")
        colPicked = input("Pick a col [1~%d]: " %gameBoard.getSize())
        colPicked = checkInput(colPicked, "col")

        if gameBoard.tabuleiro[rowPicked-1][colPicked-1] == 'o':
            # 'o' mark on gameBoard means places already picked
            print("  You picked that one already. You lost a try")
        elif answerBoard.tabuleiro[rowPicked-1][colPicked-1] != '_' and answerBoard.tabuleiro[rowPicked-1][colPicked-1] != 'x':
             # '_' marker on answerBoard means it's water
             # 'x' marker on answerBoard means it's water and has already been picked
             print("  # Hooyah! - Battleship hit! #")
             gameBoard.setMark_on_board(rowPicked-1, colPicked-1, 'o')
             piecesLeft -= 1

             shipHit(answerBoard.tabuleiro[rowPicked - 1][colPicked - 1])   # reduce the life of the ship hit

        elif answerBoard.tabuleiro[rowPicked-1][colPicked-1] == 'x':
            # 'x' on answerBoard means place has a ship but was already picked
            print("  You picked that one already. You lost a try")
        else:
            # hit the water, so mark the boards with 'x' to mark the place as 'already picked'
            print("  # Water! You missed the battleship! #")
            gameBoard.setMark_on_board(rowPicked-1, colPicked-1, 'x')
            answerBoard.setMark_on_board(rowPicked-1, colPicked-1, 'x')

        gameBoard.printBoard()

        if piecesLeft == 0:
            # All ships were destroyed
            print("\t###   You Won!   ###")
            print("Location of Ships:")
            answerBoard.printBoard()
            return 0

        if turn == num_tries-1:
            # Se esgotou o numero de tentativas
            print("\t###   Game Over!   ###")
            print("Location of Ships:")
            answerBoard.printBoard()

    return 0

startGame()