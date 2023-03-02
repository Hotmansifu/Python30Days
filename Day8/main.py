import random

# List of words to choose from
words = ['python', 'java', 'javascript', 'ruby', 'php', 'swift']

# Choose a word randomly
word = random.choice(words)

# Display the word as underscores
word_display = ['_'] * len(word)
print(' '.join(word_display))

# Set up the game
max_guesses = 6
guessed_letters = []
num_guesses = 0

# Loop until the player wins or loses
while num_guesses < max_guesses:
    # Get a letter guess from the player
    guess = input('Guess a letter: ').lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter. Try again.')
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word:
        # Replace the corresponding underscores with the guess
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess

        print(' '.join(word_display))

        # Check if the player has won
        if '_' not in word_display:
            print('Congratulations! You won!')
            break
    else:
        # Increment the number of guesses and draw the corresponding part of the stick figure
        num_guesses += 1
        print('Incorrect guess. You have', max_guesses - num_guesses, 'guesses left.')

        if num_guesses == 1:
            print('   ____   ')
            print('  |    |  ')
            print('       |  ')
            print('       |  ')
            print('       |  ')
            print('       |  ')
        elif num_guesses == 2:
            print('   ____   ')
            print('  |    |  ')
            print('  O    |  ')
            print('       |  ')
            print('       |  ')
            print('       |  ')
        elif num_guesses == 3:
            print('   ____   ')
            print('  |    |  ')
            print('  O    |  ')
            print('  |    |  ')
            print('       |  ')
            print('       |  ')
        elif num_guesses == 4:
            print('   ____   ')
            print('  |    |  ')
            print('  O    |  ')
            print(' /|    |  ')
            print('       |  ')
            print('       |  ')
        elif num_guesses == 5:
            print('   ____   ')
            print('  |    |  ')
            print('  O    |  ')
            print(' /|\   |  ')
            print('       |  ')
            print('       |  ')
        elif num_guesses == 6:
            print('   ____   ')
            print('  |    |  ')
            print('  O    |  ')
            print(' /|\   |  ')
            print(' / \   | ')
            print('       |  ')
            print('You lose. The word was', word)
            break
