import random

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "csharp", "console", "consoleOS", "hangman", "text", "game", "windows", "executable", "pytorch", "tensorflow"] #words list
    random_number = random.randint(0, 4)
    chosen_word = word_list[random_number]
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")
    print("_ " * len(chosen_word))

    while attempts > 0:
        guess = input("\nPlease guess a letter: ").lower()
        if len(guess) != 1:
            print("You need to guess a single letter.")
        elif guess in guessed_letters:
            print("You've already guessed this letter.")
        elif guess not in chosen_word:
            print("This letter is not in the word.")
            attempts -= 1
        else:
            print("Good job! This letter is in the word.")
            guessed_letters.append(guess)
        word_completion = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                word_completion += letter + " "
            else:
                word_completion += "_ "
        print(word_completion)
        if "_" not in word_completion:
            print("Congratulations, you won!")
            return
        print(f"You have {attempts} attempts remaining.")
    print("Sorry, you lost. The word was " + chosen_word + ".")

