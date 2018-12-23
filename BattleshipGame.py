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

gameBoard.defineBoard()
#end

### Function to set ships on answerBoard ###
def set_ship_on_board(ship):
    # Define ships' position on the board_answer
    ship_row = ship.bottom_row-1
    ship_col = ship.bottom_col-1
    if ship.getOrientation() == 'h':
        if answerBoard.tabuleiro[ship_row][ship_col] == "_":
            answerBoard.set_mark_on_board(ship_row,ship_col, ship.mark)
            # To know the position of first piece of ship, uncomment the line below
            #print ("row: ",ship_row, " col: ", ship_col)
        else:
            answerBoard.eraseMark(ship.mark)
            return False

        for pieces in range(1,ship.getSize()):
            ship_col += 1
            if answerBoard.tabuleiro[ship_row][ship_col] == "_":
                answerBoard.set_mark_on_board(ship_row, ship_col, ship.mark)
                # To know the position of first piece of ship, uncomment the line below
                # print ("row: ",ship_row, " col: ", ship_col)
            else:
                answerBoard.eraseMark(ship.mark)
                return False

    elif ship.getOrientation() == "v":
        if answerBoard.tabuleiro[ship_row][ship_col] == "_":
            answerBoard.set_mark_on_board(ship_row, ship_col, ship.mark)
            # To know the position of first piece of ship, uncomment the line below
            #print ("row: ",ship_row, " col: ", ship_col)
        else:
            answerBoard.eraseMark(ship.mark)
            return False

        for pieces in range(1,ship.getSize()):
            ship_row += 1
            if answerBoard.tabuleiro[ship_row][ship_col] == "_":
                answerBoard.set_mark_on_board(ship_row, ship_col, ship.mark)
                # To know the position of first piece of ship, uncomment the line below
                # print ("row: ",ship_row, " col: ", ship_col)
            else:
                answerBoard.eraseMark(ship.mark)
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
    answerBoard.printBoard()
#end

setAllShips_onBoard()