from random import randint

def battlewar():
    row_size = 5
    col_size = 5
    board = [["0"]*col_size for x in xrange(row_size)]

    print "Lets play Battleship!"
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for turn in xrange(1,4):
        guess_row, guess_col = get_guess()

        #unneccessary, but the contine statement is really cool...
        if guess_row is None or guess_col is None:
            print "You will have to try again... with a number this time."
            continue

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            #leave the method, instead of break out of the loop
            return
        #\ breaks the line, because it is longer than 80 characters
        if guess_row not in xrange(row_size) or \
            guess_col not in xrange(col_size):
                print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print 'Try %s out of 3' % turn
        print_board(board)

    #will only print this if the return on line 26
    #didn't happen
    print "Game Over"

def get_guess():
    guess_row = raw_input("Guess Row from 1 to 5: ")
    try:
        guess_row = int(guess_row)
    #you can learn which type of exception will be
    #thrown if you use a python interpreter/ipython:
    #type: int('abc')
    except ValueError:
        print "the row guess is not a number!"
        guess_row = None
    else:
        guess_row -= 1

    guess_col = raw_input("Guess Col from 1 to 5: ")
    try:
        guess_col = int(guess_col)
    except ValueError:
        print "the column guess is not a number!"
        guess_col = None
    else:
        guess_col -= 1

    return guess_row, guess_col


def print_board(board):
    for row in board:
        print " ".join(row)


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

if __name__ == '__main__':
    battlewar()
