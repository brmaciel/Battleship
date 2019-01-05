from Ship import *

###   Initialize Objects   ###
# Create all ships
destroyer = Ship(2, 'v', 'D', 'Destroyer')
cruiser = Ship(3, 'h', 'C', 'Cruiser')
submarine = Ship(3, 'v', 'S', 'Submarine')
battleship = Ship(4, 'h', 'B', 'Battleship')
carrier = Ship(5, 'v', 'R', 'Carrier')

# list must be in a descending size-sorted, cuz that's the order the ships will be placed on the board
shipsList = [carrier, battleship, submarine, cruiser, destroyer]
# end

# Create the gameBoard and the answerBoard
gameBoard = Board('jogo')
answerBoard = Board('respostas')
# end


###   Function to set ships on answerBoard   ###
def set_ship_on_board(ship):
    # Define ships' position on the board_answer
    ship_row = ship.row - 1
    ship_col = ship.col - 1
    if ship.orientation == 'h':
        if answerBoard.getBoardPosition(ship_row, ship_col) == '_':
            answerBoard.setMark_on_board(ship_row, ship_col, ship.mark)
            # To know the position of first piece of ship, uncomment the line below
            #print('row: {} col: {}'.format(ship_row, ship_col))
        else:
            answerBoard.eraseMark(ship.mark)
            return False

        for pieces in range(1, ship.size):
            ship_col += 1
            if answerBoard.getBoardPosition(ship_row, ship_col) == '_':
                answerBoard.setMark_on_board(ship_row, ship_col, ship.mark)
                # To know the position of first piece of ship, uncomment the line below
                #print('row: {} col: {}'.format(ship_row, ship_col))
            else:
                answerBoard.eraseMark(ship.mark)
                return False

    elif ship.orientation == 'v':
        if answerBoard.getBoardPosition(ship_row, ship_col) == '_':
            answerBoard.setMark_on_board(ship_row, ship_col, ship.mark)
            # To know the position of first piece of ship, uncomment the line below
            #print('row: {} col: {}'.format(ship_row, ship_col))
        else:
            answerBoard.eraseMark(ship.mark)
            return False

        for pieces in range(1, ship.size):
            ship_row += 1
            if answerBoard.getBoardPosition(ship_row, ship_col) == '_':
                answerBoard.setMark_on_board(ship_row, ship_col, ship.mark)
                # To know the position of first piece of ship, uncomment the line below
                #print('row: {} col: {}'.format(ship_row, ship_col))
            else:
                answerBoard.eraseMark(ship.mark)
                return False
    return True


def reposition(check, ship):
    # Reset the ship on board in case it was overlapping another ship
    while check != True:
        # If wanna know how many times the ship was overlapping another and had to be reset, uncomment below
        #print('overlapping: ', ship.name)
        ship.definePosition()
        check = set_ship_on_board(ship)


def setAllShips_onBoard():
    # loop to set ao ships on board
    for ship in shipsList:
        success = set_ship_on_board(ship)
        if not success:
            reposition(success, ship)
    #answerBoard.printBoard()           # show the position of all ships on board
# end


###   Auxiliary Functions   ###
# Check if rows and columns input are valid
def checkInput(opt):
    # input must be: (an integer) AND (between 1 and board size)
    while True:
        try:
            userInput = int(input(f'Pick a {opt} [1~{gameBoard.size}]:').strip())
            if userInput < 1 or userInput > gameBoard.size:
                print(f"Oops, that's not even in the ocean. Pick a {opt} between 1 and {gameBoard.size}")
                continue
            return userInput
        except ValueError:
            print('Error: You must enter numbers only')
# end

# Check which ship was hit and reduce it's 'life'
def shipHit(mark):
    for ship in shipsList:
        if mark == ship.mark:
            ship.hitTaken()
            if ship.getLife == 0:
                # if the ship hit gets life to zero, it means it was destroyed
                print('*** Hooyah! {} was destroyed ***'.format(ship.name))
# end


###   Main Function to Start the Game   ###
def startGame():
    setAllShips_onBoard()
    print('\n\t\tBattleship: The Game')
    print(' ===== The Battle has Started ===== \n')
    gameBoard.printBoard()

    num_tries = 34
    piecesLeft = 0
    for ship in shipsList:
        piecesLeft += ship.size  # return 17, sum of all ships size

    for turn in range(0, num_tries):
        # find out and inform which ships weren't completely destroyed yet
        shipsAlive = []
        for ship in shipsList:
            if ship.getLife != 0:
                shipsAlive.append(ship.name)
        print('Ships remaining: ', shipsAlive)
        print(f'Turn: {turn + 1}/{num_tries}')
        print('Pieces Left: ', piecesLeft)  # how many pieces os ships weren't hit yet

        # User picks a row and col of next attack
        rowPicked = checkInput('row')
        colPicked = checkInput('col')

        if gameBoard.getBoardPosition(rowPicked - 1, colPicked - 1) == 'o':
            # 'o' mark on gameBoard means places already picked
            print('  You picked that one already. You lost a try')
        elif answerBoard.getBoardPosition(rowPicked - 1, colPicked - 1) != '_' and answerBoard.getBoardPosition(rowPicked - 1, colPicked - 1) != 'x':
            # '_' marker on answerBoard means it's water
            # 'x' marker on answerBoard means it's water and has already been picked
            print('  # Hooyah! - Battleship hit! #')
            gameBoard.setMark_on_board(rowPicked - 1, colPicked - 1, 'o')
            piecesLeft -= 1

            shipHit(answerBoard.getBoardPosition(rowPicked - 1, colPicked - 1))  # reduce the life of the ship hit

        elif answerBoard.getBoardPosition(rowPicked - 1, colPicked - 1) == 'x':
            # 'x' on answerBoard means place has a ship but was already picked
            print('  You picked that one already. You lost a try')
        else:
            # hit the water, so mark the boards with 'x' to mark the place as 'already picked'
            print('  # Water! You missed the battleship! #')
            gameBoard.setMark_on_board(rowPicked - 1, colPicked - 1, 'x')
            answerBoard.setMark_on_board(rowPicked - 1, colPicked - 1, 'x')

        gameBoard.printBoard()

        if piecesLeft == 0:
            # All ships were destroyed
            print('\t###   You Won!   ###')
            print('Location of Ships:')
            answerBoard.printBoard()
            return 0

        if turn == num_tries - 1:
            # Se esgotou o numero de tentativas
            print('\t###   Game Over!   ###')
            print('Location of Ships:')
            answerBoard.printBoard()

    return 0

startGame()
