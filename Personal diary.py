import random
import shutil
import os
import time

def wait(wait = 2):
    time.sleep(wait)

def clear_screen():
    os.system("cls")

def get_width():
    return shutil.get_terminal_size().columns

def line():
    print("=" * get_width())
    
def generate_number():
    return random.randint(1, 10)

def tablo(attempts):
    line()
    print("Guess the number from 1 to 10!".center(get_width()))
    line()
    print(f"Attempts: {attempts}".center(get_width()))
    line()

def game(number, attempts):
    tablo(attempts)
    guess = int(input("Enter number: ".center(get_width()).rstrip() + " "))

    while attempts != 0:
        if guess == number:
            print(f"You win! The answer was {number}".center(get_width()))
            line()
            wait(5)
            break
        else:
            attempts -= 1
            print(f"Wrong! You have only {attempts} attempts left".center(get_width()))
            wait()
            if guess > number:
                print(f"Your guess - {guess} is bigger than the right answer".center(get_width()))
            else:
                print(f"Your guess - {guess} is smaller than the right answer".center(get_width()))

            wait()
            clear_screen()
            tablo(attempts)
            guess = int(input("Enter number again: ".center(get_width()).rstrip() + " "))

game(generate_number(), 5)
