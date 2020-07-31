secret_number = 42
guess = 0

print("what is the secret number? ")

while guess != secret_number:
    guess = eval(input("  "))
    if guess < secret_number:
        print("That is way too low. Please try again. ")
    elif guess > secret_number:
        print("That is way too high. Please try again.")

print("Congratulations, you have guessed the secret number!")
