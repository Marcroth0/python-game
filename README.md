# Python Hangman Game

![headshot](assets/images/headshot-readme.png)

Live link: https://thawing-hamlet-48348.herokuapp.com/

### Table of Contents

1. [Goals](#goals)
    1. [Organisational Goals](#organisation-goals)
    2. [User Stories](#user-stories)
2. [Whatever](#)
    1. [Whatever](#)
    2. [Whatever](#)
    3. [Whatever](#)
3. [Planning](#planning)
    1. [Whatever](#)
4. [Testing](#testing)
    1. [Lighthouse](#lighthouse)
    2. [Validator](#validator-testing)
5. [Credits](#credits)

## Goals

### Organisation Goals

-   As a creator I want to portray a game that flows smoothly
-   As a creator I want to let the player choose between difficulties
-   As a creator I want to make sure the player enjoys their game


### User Stories

1. As a user I want to easily know the rules of the game
2. As a user I want to easily understand how to start the game
3. As a user I need to know what my score is
4. As a user I need to know when the game has been won


### Development Plane

The end goal is to create a smooth-running game that lets the player with ease dive into the world of word-guessing. 

## Strategy

The strategy is to create a clear and funny game based on the classic Hangman with a few twists. The twists being a scary/vindictive/halloween-ey theme. In order to complete the game the user stories had to be answered. 




## Planning

The planning phase was made in stages, starting off with a generalised overview and then advancing into specifics. 

### Flowcharts

<br>
The over-all birds-eye view of the game is as below, in which you'll find the general flow of the game: 
<details close>
<summary>General Flowchart</summary>

![general-flowchart](assets/images/flowchart-big-readme.png)

</details>
<br>

## Upgradability

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

 Or another one: 
1. Add a wordsL4 list of whatever words you want in the IMPOSSIBLE-difficulty
2. Add whatever imagery (HANGMANPICS), e.g removing or adding levels, and name it HANGMANPICS_IMPOSSIBLE
3. Extend the above code with to:

```
if choice == 'EASY':
            startGame(wordsL1, HANGMANPICS_EASY, name)
        elif choice == 'HARD':
            startGame(wordsL2, HANGMANPICS_HARD, name)
        elif choice == 'INSANE':
            startGame(wordsL3, HANGMANPICS_INSANE, name)
        elif choice == 'IMPOSSIBLE':
            startGame(wordsL4, HANGMANPICS_IMPOSSIBLE, name)
```

## Functions

 The ability to enter your name, which personalizes the experience of the game: 

![functions-name](assets/images/functions-name-readme.png)

 Immediately after you input your name, the rules of the game are displayed, as well as the ability to always be able to type "exit" if you should want to quit the game: 
 (User stories: 1. As a user I want to easily know the rules of the game)

![functions-rules](assets/images/functions-rules-readme.png)

 In order to start the game, one is asked whether they want it Easy or Hard:
 (User stories: 2. As a user I want to easily understand how to start the game) 

![functions-difficulty](assets/images/functions-difficulty-readme.png)

 After choosing, the game starts, and instantly lets the player know the amount of lives, the fact that the guessed letters will be saved for them, and where to enter their letter:
 (User stories 1/3: As a user I want to easily know the rules of the game/As a user I need to know what my score is)

![functions-start](assets/images/functions-start-readme.png)
 
 In order to let the player know they've guessed the word incorrectly, the lives will go down as well as print the wrongly put letter in "Tried letters/words":

![functions-incorrect](assets/images/functions-incorrect-readme.png)

While the player tries to guess an entire word a warning pops up letting the user know that if they decide to be brave, they might lose a life: 

![functions-word](assets/images/functions-word-readme.png)

In order to let the player know they've guessed the word correctly and won, before running out of lives, the below function will display:
(User stories: 4. As a user I need to know when the game has been won)

![functions-win](assets/images/functions-win-readme.png)

In order to let the player know they've ran out of lives and lost the game. The user is also made aware of the actual word, as well as being able to play again:

![functions-loss](assets/images/functions-loss-readme.png)

### Heckling

Or the nicer phrasing "interaction with the player" - which is a key part of playing any game, more so in a python terminal game where the gaming experience is quite linear. So in order to bring the game alive I've added interaction in three steps: 

Three lives remaining: 

![functions-heckle1](assets/images/functions-heckle1-readme.png)

Two lives remaining:

![functions-heckle2](assets/images/functions-heckle2-readme.png)

One life remaining: 

![functions-heckle3](assets/images/functions-heckle3-readme.png)


Lastly, a complete run-through of the game: 

https://user-images.githubusercontent.com/86383017/140244395-2610532f-4ae3-4d97-87a9-42801440fa90.mov


## Testing

**Browsers:**

-   Chrome
-   Mozilla Firefox
-   Safari
-   Edge

### Functional testing

A buncha gifs in separate file or drop-down.


### Validator Testing

## Issues

So many. 

## Unfixed Bugs


## Improvements


## Features Left to Implement


## Deployment


## Credits

-   
-   A general shout-out to [StackOverflow](https://stackoverflow.com/)

## Media

-   
