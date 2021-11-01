import random
wordsL1 = ["pasta", "spaghetti", "maccheroni"]
wordsL2 = ["pasteroni", "maccharetti", "cannelloncelli"]

class HangmanGame: 
    def __init__(self, wordsList, lives):
        self.wordsToPlay = wordsList
        self.plain_text = random.choice(wordsList)
        self.hidden = ("_" * len(self.plain_text))
        self.lives = lives
        self.tries = []

    def updateHidden(self, index):
        self.hidden = self.hidden[:index] + self.plain_text[index] + self.hidden[index+1:]

def main():
    ## Check if they actually want to play, if so:
    startGame(wordsL1, 7)
    

def startGame(listOfWords, lives):
    game = HangmanGame(listOfWords, lives)
    print("----------- THE GAME BEGINS----------")
    print("\n")
    print(game.hidden)
    print("\n")
    print(f"Lives: {game.lives}")
    print("\n")
    while(True):
        guess = input("Please enter a guess, it must be a letter!, go ahead: ")
        if validateInput(game, guess):
            matchedIndexes = (checkMatch(game, guess))
            if len(matchedIndexes):
                updateDisplayedWord(game, matchedIndexes)
            else:
                game.tries.append(guess)
                print(HANGMANPICS[-game.lives])
                game.lives -= 1
                
            
            winOrLose(game)
            print("\n")
            print(game.hidden)
            print("\n")
            print("Tried letters/words: ")
            print(*game.tries, sep = ", ")
            print("\n")
            print(f"Lives: {game.lives}")

def checkMatch(game, guess):
    return [i for i, ltr in enumerate(game.plain_text) if ltr == guess]

def updateDisplayedWord(game, list):
    for idx in list:
        game.updateHidden(idx)

def winOrLose(game):
    if (game.hidden == game.plain_text):
        print(f"Congrats, you won! The word was {game.plain_text}")
        playAgain = input("Wanna go ahead to the next level(y/n): ")
        if playAgain == "y":
            startGame(wordsL2, 3)
        exit(0)
    elif(game.lives == 0):
        print("You lost, poor idiot")
        exit(0)

def validateInput(game, guess):
    if not guess.isalpha():
        print("Please enter a letter [a, b, c ..]: ")
        return False
    elif len(guess) > 1:
        answer = input("Are you sure you want to guess the whole word? It's gonna cpst you lives! (y/n): ")
        return False if answer == "n" else checkMatchWord(game, guess)
    elif guess in game.tries or guess in game.hidden:
        print("You already tried that letter, silly. ")

        return False
    else:
        return True

def checkMatchWord(game, guess):
    if (guess == game.plain_text):
        print(f"Congrats, you won! The word was {game.plain_text}")
        exit(0)
    else:
        print("You guessed the wrong word! Try again")
        game.lives -= 1
        game.tries.append(guess)
        print(game.lives)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

main()

