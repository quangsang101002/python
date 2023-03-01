import string
import random


print(string.ascii_letters)


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def password_generator(length=8):
    printtable = f'{LETTERS}, {NUMBERS}, {PUNCTUATION}'
    printtable = list(printtable)
    random.shuffle(printtable)
    
    random_password = random.choices(printtable, k=length)
    random_password = "".join(random_password)
    return random_password

def input_password():
    print_password = input("How long do you want your password to be? ")
    return int(print_password)

def main():
    passlength = input_password()
    passlength = password_generator(passlength)
    print(passlength)

if __name__ == "__main__":
    main()
