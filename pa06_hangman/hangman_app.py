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
   """ this is the python script version of the game """
   print("The hangman app is under construction. Try again later!")

if __name__ == '__main__':
    play_hangman()
