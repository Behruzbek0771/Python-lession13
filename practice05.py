import random

def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri!")
    else:
        print("Xato, yana urinib ko'ring.")

def main():
    secret_number = random.randint(1, 10)  # 1 dan 10 gacha sirli son
    guess = int(input("1 dan 10 gacha son kiriting: "))

    result = check_guess(secret_number, guess)
    print_result(result)
main()