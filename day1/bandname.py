#bandname.py generator

import os
from adverbs import pickAdverb
from verbs import pickVerb


def main():
    """ Main Function """
    name = generate_bandname()
    os.system('clear')
    print(f"Your Band Name will be: {name}")
    print("")


def generate_bandname():
    """ construct a random band name from an adverb and verb """
    prefix = str(pickAdverb().upper())
    suffix = str(pickVerb().upper())
    band_name = (f"{prefix} {suffix}")
    return band_name


if __name__ == "__main__":
    main()
