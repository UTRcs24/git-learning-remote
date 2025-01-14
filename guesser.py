import random

def get_answer(guess):
    answer = "q"
    while answer != "y" and answer != "n":
        answer = input("\nIs your age " + str(guess) + "? y/n ").lower()
    if answer == "y":
        return True
    return False

print("#####################################")
print("Hello. I'm going to guess your age!")
print("#####################################\n")
name = input("What is your name? ")
guessed_correct = False
guesses = []
while not guessed_correct:
    guess = random.randrange(15, 30)
    if guess not in guesses:
        guesses.append(guess)
        if get_answer(guess):
            print("\n" + name + " is " + str(guess) + " years old.\n")
            guessed_correct = True
        else:
            print("Rats.")
print("\n#####################################")
print("Goodbye.")
print("#####################################")


