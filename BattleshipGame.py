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

# make the list in a descending size-sorted, cuz that's the order the ships will be placed on the board
shipsList = [carrier, battleship, submarine, cruiser, destroyer]
#end

# Create the gameBoard and the answerBoard
gameBoard = Board("jogo")
answerBoard = Board("respostas")

gameBoard.defineBoard()
#end