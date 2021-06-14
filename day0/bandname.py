# bandname.py generator

import os
from adverbs import pick_adverb
from verbs import pick_verb


def main():
    """ Main Function """
    again = False
    while not again:
        name = generate_band_name()
        os.system('cls')
        print(f"Your Band Name will be: {name}")
        answer = input("Keep Band Name (y/n): ")
        if answer.lower().strip() == "y":
            print(f"Congrats {name}!")
            return True


def generate_band_name():
    """ construct a random band name from an adverb and verb """
    prefix = pick_adverb().upper()
    suffix = pick_verb().upper()
    band_name = f"{prefix} {suffix}"
    return band_name


if __name__ == "__main__":
    main()
