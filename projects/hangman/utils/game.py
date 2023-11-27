import random

class Hangman:
    # List of possible words for the Hangman game
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        self.word_to_find = []               # Choose a random word to guess
        self.correctly_guessed_letters = []  # List to track correctly guessed letters
        self.wrongly_guessed_letters = []    # List to track wrongly guessed letters
        self.lives = 5                       # Number of lives the player has
        self.turn_count = 0                  # Number of turns played
        self.error_count = 0                 # Number of errors made
    
    
    def choose_word(self):
        """
        Function to choose a random word from the list of possible words.
        Returns:
            list: A list of characters representing the chosen word.
        """
        return list(random.choice(self.possible_words))

    def display_word(self):
        """
        Function to display the current state of the word with underscores for unknown letters.
        Returns:
            str: The word with underscores for letters not guessed and letters for guessed letters.
        """
        return ' '.join([letter if letter in self.correctly_guessed_letters else '_' for letter in self.word_to_find])

    def play(self):
        """
        Function to play the Hangman game.
        This function interacts with the player, handles guesses, and determines the game outcome.
        Returns:
            None
        """
        # Access instance-specific attributes using self
        self.word_to_find = self.choose_word()
        
        while self.lives > 0:
            guess = input(f"Word: {self.display_word()}\nLives: {self.lives}\nGuess a letter: ").lower()
            
            # Check if the input is a valid single letter
            if len(guess) != 1 or not guess.isalpha(): 
            # if not re.match(r'^[a-zA-Z]$', guess):
                print("Please enter a single letter.")
                continue
            
            
            if guess in self.word_to_find:
                # If the guessed letter is in the word, update correctly guessed letters
                for i, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        self.correctly_guessed_letters.append(guess)
            else:
            # If the guessed letter is not in the word, update wrongly guessed letters and reduce lives                
                self.wrongly_guessed_letters.append(guess)
                self.error_count += 1
                self.lives -= 1
            
            self.turn_count += 1
            
            if all(letter in self.correctly_guessed_letters for letter in self.word_to_find):
            # If all letters in the word have been guessed correctly, the player wins
                print(f"Congratulations! You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
                break
        else:
            # If lives run out, the player loses
            self.game_over()

    def start_game(self):
        """
        Function to start the Hangman game.
        Returns:
            None
        """
        self.play()

    def game_over(self):
        """
        Function to handle the game over scenario when the player runs out of lives.
        Returns:
            None
        """
        print("Game is over. You ran out of lives.")
