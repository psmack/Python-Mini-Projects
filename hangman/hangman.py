import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def update_word_completion(user_guess, word, word_completion):
    index = 0
    update_letter = []
    word_as_list = list(word_completion)

    for letter in word:
        if user_guess == letter:
            update_letter.append(index)
        index += 1

    for i in update_letter:
        word_as_list[i] = user_guess

    word_completion = "".join(word_as_list)

    return word_completion

def play_game(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    user_attempt = 6
    winner = False

    print("Let's play Hangman!")

    while user_attempt > 0:
        print(f"Attempt: {user_attempt}")
        print(word_completion)
        user_guess = input("Please enter a letter: ").upper()

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f"You have already guessed {user_guess}.")
            elif user_guess in word:
                print(f"Good guess!")
                guessed_letters.append(user_guess)
                word_completion = update_word_completion(user_guess, word, word_completion)
                if "_" not in word_completion:
                    winner = True
                    break
            else:
                print(f'{user_guess} is not in the word.')
                user_attempt -= 1
        else:
            print("Not a valid guess!")

    if winner is True:
        print(f"Congrats! The word was {word}.")
    else:
        print(f"Better luck next time! The word was {word}")

def main():
    word = get_word()
    print("Game Word:", word)
    play_game(word)

if __name__ == "__main__":
    main()