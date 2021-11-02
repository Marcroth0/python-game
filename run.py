import random
wordsL1 = ["DRAGON", "ENGULFED", "DIAMONDS", "JEWELS", "TREASURE", "DESTRUCTION"]
wordsL2 = ["PHENOMENON", "ONOMATOPOEIA", "DISINTERESTED", "IRREGARDLESS"]

class HangmanGame: 
    def __init__(self, wordsList, imageArray):
        self.wordsToPlay = wordsList
        self.plain_text = random.choice(wordsList)
        self.hidden = ("_" * len(self.plain_text))
        self.tries = []
        self.displayedImage = imageArray
        self.lives = len(self.displayedImage) -1

    def updateHidden(self, index):
        self.hidden = self.hidden[:index] + self.plain_text[index] + self.hidden[index+1:]

def main():
    while True:
        choice = input("Easy or hard? Enter 'easy' for Easy, and 'hard' for Hard: ").upper()
        ## Check if they actually want to play, if so:
        if choice == 'EASY':
            startGame(wordsL1, HANGMANPICS_EASY)
        elif choice == 'HARD':
            startGame(wordsL2, HANGMANPICS_HARD)
        elif choice == 'EXIT':
            exit(0)
        else:
            print("Please enter (easy/hard) or (exit) to quit")


def startGame(listOfWords, lives):
    game = HangmanGame(listOfWords, lives)
    print("----------- THE GAME BEGINS----------")
    print("\n")
    
    while(game.lives > 0 and game.hidden != game.plain_text):
        print(game.displayedImage[-game.lives-1])
        print("\n")
        print(game.hidden)
        print("\n")
        print("Tried letters/words: ")
        print(*game.tries, sep = ", ")
        print("\n")
        print(f"Lives: {game.lives}")
        print("\n")
        guess = input("Please enter a guess, it must be a letter!, go ahead: ").upper()
        if validateInput(game, guess):
            matchedIndexes = (checkMatch(game, guess))
            if len(matchedIndexes):
                updateDisplayedWord(game, matchedIndexes)
            else:
                game.tries.append(guess)
                game.lives -= 1
                
            
            winOrLose(game)
            # print("\n")
            # print(game.hidden)
            # print("\n")
            # print("\n")
            # print(f"Lives: {game.lives}")

def checkMatch(game, guess):
    return [i for i, ltr in enumerate(game.plain_text) if ltr == guess]

def updateDisplayedWord(game, list):
    for idx in list:
        game.updateHidden(idx)

def playAgain():
    playAgain_question = input("Wanna play again? (y/n): ").upper()
    if playAgain_question == "Y":
        return
    elif playAgain_question == "N":
        exit(0)

def winOrLose(game):
    if (game.hidden == game.plain_text):
        print(f"Congrats, you won! The word was {game.plain_text}")
        playAgain()
    elif(game.lives == 0):
        print(game.displayedImage[-1])
        print(f"You lost, poor idiot. The word was {game.plain_text}")
        playAgain()

def validateInput(game, guess):
    if not guess.isalpha():
        print("Please enter a letter [a, b, c ..]: ")
        return False
    elif guess == "exit":
        exit(0)
    elif len(guess) > 1:
        answer = input("Are you sure you want to guess the whole word? It's gonna cost you lives! (y/n): ")
        return False if answer == "n" else checkMatchWord(game, guess)
    elif guess in game.tries or guess in game.hidden:
        print("You already tried that letter, silly. ")
        return False
    else:
        return True

def checkMatchWord(game, guess):
    if (guess == game.plain_text):
        game.hidden = game.plain_text
        print(f"Congrats, you won! The word was {game.plain_text}")
        playAgain()
    else:
        print("You guessed the wrong word! Try again")
        game.lives -= 1
        game.tries.append(guess)
        print(game.lives)


HANGMANPICS_EASY = ['''
           ______
        .-"      "-.
      //            \\
      |              |
      |,            ,|
      | )          ( |
      |/            \|
      (_            _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,       .-.  ,|
      | )      \__)( |
      |/            \|
      (_            _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/            \|
      (_            _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__        __/
        | \IIIIII/ |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
''']

HANGMANPICS_HARD = ['''
           ______
        .-"      "-.
      //            \\
      |              |
      |,            ,|
      | )          ( |
      |/            \|
      (_            _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/            \|
      (_            _)
       \__        __/
        |          |
        \          /
         `--------`
''','''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/            \|
      (_     /\     _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/            \|
      (_     ^^     _)
       \__        __/
        |          |
        \          /
         `--------`
''', '''
           ______
        .-"      "-.
      //            \\
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
''']
main()

