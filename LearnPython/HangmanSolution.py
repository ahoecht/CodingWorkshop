################################################################################
### IMPORTS ###
import random

################################################################################
### GAME CLASS ###
class HangMan(object):

    ##############################
    ### GAME SETUP ###
    pics = []

    # Game board
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    # Our poor player =(
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']

    # Word bank to play from (Add words freely)
    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
                crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
                mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
                rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
                toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

    # You win outline
    infStr='_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    ##############################
    ### GAME LOGIC ###
    """ Initialize and draw game board """
    def __init__(self, *args, **kwargs):
        # Index variables
        i = 2
        j = 0

        # Draw game board and our poor player
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic = self.hang[:]
            j = 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    """ Select a word from the word bank """
    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    """ Print our game board and player properly """
    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)

    """ Prompt user for a guess, and compare to mystery word """
    def askAndEvaluate(self, word, result, missed):
        # Prompt user
        guess = input("Guess a letter: ")

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

    """ Output of each round """
    def info(self, info):
        ln=len(self.infStr)
        print()
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])
        print()

    """ Initialize game """
    def start(self):
        # Initial variable setup
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

            # Some output spacing to make it look pretty
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
a = HangMan().start()
