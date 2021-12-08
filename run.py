import random
import time

# Word lists for Easy and hard
wordsL1 = [
    "DRAGON", "ENGULFED", "DIAMONDS", "JEWELS", "TREASURE", "DESTRUCTION"
]
wordsL2 = ["PHENOMENON", "ONOMATOPOEIA", "DISINTERESTED", "IRREGARDLESS"]


class hangman_game:
    """
    Hangman class containing all information needed to run the game.
    Allows the same functions to be used no matter the existing
    difficulties or added ones, as well as further improvement
    """
    def __init__(self, wordsList, imageArray, name):
        self.word_to_play = wordsList
        self.plain_text = random.choice(wordsList)
        self.hidden = ("_" * len(self.plain_text))
        self.tries = []
        self.displayed_image = imageArray
        self.lives = len(self.displayed_image) - 1
        self.name = name

    def update_hidden(self, index):
        self.hidden = self.hidden[:index] + \
            self.plain_text[index] + self.hidden[index+1:]


def main():
    """
    Holds the welcoming message and choice of difficulty
    """
    print("""
                    #########################################
                     _   _______ _     _______  ___  _   _
                     | | / |  _  | |   ( |  _  \/ _ \| \ | |
                     | |/ /| | | | |   |/| | | / /_\ |  \| |
                     |    \| | | | |     | | | |  _  | . ` |
                     | |\  \ \_/ | |____ | |/ /| | | | |\  |
                     \_| \_/\___/\_____/ |___/ \_| |_\_| \_/

                    #########################################
                                       """)
    print("At last! At last a challenger appears...")
    time.sleep(1)
    print("Many have come, none have left.",
          "\nWhat makes you think you will be",
          "the first to defeat the Skull of Kol'dan?")
    time.sleep(1)
    print("Centuries upon centuries I've",
          "feasted on the souls of these trials.",
          "\nTell me, what is your name?\n")
    name = input("Enter your name: ")

    while (not name.isalnum()):
        print("Please provide an alphanumeric value")
        name = input("Enter your name: ")

    time.sleep(1)
    print(
        "Oh, another " + name + " have already perished upon the sight of me.",
        "\nWill you be the second?")
    time.sleep(1)
    print("\nIf you should ever fear, typing 'exit'",
          "will always let you out...Somewhat unscaved.")
    time.sleep(1.5)
    print("\nThe rules are simple, even for a simpleton:\n",
          "- A word is to be found.\n", "- A simple letter per proposal.",
          "- Perhaps in the end you will be crowned.\n",
          "- A set of lives at your disposal.\n ")
    time.sleep(1)

    while True:

        choice = input(
            "Easy or hard? Enter 'easy' for Easy, 'hard' for Hard: ").upper()
        if choice == 'EASY':
            start_game(wordsL1, HANGMANPICS_EASY, name)
        elif choice == 'HARD':
            start_game(wordsL2, HANGMANPICS_HARD, name)
        elif choice == 'EXIT':
            print("Sad to see you go, " + name +
                  ". All things must come to an end.")
            exit(0)
        else:
            print("Please enter (easy/hard) or (exit) to quit")


def start_game(list_of_words, lives, name):
    """
    Starts the game, with chosen difficulty, as well
    as the while loop containing the games functions
    """
    game = hangman_game(list_of_words, lives, name)
    print("----------- THE GAME BEGINS -----------")
    display_info(game)

    while (game.lives > 0 and game.hidden != game.plain_text):
        guess = input(
            "Please enter a guess, it must be a letter/word: ").upper()
        if validate_input(game, guess):
            matched_indexes = (check_match(game, guess))
            if len(matched_indexes):
                update_displayed_word(game, matched_indexes)
            else:
                game.tries.append(guess)
                game.lives -= 1
            display_info(game)
            win_or_lose(game)


def check_match(game, guess):
    """
    Checks whether a guess is equal to the word to be guessed
    """
    return [i for i, ltr in enumerate(game.plain_text) if ltr == guess]


def update_displayed_word(game, list):
    """
    Displays a correctly guessed letter at the correct index
    """
    for idx in list:
        game.update_hidden(idx)


def play_again(game):
    """
    Allows the player to play again, letting them again choose the
    difficulty, and restart the game
    """
    play_again_question = input("Wanna play again? (y/n): ").upper()
    if play_again_question == "Y":
        return
    elif play_again_question == "N":
        print(f"Sad to see you go, {game.name}.",
              "All things must come to an end.")
        exit(0)
    else:
        print("Incorrect value provided, please enter your response again.\n")
        play_again(game)


def win_or_lose(game):
    """
    Checks whether or not the player has won or lost
    Prints messages accordingly, as well as offers the player
    to play again calling correct function
    """
    if (game.hidden == game.plain_text):
        print(f"Congrats, you won! The word was {game.plain_text}")
        print("I guess there had to be a first...")
        play_again(game)
    elif (game.lives == 0):
        print(game.displayed_image[-1])
        print(f"You lost, {game.name}! The word was {game.plain_text}")
        print(f"Another one to add to my collection!")
        play_again(game)


def validate_input(game, guess):
    """
    Validates the players input - makes sure it's alphabetical
    Controls if the player wants to guess an entire word
    Controls if the player guesses an already guessed letter/word
    """
    if not guess.isalpha():
        print("Please enter a letter [a, b, c ..]: ")
        return False
    elif guess == "EXIT":
        print(f"Sad to see you go, {game.name}.",
              "All things must come to an end.")
        exit(0)
    elif len(guess) > 1:
        print(f"Are you sure you want to guess the whole word, {game.name}?")
        answer = input("It's gonna cost you lives! (y/n): ")
        while (answer != "y" and answer != "n"):
            print("Please provide a valid answer")
            answer = input("(y/n): ")
        return False if answer == "n" else check_matchWord(game, guess)
    elif guess in game.tries or guess in game.hidden:
        print(f"You already tried that letter, {game.name}")
        return False
    else:
        return True


def check_matchWord(game, guess):
    """
    Controls whether or not a guessed word matches
    """
    if (guess == game.plain_text):
        game.hidden = game.plain_text
        print(f"Congrats, you won! The word was {game.plain_text}")
        play_again(game)
    else:
        print("You guessed the wrong word! Try again")
        game.lives -= 1
        game.tries.append(guess)
        print(game.lives)


def display_info(game):
    """
    Displays the information needed for the flow of the game, such
    as lives, the skull, heckles, and attempted incorrect words
    """
    print("\n")
    print(game.displayed_image[-game.lives - 1])
    print("\n")
    print(game.hidden)
    print("\n")
    print("Tried letters/words: ")
    print(*game.tries, sep=", ")
    print(f"Lives: {game.lives}")
    print("\n")
    if game.lives == 3:
        print("Three little lives went out for a stroll...")
    elif game.lives == 2:
        print(f"THIS IS THE TIME FOR PANIC, {game.name}!")
        print("Is this the last breath before the neverending plunge?")
    elif game.lives == 1:
        print("*Gulp*")


# Pictures used for difficulty: Easy
HANGMANPICS_EASY = [
    '''
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
'''
]

# Pictures used for difficulty: Hard
HANGMANPICS_HARD = [
    '''
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
''', '''
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
'''
]

main()
