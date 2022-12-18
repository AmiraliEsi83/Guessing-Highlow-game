# Hi guys,
# I created a straightforward guessing game and Highlow game using the While Loop.

def guessing_game():
    print('Lets play two games')

    # At here I'm using the While loop to create a small game
    # and if you will get the answers from the define range that I mention in the bottom
    # we have a range for our random number
    random_number = range(80000, 85000)


    while True:
        # This loop for continue looping after user find the correct number
        any_number = input('What is the average salary for computer science in Canada ? Hint: Between 80000 to 90000 ')
        # if user guess the number
        if int(any_number) in random_number:
            print('You guessed it. Good Job!')
            break
            # break out the loop when you got the answer
        else:
            # if user didn't find the correct number
            print('Try again!')


def high_low():
    # At the end we have a mini High low game ...
    # we define to variables like low and high
    low = 1
    high = 1000
    # I use format because I want to change that to the actual numbers to low and high
    # I've included a tab character it makes it easier to pick out the computer guesses from the diagnostic information
    print("Please think of a number between {} and {}".format(low, high))
    # In here I call the input function so the computer waits until the user presses the enter key to start the game
    input("Press ENTER to start")

    guesses = 1
    # I use the while loop to let the computer keep guessing until it gets the answers
    # After each guess the user is going to tell the computer whether to guess higher or lower
    while low != high:

        print("\tGuessing in the range of {} to {}".format(low, high))
        # binary search formula which calculate teh midpoint between the low and high values to produce next guess
        guess = low + (high - low) // 2
        # I split the line to three to reading the code better
        high_low = input("My guess is {}. Should I guess higher or lower? "
                         "Enter h or l, or c if my guess was correct "
                         # It guaranteed that all characters changes to lowercase
                         .format(guess)).casefold()

        if high_low == "h":
            # Guess higher. The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        elif high_low == "l":
            # Guess lower. The high end of the range becomes one less than the guess.
            # if we have to guess lower, then the new high value is one less than the current guess
            high = guess - 1
        elif high_low == "c":
            print("I got it in {} guesses!".format(guesses))
            break  # computer guesses true then we break out of the while loop
        else:
            print("Please enter h, l or c")

        # guesses = guesses + 1
        guesses += 1
    else:
        # .format is using for when user find the correct answer it sets in side the print statment
        print("You thought of the number {}".format(low))
        # computer said that with how many guess it founds the correct answer
        print("I got it in {} guesses".format(guesses))

if __name__ == "__main__":
    guessing_game()
    high_low()