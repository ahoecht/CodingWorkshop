################################################################################
### IMPORTS ###
################################################################################
"""
TO DO: Import the pre-built "random" module
"""

################################################################################
### GAME CLASS ###
################################################################################
"""
What is a class?
A class provides the means of bundling data and functionality together to form
a new type of object.
"""
class HangMan(object):

    ##############################
    ### GAME SETUP ###
    ##############################
    pics = []

    # Game board
    gameBoard = []
    gameBoard.append(' +---+')
    gameBoard.append(' |   |')
    gameBoard.append('     |')
    gameBoard.append('     |')
    gameBoard.append('     |')
    gameBoard.append('     |')
    gameBoard.append('=======')

    # Our poor player (in pieces) =(
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']

    # Word bank to play from
    """
        TO DO: Fill in your word bank
        (use as many or as few words as you would like)
    """
    words = ''' X Y X '''.split()

    # You win outline
    infStr='_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    ##############################
    ### GAME LOGIC ###
    ##############################
    """
    "__init__" is an important method!
    When an instance of a class is created, this method is automatically called
    to initialize the different inital state attributes of the class.

    In this case, it will initialize and draw the game board.

    NOTE: We use the variable "self" to refer to this specific instance of
            the class
    """
    def __init__(self, *args, **kwargs):
        # Index variables used for iteration
        i = 2
        j = 0

        # Draw the game board and our poor player
        self.pics.append(self.gameBoard[:])
        for ls in self.man.values():
            pic = self.gameBoard[:]
            j = 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)


    """ Select a word from the word bank """
    def pickWord(self):
        """
        TO DO: Write the statement below!
            It should: "Return the word at a randomly selected position."
            (HINT: Index positions start at zero! You should generate a
                random position between 0 and the length of the wordbank -1)
        """
        return self.words


    """ Print our game board and player properly """
    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)


    """ Prompt user for a guess, and compare to mystery word """
    def askAndEvaluate(self, word, result, missed):
        # Prompt user
        """
        TO DO: Prompt the user and save their response as the variable
                "guess"
        """


        # Return, if invalid input
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False

        # Check if input is in our mystery word
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    """ Output updated state """
    def info(self, info):
        ln=len(self.infStr)
        print()
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])
        print()

    """ Start the game! """
    def start(self):
        # Initial game setup
        word = list(self.pickWord())
        result = list('*' * len(word))
        success = False
        missed = []
        i = 0

        print('Welcome to Hangman !')
        print('NOTE: player should guess in lowercase')
        print('Mystery word: ', result)

        # Main game loop
        while i < len(self.pics)-1:
            print()
            print()
            # Prompt user and evaluate guess
            guess,right = self.askAndEvaluate(word, result, missed)

            # Case 1) Invalid input
            if guess == None:
                print('You\'ve already entered this character.')
                continue

            print(''.join(result))

            # Case 2) Player wins the game!
            if result == word:
                self.info('Congratulations ! You\'ve just saved a life !')
                success = True
                break

            # Case 3) Player guessed incorrectly
            if not right:
                missed.append(guess)
                i+=1

            self.printPic(i, len(word))
            print('Missed characters: ', missed)

        # Game over
        if not success:
            self.info('GAME OVER! The word was \''+''.join(word)+'\' ! Please play again!!!')


################################################################################
### RUN GAME ###
"""
You did it! You made it to the end! Congratulations! You Rock 😎
The last step is to run everything. We do that by creating and instance
of our HangMan class by calling its constructor method "HangMan()".

Now that you have read through the full code once, try and trace the flow
of how each method is used together to create our game. Start here with our
run statement. What happens when we use the "HangMan()" method? What then?
"""
a = HangMan().start()
