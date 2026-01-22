import random

print ("Wellcome to Taahirah's game. It is just a biology version of the Hangman you know!")
print input("Press enter to continue: ")
name = (input("Kindly input your name: "))
print ("Hello " + name + ", let's start the game. Kindly read the game rules below then press enter to continue.")
print (" The Objective is guess the hidden word by suggesting letters before you run out of chances. The player guesses one letter at a time.
If the letter is in the word: All matching positions are revealed, else one attempt is lost. The player wins by guessing all letters in the word before attempts run out. 
The player loses if all allowed wrong guesses are used before the word is complete. All words are 6 letter and you will get only 3 hints")
print input()


# Load the dictionary from secret-word.txt
with open("secret-word.txt", "r") as file:
    content = file.read()
    words_with_hints = eval(content)  # Converts string to dictionary

secret_word = random.choice(list(words_with_hints.keys()))
print("SECRET WORD (for testing):", secret_word)                       #hashtag after launch






       
