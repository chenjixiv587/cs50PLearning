import random
import sys


def main():
    n = get_num("Level: ")
    to_guess = random.randint(1, n)
    guess(to_guess)


def guess(num):
    while True:
        guess_num = get_num("Guess: ")
        if guess_num > num:
            print("Too large!")
        elif guess_num < num:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit()


def get_num(kind):
    while True:
        s_level = input(kind)
        try:
            i_level = int(s_level)
        except ValueError:
            pass
        else:
            if i_level <= 0:
                continue
            return i_level


if __name__ == "__main__":
    main()
