import random
import time

wordsL1 = ['DRAGON', 'GOLDEN', 'TREASURE', 'DIAMOND', 'MOUNTAIN', 'COINS', 'ENGULFED', 'DESTRUCTION', 'DEMOLISHED']
wrong_guesses=0
global lives
guessed_char = []
attempts = []

## A welcoming message and invite to play
def main():
    # print("\n Oh, no, no, no, not you again... \n")
    # time.sleep(1)
    # print("\nRemind me, I seem to have intentionally misplaced your name. Do remind me, so I can forget again.\n")
    # name = input("Enter your forgetful name:\n")
    # time.sleep(1)
    # print("\nAnd here I thought " + name + " wasn't up for the challenge of facing me!\n")
    # time.sleep(1)
    # print("\nWell, Harold...Harold, was it? " + name + " , I know, I know. I've considered it and will allow you to play the game.\n")
    # print("\nBut before we start...")
    # time.sleep(1)
    # print("\n" + name + " Haroldsen, how about before I devour you with the shere sight of me, we start off with a riddle?\n")
    # start_game = input("Start game y/n: ")
    # if start_game == 'y':
    #     startgame()
    # else:
    #     print('Bye Felicia')
    #     exit(0)
    myword = random_words(wordsL1) 
    lives = 5
    

    while wrong_guesses < lives:
        #print(hangman_lives[lives])
        GUESS = input("Oh, do try me with a letter: ")
        charMatch(hidden_word, GUESS.upper(), lives)

## Check if the char matches
def charMatch(word, guess, lives):







## Start the game

## Random words
def random_words(list_words):
    random.shuffle(list_words)
    return list_words[0]

## Play again
def play_again():
    replay_question = input("How about another game? Enter 'Y' for yes or 'N' for no.")
    if replay_question == 'y':
        startgame()
    else:
        print("Perhaps another time.")


def hangman_lives(lives):
    
    hangman_images =  ['''
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

    return hangman_images[lives]


main()