import random

print ("Welcome to Taahirah's game. It is just a biology version of the Hangman you know!")
print (input("Press enter to continue"))
name = (input("Kindly input your name: "))
print ("Hello " + name + ", let's start the game. Kindly read the game rules below then press enter to continue.")
print ("The Objective is guess the hidden word by suggesting letters before you run out of chances.")
print ("1. The player guesses one letter at a time.")
print ("2. If the letter is in the word, All matching positions are revealed, else one attempt is lost.")
print ("3. The player wins by guessing all letters in the word before attempts run out.")
print ("4. The player loses if all allowed wrong guesses are used before the word is complete.")
print ("5. All words are 6 letter and you will get only 3 hints")
print (input())

class Hangman:
    def __init__(self, word_file):
        # Load words from file
        with open(word_file, "r") as file:
            content = file.read()
            self.words_with_hints = eval(content)  # convert string to dictionary

        # Pick a random word
        self.secret_word = random.choice(list(self.words_with_hints.keys()))

        # Create display list
        self.display = ["_"] * len(self.secret_word)

        # Keep track of guessed letters
        self.guessed_letters = []

    def show_progress(self):
        # Print current progress
        print(" ".join(self.display))

    def process_guess(self, guess):
        # Update display for matching letters
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == guess:
                self.display[i] = guess
        # Track guessed letters
        self.guessed_letters.append(guess)
        self.show_progress()

game = Hangman("secret-words.txt")
game.show_progress()

# Example: one guess
guess = input("Type a letter: ").lower()
game.process_guess(guess)







       
