


class WordleGame:
    

    def __init__(self, answer):
        
        self.answer = answer
        self.attempts = 0
        self.won = False
        self.word_length = len(answer)
        self.max_attempts = 6


    
    def check_guess(self, guess):
        
        result = ["x"] * self.word_length

        for i in range(self.word_length):
            if guess[i] == self.answer[i]:
                result[i] = "g"
            elif guess[i] in self.answer:
                result[i] = "y"

        return result

    def make_guess(self, guess):
        
        guess = guess.lower()

        if len(guess) != self.word_length:
            return None

        if self.won or self.attempts >= self.max_attempts:
            return None

        self.attempts += 1
        result = self.check_guess(guess)

        if guess == self.answer:
            self.won = True

        return result