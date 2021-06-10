# verbs.py
import random

verblist = [
    "Accept", "Achieve", "Add", "Admire",
    "Admit", "Adopt", "Advise", "Agree",
    "Allow", "Announce", "Appreciate", "Approve",
    "Argue", "Arrive", "Ask", "Assist",
    "Attack", "Bake", "Bathe", "Be",
    "Beat", "Become", "Beg", "Behave",
    "Bet", "Boast", "Boil", "Borrow",
    "Breathe", "Bring", "Build", "Burn",
    "Bury", "Buy", "Call", "Catch",
    "Challenge", "Change", "Cheat", "Chew",
    "Choose", "Clap", "Clean", "Collect",
    "Compare", "Complain", "Confess", "Confuse",
    "Construct", "Control", "Copy", "Count",
    "Create", "Cry", "Damage", "Dance",
    "Deliver", "Destroy", "Disagree", "Drag",
    "Drive", "Drop", "Earn", "Eat",
    "Employ", "Encourage", "Enjoy", "Establish",
    "Estimate", "Exercise", "Expand", "Explain",
    "Fear", "Feel", "Fight", "Find",
    "Fly", "Forget", "Forgive", "Fry",
    "Gather", "Get", "Give", "Glow",
    "Greet", "Grow", "Guess", "Harass",
    "Hate", "Hear", "Help", "Hit",
    "Hope", "Identify", "Interrupt", "Introduce",
    "Irritate", "Jump", "Keep", "Kick",
    "Kiss", "Laugh", "Learn", "Leave",
    "Lend", "Lie", "Like", "Listen",
    "Lose", "Love", "Make", "Marry",
    "Measure", "Meet", "Move", "Murder",
    "Obey", "Offend", "Offer", "Open",
    "Paint", "Pay", "Pick", "Play",
    "Pray", "Print", "Pull", "Punch",
    "Punish", "Purchase", "Push", "Quit",
    "Race", "Read", "Relax", "Remember",
    "Reply", "Retire", "Rub", "See",
    "Select", "Sell", "Send", "Sing",
    "Snore", "Stand", "Stare", "Start",
    "Stink", "Study", "Sweep", "Swim",
    "Take", "Talk", "Teach", "Tear",
    "Tell", "Thank", "Travel", "Type",
    "Understand", "Use", "Visit", "Wait",
    "Walk", "Want", "Warn", "Wed",
    "Weep", "Wink", "Worry", "Write",
    "Yell"
    ]


def pick_verb():
    """ randomly select a verb """
    return random.choice(verblist)
