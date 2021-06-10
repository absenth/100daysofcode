# adverbs.py
import random

adverblist = [
    "accidentally", "always", "angrily", "anxiously",
    "awkwardly", "badly", "blindly", "boastfully",
    "boldly", "bravely", "brightly", "cheerfully",
    "coyly", "crazily", "defiantly", "deftly",
    "deliberately", "devotedly", "doubtfully", "dramatically",
    "dutifully", "eagerly", "elegantly", "enormously",
    "evenly", "eventually", "exactly", "faithfully",
    "finally", "foolishly", "fortunately", "frequently",
    "gleefully", "gracefully", "happily", "hastily",
    "honestly", "hopelessly", "hourly", "hungrily",
    "innocently", "inquisitively", "irritably", "jealously",
    "justly", "kindly", "lazily", "loosely",
    "madly", "merrily", "mortally", "mysteriously",
    "nervously", "never", "obediently", "obnoxiously",
    "occasionally", "often", "only", "perfectly",
    "politely", "poorly", "powerfully", "promptly",
    "quickly", "rapidly", "rarely", "regularly",
    "rudely", "safely", "seldom", "selfishly",
    "seriously", "shakily", "sharply", "silently",
    "slowly", "solemnly", "sometimes", "speedily",
    "sternly", "technically", "tediously", "unexpectedly",
    "usually", "victoriously", "vivaciously", "warmly",
    "wearily", "weekly", "wildly", "yearly"
    ]


def pickAdverb():
    """ randomly select an adverb """
    return random.choice(adverblist)
