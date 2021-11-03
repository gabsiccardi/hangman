
# Hangman
# Author: Gabriel Siccardi
# Date: 03/11/2021
# Version: 1.0.0
# Future plans: Add support for portuguese, difficulty leves and better display for the game.


import functions

game_on = True

while game_on is True:
    tries = 6
    word = functions.get_word()
    word_list = list(word)
    word_spaces = "_" * len(word)
    used_letters = []
    victory = False

    while victory is False:
        functions.display_game(tries, word_spaces, used_letters)
        letter = functions.letter_choice(used_letters)
        tries, word_spaces = functions.guess(word_list, letter.upper(), tries, word_spaces, used_letters)
        victory = functions.game_state(word_spaces, tries, word)
        if victory is True:
            game_on = functions.keep_playing()
        else:
            pass
