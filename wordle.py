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



while game_stats["won"] == False and game_stats["attempts"] < 6:
    result = ["x", "x", "x", "x", "x"]
    guess = input("enter a guess")

    if len(guess) != 5:
        print(guess, "is not 5 letters long")
        continue

    game_stats["attempts"] += 1


    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = "g"
        elif guess[i] in answer:
            result[i] = "y"

    if guess == answer:
        game_stats["won"] = True
        print("You guessed the word")
