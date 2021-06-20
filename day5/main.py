# 100 Days Of Code - Day 5 - PyPassword Generator

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
           "C", "D", "E", "F", "G", "H", "J", "K", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
elements = ["letter", "number", "symbol"]
generated_pw = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))


pw_length = nr_letters + nr_symbols + nr_numbers

while pw_length > 0:
    element_type = random.choice(elements)
    if element_type == "letter":
        if nr_letters > 0:
            pw_part = random.choice(letters)
            generated_pw = generated_pw + pw_part
            nr_letters -= 1
            pw_length -= 1
    elif element_type == "symbol":
        if nr_symbols > 0:
            pw_part = random.choice(symbols)
            generated_pw = generated_pw + pw_part
            nr_symbols -= 1
            pw_length -= 1
    else:
        if nr_numbers > 0:
            pw_part = random.choice(numbers)
            generated_pw = generated_pw + pw_part
            nr_numbers -= 1
            pw_length -= 1

if pw_length == 0:
    print(generated_pw)
