import numpy as np
import time
import os

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def read_data(path='data/data.txt'):
    # txt file obtained from Platzi Course:
    # "Clases del Curso de Python: Comprehensions, Lambdas y Manejo de Errores"
    f = open('data/data.txt', 'r', encoding="utf-8")
    f = f.read()

    for x in '-.,\n':
        f = f.replace(x,' ')
    words = f.split()

    return words
    
def display(tries):
    frames =['''
        +---+
            |
            |
            |
        =====''','''
        +---+
        O   |
            |
            |
        =====''','''
        +---+
        O   |
        |   |
            |
        =====''','''
        +---+
        O   |
       /|   |
            |
        =====''','''
        +---+
        O   |
       /|\  |
            |
        =====''','''
        +---+
        O   |
       /|\  |
       /    |
        =====''','''
        +---+
        O   |
       /|\  |
       / \  |
        =====''']
    return frames[6-tries]

def game(words):
    print("LET'S PLAY HANGMAN")
    time.sleep(0.5)    
    print("Choosing a word...")
    chosen_word = normalize(np.random.choice(words).upper())
    #chosen_word_letters = [letter for letter in chosen_word]
    word_completion = "_" * len(chosen_word)
    word_guessed = False
    tries = 6
    guessed_letters = []
    time.sleep(1)
    print(display(tries), '\n', word_completion)
    #print(chosen_word)
    
    while not word_guessed and tries > 0:
        try:
            guess = normalize(input('Choose a letter: ').upper().strip())
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print('You already tried that word. Choose another:')
                elif guess not in chosen_word:
                    print(guess, 'is not part of the word')
                    tries -= 1
                    print(display(tries), '\n', word_completion)
                    guessed_letters.append(guess)
                else:
                    print(guess, 'is part the word!')
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    print(display(tries), '\n', word_completion)
                    guessed_letters.append(guess)
                    if "_" not in word_completion:
                        word_guessed = True
            else:
                print('You can only pick letters')
                print(display(tries), '\n', word_completion)
        except ValueError:
            print('You can only pick individual letters')
    if word_guessed == True:
        print('Congratulations! You just won!')
    else:
        print('You lose. The word was: "{}"'.format(chosen_word))


def main():
    words = read_data()
    game(words)
    while input('Want to play again? (Y/N) ').upper() == 'Y':
        game(words)
    
if __name__ == "__main__":
    main()