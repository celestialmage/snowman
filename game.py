SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]


def snowman(snowman_word):

    # creates a constant that stores the length of the snowman word
    WORD_LENGTH = len(snowman_word) 

    # using the snowman word, creates a dictionary that stores the letters and their current guesssed status
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    # list that stores the guessed incorrect letters
    wrong_guesses_list = []
    # boolean that stores the puzzle win state
    puzzle_solved = False
    # int that stores the amount of wrong guesses
    num_wrong_guesses = 0

    # while loop with the following exit conditions:
    # - the length of wrong_guesses_list equals or exceeds SNOWMAN_MAX_WRONG_GUESSES
    # - the puzzle_solved boolean's state is changed to True
    while num_wrong_guesses < SNOWMAN_MAX_WRONG_GUESSES and not puzzle_solved:

        # generates the word progress string by calling the relevant function
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)
        
        # calls the function that receives input from the user and, if the input is valid, stores that
        # value into the user_letter variable
        user_letter = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)

        # if statement with the following conditions that checks if the current input letter is found
        # in the snowman word's status dictionary
        if user_letter in correct_letter_guess_statuses:
            # if the letter is found

            # prints a status message and changes the status of the input letter to True, marking it as found
            print("You guessed a letter that's in the word!")
            correct_letter_guess_statuses[user_letter] = True
        else:
            # if the letter is not found

            # prints a status message and adds the incorrect letter to the wrong_guesses_list
            print(f"The letter '{user_letter}' is not in the word.")
            wrong_guesses_list.append(user_letter)
            # increments the wrong guess counter and then generates the snowman image
            num_wrong_guesses += 1
            print_snowman_graphic(num_wrong_guesses)

        #prints out all current incorrect guesses, separated by ", "
        print(", ".join(wrong_guesses_list))
        
        # calls the function that checks the game state and assigns the resulting value to puzzle_solved
        puzzle_solved = is_word_guessed(snowman_word, correct_letter_guess_statuses)
    
    # at this point, the game is over

    # prints the final status of the game, whether or not the word was fully guessed.
    print(generate_word_progress_string(snowman_word, correct_letter_guess_statuses))

    # if statement that checks the status of the puzzle_solved boolean variable
    if puzzle_solved:
        # if puzzle_solved resolves to True

        # print a status message that congratulates the player on win
        print("Congratulations, you win!")

    else:
        # if puzzle_solved resolves to False

        # prints a status message that consoles the player on loss and reveals the snowman_word
        print(f"Sorry, you lose! The word was {snowman_word}")


def print_snowman_graphic(wrong_guesses_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
    

def build_letter_status_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """

    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It calls another function to generate a string representation of the  
    user's progress towards guessing snowman_word and prints this string.
    """

    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It creates and returns an output string that shows the correct letter 
    guess placements as well as the placements for the letters yet to be 
    guessed.
    """

    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """

    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True