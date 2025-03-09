# FILE NAME - while_loop_guess.py

# NAME - 
# DATE - 
# DESCRIPTION - 

def main():
    while_loop_guess()

def while_loop_guess():

    guess = -1;
    num_guesses = 0

    while (guess != 33):
        guess = int(input('Guess a number: '))
        num_guesses = num_guesses + 1

    print('You guessed in', num_guesses, 'tries.')

main()