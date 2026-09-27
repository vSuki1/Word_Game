"""
Word Game

Author: Disukhi Ahmed

Recreating Wordle in vs code
"""


import random

# dictionary with lists of word organized by length
words = {
    4: [
        "book",
        "tree",
        "fish",
        "blue",
        "game"
    ],

    5: [
        "apple",
        "house",
        "plant",
        "chair",
        "water",
        "green",
        "bread",
        "mouse",
        "table",
        "light"
    ],

    6: [
        "school",
        "planet",
        "friend",
        "animal",
        "yellow"
    ]
}

"""Ask the player to choose a word length between 4 5 6 and returns the chosen length."""
def choose_word():
     choice = int(input("Choose a word length, 4, 5 or 6:"))

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
answer = random.choice(words[word_length])
    


game_stats = {
    "attempts": 0,
    "won": False

}
print("This is the word game, try to guess the word, you have 6 attempts. g means wrong letter wrong position, y means correct letter wrong position, x means letter not in the word")

# The game continues until the player wins or uses all six attempts
while game_stats["won"] == False and game_stats["attempts"] < 6:
    
    guess = input("enter a guess: ").lower()

    if len(guess) != word_length:
        print(guess, "is not", word_length, "letters long")
        continue

    game_stats["attempts"] += 1

    result = ["x"] * word_length
    for i in range(word_length):
        if guess[i] == answer[i]:
            result[i] = "g"
        elif guess[i] in answer:
            result[i] = "y"

    if guess == answer:
            game_stats["won"] = True
            print("You guessed the word")
    

    print("Result:", result)
    if game_stats["attempts"] == 6 and game_stats["won"] == False:
        print("You ran out of attempts. The word was:", answer)
    