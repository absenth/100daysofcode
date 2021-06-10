# bandname.py generator

import os
from adverbs import pickAdverb
from verbs import pickVerb


def main():
    """ Main Function """
    again = False
    while not again:
        name = generate_bandname()
        os.system('clear')
        print(f"Your Band Name will be: {name}")
        answer = input("Keep Band Name (y/n): ")
        if answer.lower().strip() == "y":
            print(f"Congrats {name}!")
            return True


def generate_bandname():
    """ construct a random band name from an adverb and verb """
    prefix = str(pickAdverb().upper())
    suffix = str(pickVerb().upper())
    band_name = (f"{prefix} {suffix}")
    return band_name


if __name__ == "__main__":
    main()
