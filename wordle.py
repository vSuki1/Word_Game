"""
Word Game

Author: Disukhi Ahmed

Recreating Wordle in vs code
Used w3schools tutorials for learning Python range in while loops.


"""


import random
from wordle_game import WordleGame
from pathlib import Path

def load_words(word_length):


    files = {
        4: Path("four_letter_words.txt"),
        5: Path("five_letter_words.txt"),
        6: Path("six_letter_words.txt")
    }

    try:
        file = files[word_length].open("r", encoding="utf-8")
        words = [word.lower() for word in file.read().splitlines()]
        file.close()
        return words
    except FileNotFoundError:
        print("Word file not found.")
        return []


def main():
    print("This is the word game, try to guess the word, you have 6 attempts. g means correct letter correct position, y means correct letter wrong position, x means letter not in the word")
    """Ask the player to choose a word length between 4 5 6 and returns the chosen length."""

    def choose_word():
        choice = int(input("How many letters should the word have? Choose a word length , 4, 5 or 6: "))

        if choice == 4:
            return 4
        elif choice == 5:
            return 5
        elif choice == 6:
            return 6
        else:
            print("Invalid choice")
            return choose_word()
        
    word_length = choose_word()
    words = load_words(word_length)

    if not words:
        print("No words available.")
        return

    answer = random.choice(words)
    game = WordleGame(answer)

 


    while not game.won and game.attempts < game.max_attempts:
        """ The game continues until the player wins or uses all six attempts """
        guess = input("Guess the word: ").lower()

        if len(guess) != word_length:
            print(guess, "is not", word_length, "letters long")
            continue

        result = game.make_guess(guess)
        if result is None:
            print("Invalid guess")
            continue

        if guess == answer:
                game.won = True
                print("You guessed the word")
        

        print("Result:", result)
        if game.attempts == 6 and not game.won:
            print("You ran out of attempts. The word was:", answer)

if __name__ == "__main__":
     main()