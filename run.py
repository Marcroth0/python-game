import random
import time

## A welcoming message and invite to play
def main():
    print("\n Oh, no, no, no, not you again... \n")
    time.sleep(1)
    print("\nRemind me, I seem to have intentionally misplaced your name. Do remind me, so I can forget again.\n")
    name = input("Enter your forgetful name:\n")
    time.sleep(2)
    print("\nAnd here I thought " + name + " wasn't up for the challenge of facing me!\n")
    time.sleep(2)
    print("\nWell, Harold...Harold, was it? " + name + " , I know, I know. I've considered it and will allow you to play the game.\n")
    print("\nBut before we start...")
    time.sleep(1)
    print("\n" + name + " Haroldsen, how about before I devour you with the shere sight of me, we start off with a riddle?\n")
    start_game = input("Start game y/n: ")
    if start_game == 'y':
        startgame()
    else:
        print('Bye Felicia')
        exit(0)

## Start the game
def startgame():
    myword = random_words(wordsL1)    
    print("_" * len(myword))

## Random words
def random_words(list_words):
    random.shuffle(list_words)
    return list_words[0]

## Already guessed words

## Play again

## Words list
wordsL1 = ['dragon', 'golden', 'treasure', 'diamond', 'mountain', 'coins', 'engulfed', 'destruction', 'demoliished']
wordsL2 = ['dragon', 'golden', 'treasure', 'diamond', 'mountain', 'coins', 'engulfed', 'destruction', 'demoliished']
## Hangman pic


## Check if right or wrong

## Check won


main()