import random
wordsL1 = ["pasta", "spaghetti", "maccheroni"]

class HangmanGame: 
    def __init__(self, wordsList, lives):
        self.wordsToPlay = wordsList
        self.plain_text = random.choice(wordsList)
        self.hidden = ("_" * len(self.plain_text))
        self.lives = lives

    def updateHidden(self, index):
        self.hidden = self.hidden[:index] + self.plain_text[index] + self.hidden[index+1:]

def main():
    ## Check if they actually want to play, if so:
    game = HangmanGame(wordsL1, 5)
    tries = []
    print(game.plain_text)
    print(game.hidden)
    while(True):
        guess = input("Please enter a guess, it must be a letter!, go ahead: ")
        matchedIndexes = (checkMatch(game, guess))
        if len(matchedIndexes):
            updateDisplayedWord(game, matchedIndexes)
        else:
            tries.append(guess)
            game.lives -= 1
        
        winOrLose(game)
        print(game.hidden)
        print("Tried letters: ")
        print(tries)
        print(f"Lives: {game.lives}")

def checkMatch(game, guess):
    return [i for i, ltr in enumerate(game.plain_text) if ltr == guess]

def updateDisplayedWord(game, list):
    print(list)
    for idx in list:
        game.updateHidden(idx)

def winOrLose(game):
    if (game.hidden == game.plain_text):
        print("Congrats, you won!")
        exit(0)
    elif(game.lives == 0):
        print("You lost, poor idiot")
        exit(0)

main()