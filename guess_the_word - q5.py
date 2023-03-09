#!/usr/bin/python

# 5. Create a guess the word game (computer knows the word, player has to guess)

# Define some constants. A constant is a variable whose value never changes
# In Python, we define constants with an upper case variable name as below
COMPUTER_WORD = 'derelict'
CLUES = [
    f'It has {len(COMPUTER_WORD)} letters',
    'It rhymes with clicked',
    'A synonym is abandoned',
    'It starts with d'
]

# Set our possible clue frequency values
EASY = 1
MEDIUM = 2
HARD = 3
IMPOSSIBLE = 0

# Put those clue frequencies in a list ordered by difficulty
DIFFICULTIES = [EASY, MEDIUM, HARD, IMPOSSIBLE]


def is_the_computer_word(word):
    # ensure that we use .lower to be case-insensitive
    return word.lower() == COMPUTER_WORD.lower()


def letters_in_common(word):
    # Create a list with an underscore for each letter of the computer word
    letters = ['_'] * len(COMPUTER_WORD)

    # Enumerate over our given word but only up to the length of the computer word
    for i, letter in enumerate(word[:len(COMPUTER_WORD)]):
        # If the letter at index i is the same as our letter then update our list with that letter
        if COMPUTER_WORD[i] == letter.lower():
            letters[i] = letter

    # Return a string of our letters rather than a list
    return "".join(letters)


def should_print_clue(iteration_number, clue_frequency):
    # If we're on impossible difficulty, don't give any clues
    if clue_frequency == IMPOSSIBLE:
        return False
    # Otherwise, return a clue only every clue_frequency iterations
    return iteration_number % clue_frequency == 0


def print_clue(num_clues_given):
    # Check whether we have any other clues left
    if num_clues_given >= len(CLUES):
        # Notice the escaped apostrophe
        print('I\'m all out of ideas for clues, sorry!')
        return
    # If we have clues left, print a clue out with an f string using num_clues_given as the index of the clue
    print(f'Clue: {CLUES[num_clues_given]}')


def is_valid_difficulty(difficulty):
    # Make sure we have a number and that it is between 0 and 4
    return difficulty.isnumeric() and int(difficulty) in list(range(0, len(DIFFICULTIES)))


def get_clue_frequency_string(chosen_clue_frequency):
    # Get a nicely formatted string to tell the player how often they will get a clue
    # Could have used match case pattern matching here but opted for standard if, elif, else
    if chosen_clue_frequency == IMPOSSIBLE:
        clue_frequency_string = 'No clues for you!'
    elif chosen_clue_frequency == EASY:
        clue_frequency_string = 'You\'ll get a clue every turn'
    elif chosen_clue_frequency == MEDIUM:
        clue_frequency_string = 'You\'ll get a clue every other turn'
    else:
        clue_frequency_string = f'You\'ll get a clue every {chosen_clue_frequency} turns'

    return clue_frequency_string


def select_difficulty():
    # Keep looping until player chooses a valid difficulty and then return that
    while True:
        # Have to be len(DIFFICULTIES) - 1 as we are counting from 0
        difficulty = input(f'Select your difficulty from 0 to {len(DIFFICULTIES) - 1}: ')
        if is_valid_difficulty(difficulty):
            # Look up the clue frequency in our DIFFICULTIES list that is a constant
            chosen_clue_frequency = DIFFICULTIES[int(difficulty)]
            print(f'You chose a difficulty level of {difficulty}.', get_clue_frequency_string(chosen_clue_frequency))
            # We return here so that we immediately leave the function which therefore terminates our loop
            return chosen_clue_frequency
        print(f'Please choose a number between 0 and {len(DIFFICULTIES) - 1}.')


def game_loop(clue_frequency):
    # Run our game with the clue_frequency having been pre-selected
    clues_given = 0
    iteration = 0

    # Loop forever (or until we hit a break)
    while True:
        # If we should give a clue then give it before the first guess
        if should_print_clue(iteration, clue_frequency):
            print_clue(clues_given)
            clues_given += 1

        # Check if the player has input the correct value and break out of our loop if so
        player_word = input(f'What do you think my word is? ')
        if is_the_computer_word(player_word):
            print('You got it!')
            break

        # Otherwise, print out our string showing what is correct or not
        print(f'Not quite, you have the following letters correct: {letters_in_common(player_word)}')


# A function named main is the traditional place where, as the name implies, the main functionality should occur
def main():
    # Loop forever or until we hit a break statement
    while True:
        print('Let\'s play a game. Guess the word I\'m thinking of....')

        # Set a difficulty and then run a game with that chosen difficulty
        clue_frequency = select_difficulty()
        game_loop(clue_frequency)

        # Has the player had enough? If so call it a day
        if input('Want to play again? Y/N (default Y): ').upper() == 'N':
            print('Thanks for playing')
            break


# This conditional means that we will only run our code if this file is ran as a script
# If another python file imports this file as a module, the game will not run unless explicitly called
if __name__ == "__main__":
    main()
