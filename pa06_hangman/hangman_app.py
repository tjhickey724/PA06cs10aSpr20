"""
    Authors: Timothy Hickey, Zeline Tricia Bartolome

   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
words = "this is a string of words".split()

def generate_random_word():
   """ read a list of words from a file and pick a random one to return """
   return random.choice(words)

    
def play_hangman():
    want_to_play = True


    while (want_to_play):
        guessed_letters = []
        guesses_left = 6
        word = "cat" #generate_random_word()
        letter = 'a' #"ask the user for a letter"
        done = False
        while not done:
            if letter in guessed_letters:
                print("subtract one from guesses_left")
                print("and tell them they already guessed that letter")

            elif letter not in word:
                print("""add letter to guessed letters"
                "tell user the letter is not in the word"
                "subtract one from the guesses_left" """)
            else:
                print(""" add letter to guessed letters"
                "tell user the letter is in the word" """)
            if  False: #"all the letters in the word have been guessed":
                "set done to be true and tell the user they won!"
            elif  False: #"the number of guesses left is zero":
                "set done to be true and tell the user they lost!"
            else:
                print("print the word with a dash for each letter not in guessed_letters")
                done = True
                letter = 'e' # "ask the user for another letter"
        want_to_play = False #"ask the user if they want to play another game..."

if __name__ == '__main__':
    play_hangman()
