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

    guess = input("enter a guess")