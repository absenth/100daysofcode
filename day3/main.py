# 100DaysOfCode - Day 3 Choose Your Own Adventure


def main():
    """ Riviting function description here """
    print("Welcome to Day 3 of 100DaysOfCode")
    print("")
    print("You come to a fork in the road.")
    print("Do you choose the Left or Right path?")
    if not left_or_right():
        print("You have been eaten by a Grue!")
        dead()
        exit()

    print("You arrive at a river.  Swim or Wait for a boat?")
    if not sink_or_swim():
        print("A rogue river Grue spots you swimming.")
        print("You do your best to swim faster trying to escape.")
        print("You have been eaten bya a Grue!")
        dead()
        exit()

    print("You arrive at a castle with three doors.")
    print("You must choose.  Red, Blue, or Yellow.")
    if not red_blue_or_yellow():
        print("You come face to face with a large Grue!")
        dead()
        exit()

    print("You enter the Yellow door.")
    print("Inside is a cheeseburger.")
    print("You Win!")


def dead():
    """ Function for when you fail! """
    print("You are dead! Rigor Mortis Habeas Corpus")


def left_or_right():
    """ Function for First Option """
    l_or_r = input("L or R? ")
    if l_or_r.lower().strip() == "l":
        return True
    else:
        return False


def sink_or_swim():
    """ Do we swim or wait for the boat """
    wait_or_swim = input("Wait or Swim? ")
    if wait_or_swim.lower().strip() == "w":
        return True
    else:
        return False


def red_blue_or_yellow():
    """ Pick a door, any door """
    pick_a_door = input("Red, Blue or Yellow? ")
    if pick_a_door.lower().strip() == "y":
        return True
    elif pick_a_door.lower().strip() == "b":
        return False
    else:
        return False

if __name__ == "__main__":
    main()

