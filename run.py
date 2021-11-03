import random
import time

wordsL1 = ["DRAGON", "ENGULFED", "DIAMONDS", "JEWELS", "TREASURE", "DESTRUCTION"]
wordsL2 = ["PHENOMENON", "ONOMATOPOEIA", "DISINTERESTED", "IRREGARDLESS"]


class HangmanGame: 
    def __init__(self, wordsList, imageArray, name):
        self.wordsToPlay = wordsList
        self.plain_text = random.choice(wordsList)
        self.hidden = ("_" * len(self.plain_text))
        self.tries = []
        self.displayedImage = imageArray
        self.lives = len(self.displayedImage) -1
        self.name = name

    def updateHidden(self, index):
        self.hidden = self.hidden[:index] + self.plain_text[index] + self.hidden[index+1:]


def main():
    print( """ _   _______ _     _______  ___  _   _ 
              | | / |  _  | |   ( |  _  \/ _ \| \ | |
              | |/ /| | | | |   |/| | | / /_\ |  \| |
              |    \| | | | |     | | | |  _  | . ` |
              | |\  \ \_/ | |____ | |/ /| | | | |\  |
              \_| \_/\___/\_____/ |___/ \_| |_\_| \_/
                                       """)
    print("At last! At last a challenger appears...")
    time.sleep(1)
    print("Many have come, none have left. What makes you think you will be the first to \ndefeat the Skull of Kol'dan?")
    time.sleep(1)
    print("Centuries upon centuries I've feasted on the souls of these trials. \nTell me, what is your name?")
    print("\n")
    name = input("Enter your name: ")
    time.sleep(1)
    print("Oh, another " + name +  " have already perished upon the sight of me. Will you be the \nsecond?")
    time.sleep(1)
    print("\n")
    print("If you should ever fear, typing 'exit' will always let you out...Somewhat \nunscaved.")
    time.sleep(1.5)
    print("\n")
    print("The rules are simple, even for a simpleton:\n- A word is to be found.\n- A simple letter per proposal.\n- Perhaps in the end you will be crowned.\n- A set of lives at your disposal. ")
    time.sleep(1)
    print("\n")

    while True:
        
        choice = input("Easy or hard? Enter 'easy' for Easy, and 'hard' for Hard: ").upper()
        #Check if they actually want to play, if so:
        if choice == 'EASY':
            startGame(wordsL1, HANGMANPICS_EASY, name)
        elif choice == 'HARD':
            startGame(wordsL2, HANGMANPICS_HARD, name)
        elif choice == 'EXIT':
            print(f"Sad to see you go, " + name + ". All things must come to an end.")
            exit(0)
        else:
            print("Please enter (easy/hard) or (exit) to quit")


def startGame(listOfWords, lives, name):
    game = HangmanGame(listOfWords, lives, name)
    print("----------- THE GAME BEGINS----------")
    displayInfo(game)
    
    while(game.lives > 0 and game.hidden != game.plain_text):
        guess = input("Please enter a guess, it must be a letter!, go ahead: ").upper()
        if validateInput(game, guess):
            matchedIndexes = (checkMatch(game, guess))
            if len(matchedIndexes):
                updateDisplayedWord(game, matchedIndexes)
            else:
                game.tries.append(guess)
                game.lives -= 1
                print(f"Hah! {game.name}, Look at you trying your best!")    
            displayInfo(game)
            winOrLose(game)
            

def checkMatch(game, guess):
    return [i for i, ltr in enumerate(game.plain_text) if ltr == guess]

def updateDisplayedWord(game, list):
    for idx in list:
        game.updateHidden(idx)

def playAgain(game):
    playAgain_question = input("Wanna play again? (y/n): ").upper()
    if playAgain_question == "Y":
        return
    elif playAgain_question == "N":
        print(f"Sad to see you go, {game.name}. All things must come to an end.")
        exit(0)

def winOrLose(game):
    if (game.hidden == game.plain_text):
        print(f"Congrats, you won! The word was {game.plain_text}")
        print("I guess there had to be a first...")
        playAgain(game)
    elif(game.lives == 0):
        print(game.displayedImage[-1])
        print(f"You lost, {game.name}! The word was {game.plain_text}")
        print(f"Another one to add to my collection!")
        playAgain(game)

def validateInput(game, guess):
    if not guess.isalpha():
        print("Please enter a letter [a, b, c ..]: ")
        return False
    elif guess == "EXIT":
        print(f"Sad to see you go, {game.name}. All things must come to an end.")
        exit(0)
    elif len(guess) > 1:
        answer = input(f"Are you sure you want to guess the whole word, {game.name}? It's gonna cost you lives! (y/n): ")
        return False if answer == "n" else checkMatchWord(game, guess)
    elif guess in game.tries or guess in game.hidden:
        print(f"You already tried that letter, {game.name}")
        return False
    else:
        return True

def checkMatchWord(game, guess):
    if (guess == game.plain_text):
        game.hidden = game.plain_text
        print(f"Congrats, you won! The word was {game.plain_text}")
        playAgain(game)
    else:
        print("You guessed the wrong word! Try again")
        game.lives -= 1
        game.tries.append(guess)
        print(game.lives)

def displayInfo(game):
    print("\n")
    print(game.displayedImage[-game.lives-1])
    print("\n")
    print(game.hidden)
    print("\n")
    print("Tried letters/words: ")
    print(*game.tries, sep = ", ")
    print("\n")
    print(f"Lives: {game.lives}")
    print("\n")

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