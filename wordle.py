"""
Word Game

Author: Disukhi Ahmed

Recreating Wordle in vs code
"""


import random


words = [
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
]

answer = random.choice(words)

result_types = ("x", "y", "g")

game_stats = {
    "attempts": 0,
    "won": False

}
print("This is the word game, try to guess the 5 letter word, you have 6 attempts. g means wrong letter wrong position, y means correct letter wrong position, x means letter not in the word")
print(answer)

while game_stats["won"] == False and game_stats["attempts"] < 6:
    result = ["x", "x", "x", "x", "x"]
    guess = input("enter a guess: ").lower()

    if len(guess) != 5:
        print(guess, "is not 5 letters long")
        continue

    game_stats["attempts"] += 1


    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = "g"
        elif guess[i] in answer:
            result[i] = "y"

    print("Result:", result)
    if game_stats["attempts"] == 6 and game_stats["won"] == False:
        print("You ran out of attempts. The word was:", answer)
    if guess == answer:
        game_stats["won"] = True
        print("You guessed the word")
