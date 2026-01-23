import random

print ("Welcome to Taahirah's game. It is just a biology version of the Hangman you know!")
print (input("Press enter to continue"))
name = (input("Kindly input your name: "))
print ("Hello " + name + ", let's start the game. Kindly read the game rules below then press enter to continue.")
print ("You have to guess the hidden word before you run out of chances.")
print ("1. The player guesses one letter at a time. You type the letter and press enter")
print ("2. If the letter is in the word, all matching positions are revealed, else one attempt is lost.")
print ("3. The player wins by guessing all letters in the word before attempts run out.")
print ("4. The player loses if all 6 allowed wrong guesses are used before the word is complete.")
print ("5. All words are 6 letter and you will get only 3 hints: 2 before starting and 1 after 3 wrong guesses!")
print (input())

class Hangman:
    def __init__(self, word_file):
        # Load words with hints
        with open(word_file, "r") as file:
            content = file.read()
            self.words_with_hints = eval(content)  # dictionary

        # Pick a random secret word
        self.secret_word = random.choice(list(self.words_with_hints.keys()))

        # Display underscores
        self.display = ["_"] * len(self.secret_word)

        # Track guessed letters
        self.guessed_letters = []

        # Track wrong guesses
        self.wrong_guesses = 0

        # Hints for this word
        self.hints = self.words_with_hints[self.secret_word]

    def show_hints(self):
        print("\nHints for this word:")
        for hint in self.hints[:2]:  # first 2 hints
            print("-", hint)
        print()  # empty line

    def show_progress(self):
        print("Word:", " ".join(self.display))

    def process_guess(self, guess):
        if guess in self.guessed_letters:
            print(f"You already guessed '{guess}'! Try another letter.")
            return

        self.guessed_letters.append(guess)

        if guess in self.secret_word:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == guess:
                    self.display[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            self.wrong_guesses += 1
            print(f"Wrong guess! Total wrong guesses: {self.wrong_guesses}")

            # Show 3rd hint after 3 wrong guesses
            if self.wrong_guesses == 3 and len(self.hints) > 3:
                print("Additional hint:", self.hints[2])

        self.show_progress()

    def is_won(self):
        return "_" not in self.display

    def is_lost(self, max_wrong=6):
        return self.wrong_guesses >= max_wrong

    def play(self):
        # Show initial hints and progress
        self.show_hints()
        self.show_progress()

        while not self.is_won() and not self.is_lost():
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please type a single letter.")
                continue
            self.process_guess(guess)

        # Game result
        if self.is_won():
            print(f"Congratulations! You guessed the word: {self.secret_word}")
        else:
            print(f"Game over! The word was: {self.secret_word}")

game = Hangman("secret-words.txt")
game.play()





       
