import random

class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'alexandre']
    word_to_find = []
    lives = 5
    correctly_guessed_letters = []
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0

    @classmethod
    def choose_word(cls):
        # Choose a random word from the list of possible words
        cls.word_to_find = list(random.choice(cls.possible_words))
        cls.correctly_guessed_letters = ['_'] * len(cls.word_to_find)

    @classmethod
    def display_word(cls):
        # Display the current state of the word with underscores for unknown letters
        return ' '.join(cls.correctly_guessed_letters)

    @classmethod
    def play(cls):
        # Function to play the Hangman game
        while cls.lives > 0:
            guess = input(f"Word: {cls.display_word()}\nLives: {cls.lives}\nGuess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            if guess in cls.word_to_find:
                for i, letter in enumerate(cls.word_to_find):
                    if letter == guess:
                        cls.correctly_guessed_letters[i] = guess
            else:
                cls.wrongly_guessed_letters.append(guess)
                cls.error_count += 1
                cls.lives -= 1

            cls.turn_count += 1

            if '_' not in cls.correctly_guessed_letters:
                print(f"Congratulations! You found the word: {''.join(cls.word_to_find)} in {cls.turn_count} turns with {cls.error_count} errors!")
                break

        else:
            cls.game_over()

    @classmethod
    def game_over(cls):
        print("Game is overed. You ran out of lives.")

    def start_game(self):
        self.choose_word()
        self.play()


if __name__ == '__main__':
    game = Hangman()
    game.start_game()
