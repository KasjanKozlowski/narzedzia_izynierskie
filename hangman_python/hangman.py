import random
from words import word_list


def play(word):
    word_completion = " _ " * len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Zagrajmy!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Zgadnij litere albo całe słowo: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Juz wybrales ta litere", guess)
            elif guess not in word:
                print(guess, "nope.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Dobrze!,", guess, "jest w tym slowie!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Juz odgadles ta litere", guess)
            elif guess != word:
                print(guess, "nie jest slowem.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("nope.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Gratuluje! zgadles slowo!")
    else:
        print("Sorry, ale nie zgadles, looser. slowem bylo... " + word + ". Moze nastepnym razem!")


def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
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
    return stages[tries]
    #Udaje ze ten komentarz cokolwiek zmienia bo musze cos dodac do zadania zeby miec co wpisac w sprawozdaniu
