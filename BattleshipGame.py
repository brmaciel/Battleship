from Board import *
from Ship import *

# Create all ships
destroyer = Ship(2, 'v', "D", "destroyer")
destroyer.definePosition()
cruiser = Ship(3, 'h', "C", "cruiser")
cruiser.definePosition()
submarine = Ship(3, 'v', "S", "submarine")
submarine.definePosition()
battleship = Ship(4, 'h', "B", "battleship")
battleship.definePosition()
carrier = Ship(5, 'v', "R", "carrier")
carrier.definePosition()

# list must be in a descending size-sorted, cuz that's the order the ships will be placed on the board
shipsList = [carrier, battleship, submarine, cruiser, destroyer]
#end

# Create the gameBoard and the answerBoard
gameBoard = Board("jogo")
answerBoard = Board("respostas")

#gameBoard.defineBoard()
#answerBoard.defineBoard()
#end

### Function to set ships on answerBoard ###
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
    for ship in shipsList:
        success = set_ship_on_board(ship)
        if success != True:
            reposition(success, ship)
    #answerBoard.printBoard()           # show the position of all ships on board
#end


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

###   Main Function to Start the Game   ###
def startGame():
    setAllShips_onBoard()
    print("\n\t\tBattleship: The Game")
    print(" ===== The Battle has Started ===== \n")

    num_tries = 25
    hits = 0
    piecesLeft = 0
    for ship in shipsList:
        piecesLeft += ship.getSize()

    for turn in range(1,num_tries):
        print("Pieces Left: ", piecesLeft)
        rowPicked = input("Pick a row [1~%d]: " %gameBoard.getSize())
        rowPicked = checkInput(rowPicked , "row")
        colPicked = input("Pick a col [1~%d]: " %gameBoard.getSize())
        colPicked = checkInput(colPicked, "col")

    return 0

startGame()
