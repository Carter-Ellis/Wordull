import random

class Wordle:
    def __init__(self, word, num_guess):
        self.word = word.upper()
        self.length = len(word)
        self.num_guess = num_guess
        self.__attempts = []

    def compare_word(self, guess: str) -> bool:
        guess = guess.upper()
        self.prop_attempt(guess)
        self.print_guess()
        return guess == self.word


    def prop_attempt(self, guess) -> None:
        line = ""
        for i in range(self.length):
            if guess[i] == self.word[i]:
                line += "🟩" + guess[i]
                continue
            if guess[i] in self.word:
                line += "🟨" + guess[i]
                continue
            line += guess[i]
        self.__attempts.append(line)

    def print_guess(self) -> None:
        print("-" * 4 * self.length)
        for attempt in self.__attempts:
            temp = ""
            for c in attempt:
                if not c.isalpha():
                    temp = c
                    continue
                if len(temp) > 0:
                    print("|", end="")
                    print(c + temp, end="|")
                    temp = ""
                    continue
                print("|", end="")
                print(c, end="|")
            print("|", end="")
            print("")
            print("-" * 5 * self.length)

    def get_num_attempts(self):
        return len(self.__attempts)
while True:
    with open("words.txt") as f:
        word_list = [word.strip() for word in f.read().replace("\n", ",").split(",") if word.strip()]

    word = random.choice(word_list)
    max_guesses = 6
    wordle = Wordle(word, max_guesses)
    win = False
    print("Welcome to Wordull!")

    while True:
        try:
            guess = input(f"Enter your guess. {wordle.get_num_attempts()} / {max_guesses} attempts.\n")
            if not isinstance(guess, str):
                raise TypeError("Input must be a string.")
            if len(guess) != wordle.length:
                raise ValueError(f"Word must be {wordle.length} letters long.")
            if not guess.isalpha():
                raise ValueError("Input must contain only letters.")
            if wordle.compare_word(guess):
                win = True
                break
            if wordle.get_num_attempts() >= 6:
                break
        except (TypeError, ValueError) as e:
            print(f"Invalid input: {e}")

    if win:
        print("You guessed the correct word!")
    else:
        print(f"You did not guess the word: {word.upper()}")

    if input("Play again? [y/n]").lower() != "y":
        break
print("Goodbye!")