import os
import random
from words import words


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[tries])


def display_game(tries, word_spaces, used_letters):
    print(word_spaces)
    print("Tentativas restantes: {}".format(tries))
    print("Letras usadas: {}".format(used_letters))
    display_hangman(tries)


def get_word():

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def letter_choice(used_letters):
    letter = '0'
    while letter.upper() in used_letters or letter.upper() not in alphabet:
        letter = input("Digite uma letra: ")

    return letter


def guess(word_list, letter, tries, word_spaces, used_letters):

    i = 0
    for i in range(len(word_list)):
        if letter in word_list:
            if word_list[i] == letter:
                word_spaces = word_spaces[:i] + letter + word_spaces[i + 1:]
            wrong_choice = True
        else:
            wrong_choice = False

    if wrong_choice is False:
        tries = tries - 1

    used_letters.append(letter)
    return tries, word_spaces


def game_state(word_spaces, tries, word):
    if tries == 0:
        print("GAME OVER\n")
        print("A palavra era: {}".format(word))
        return True

    elif "_" not in word_spaces:
        print("Você ganhou, a palavra é {}".format(word))
        return True

    else:
        return False


def keep_playing():
    opcao = ''
    while opcao not in ['S', 'N']:
        opcao = input('Deseja continuar jogando? (S/N)')
        if opcao.upper() == 'S':
            return True
        elif opcao.upper() == 'N':
            print("Obrigado por jogar!")
            return False

