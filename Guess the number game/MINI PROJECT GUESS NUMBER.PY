import random


number_to_guess = random.randint(1, 100)


count_tries = 0


def keep_trying(message):
    while True:
        try:
            number = int(input(message))
            if 1 <= number <= 100:
                break
            else:
                print("Input a number between 1 and 100")
        except ValueError:
            print("TRY AGAIN, DON'T USE LETTERS!")
    return number


print("START THE GAME!")


while True:
    number = keep_trying("Enter a number between 1 and 100: ")
    count_tries += 1
    if number > number_to_guess:
        print(f"The random number is lower than {number}")
    elif number < number_to_guess:
        print(f"The random number is higher than {number}")
    else: 
        print("YOU WON!")
        break

print(f"You tried {count_tries} times!")