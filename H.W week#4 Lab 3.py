def guessing_game():
    secret_word = "Balloon"
    guess = ""
    while guess != secret_word:
        guess = input("Guess the secret word: ")

        if guess != secret_word:
            print("Wrong guess! Try again. ")
            continue

    print("Great you got it right.")
