

from wordle_game import WordleGame
from wordle import load_wins, save_wins

def test_save_wins(tmp_path):
    path = tmp_path / "wins.json"
    save_wins(3)
    wins = load_wins()
    
    assert wins == 3
def test_correct_guess():
    game = WordleGame("apple")
    game.make_guess("apple")
    assert game.won == True

def test_incorrect_guess():
    
    game = WordleGame("apple")
    game.make_guess("house")
    assert game.won == False

def test_attempts():
    
    game = WordleGame("apple")
    game.make_guess("house")
    assert game.attempts == 1

def test_invalid_length():
   
    game = WordleGame("apple")
    game.make_guess("cat")
    assert game.attempts == 0

def test_correct_list():
   
    game = WordleGame("tests")
    result = game.make_guess("tests")
    assert result == ["g", "g", "g", "g", "g"]