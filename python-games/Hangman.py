import random

# Define a list of word categories
word_categories = {
    "fruits": ["apple", "banana", "cherry", "grape", "orange", "strawberry"],
    "countries": ["india", "usa", "canada", "australia", "brazil", "japan"],
    "animals": ["elephant", "tiger", "giraffe", "kangaroo", "penguin", "rhinoceros"]
}

# Function to choose a random word from the selected category
def choose_word(category):
    if category in word_categories:
        return random.choice(word_categories[category])
    else:
        return random.choice(random.choice(list(word_categories.values())))

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    print("Welcome to Hangman!")
    
    # Ask the player to choose a word category
    while True:
        print("Choose a word category:")
        for category in word_categories:
            print(f"- {category}")
        category = input("Enter the category: ").lower()
        if category in word_categories:
            break
        else:
            print("Invalid category. Please choose a valid category.")

    word = choose_word(category)
    guessed_letters = []
    attempts = 6  # Number of attempts allowed
    
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print(f"Out of attempts. The word was '{word}'. You lose!")
                break
        
        # Check if the player has guessed all letters
        if set(word).issubset(set(guessed_letters)):
            print(f"Congratulations! You guessed the word '{word}' correctly.")
            break

# Entry point of the game
if __name__ == "__main__":
    play_hangman()
