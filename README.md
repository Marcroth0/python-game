# Python Hangman Game

![amiresponsive]()

Live link: 

### Table of Contents

1. [Goals](#goals)
    1. [Organisational Goals](#organisation-goals)
    2. [User Stories](#user-stories)
2. [Design](#design)
    1. [Box Shadow](#box-shadow)
    2. [Color palette day](#color-palette-day)
    3. [Color palette night](#color-palette-night)
3. [Planning](#planning)
    1. [Fonts](#fonts)
4. [Testing](#testing)
    1. [Lighthouse](#lighthouse)
    2. [Validator](#validator-testing)
5. [Credits](#credits)

## Goals

### Organisation Goals

-   As a creator I want to portray a game that flows smoothly
-   As a creator I want to let the player choose between difficulties
-   
-   

### User Stories

1. As a user I want to easily know the rules of the game
2. As a user I want to easily understand how to start the game
3. As a user I need to know what my score is
4. As a user I need to know when the game has been won


### Development Plane

The end goal is to create a smooth-running game that lets the player with ease dive into the world of word-guessing. 

## Strategy

The strategy is to create a clear and funny game based on the classic Hangman with a few twists. The twists being a scary/vindictive/halloween-ey theme. In order to complete the game the user stories had to be answered. 




### Planning

The planning phase was made in stages, starting off with a generalised overview and then advancing into specifics. 

## Flowcharts
<br>
The over-all birds-eye view of the game is as below, in which you'll find the general flow of the game: 
<details close>
<summary>General Flowchart</summary>

![general-flowchart](assets/images/flowchart-big-readme.png)

</details>
<br>
The puppetmaster behind the game - in order to make the game easily upgradable with difficulties i added a hangman class which controls it:
<details close>
<summary>Class Flowchart</summary>

![class-flowchart](assets/images/flowchart-class-readme.png)

</details>
<br>

In order to upgrade the game with more wordslists or difficulties all that was needed was to make the list and apply it in the parameter of the intended difficulty in the code. 

Example:

```
if choice == 'EASY':
            startGame(wordsL1, HANGMANPICS_EASY, name)
        elif choice == 'HARD':
            startGame(wordsL2, HANGMANPICS_HARD, name)
```

This means if you'd like to add another difficulty, let's say "INSANE" all you have to do is:
1. Add a wordsL3 list of whatever words you want in the INSANE-difficulty
2. Add whatever imagery (HANGMANPICS), e.g removing or adding levels, and name it HANGMANPICS_INSANE
3. Extend the above code with to:

```
if choice == 'EASY':
            startGame(wordsL1, HANGMANPICS_EASY, name)
        elif choice == 'HARD':
            startGame(wordsL2, HANGMANPICS_HARD, name)
        elif choice == 'INSANE':
            startGame(wordsL3, HANGMANPICS_INSANE, name)
```

Then the class with do the rest, meaning all other functions will be reusable. 

## Testing

**Browsers:**

-   Chrome
-   Mozilla Firefox
-   Safari
-   Edge

### Functional testing

### Lighthouse

![lighthouse](assets/images/lighthouse-memory-readme.png)

### Validator Testing

## Unfixed Bugs


## Improvements

## Features Left to Implement


## Deployment


## Credits

-   
-   A general shout-out to [StackOverflow](https://stackoverflow.com/)

## Media

-   