#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program simulates a grandma that wants to know if you deserve to date
# her grandchild


def main():
    print("For you to date my grandchild I have to"
          " ask you a couple of questions.")

    input1 = input("Are you rich? (respond with an yes or no):")
    input2 = input("Are you really good looking? (respond with an yes or no):")

    if input1 == "yes":
        rich = True
    elif input1 == "no":
        rich = False

    if input2 == "yes":
        good_looking = True
    elif input2 == "no":
        good_looking = False

    try:
        rich is True or rich is False
        good_looking is True or good_looking is False
        if rich is True or good_looking is True:
            print("\nYou can date my grandchild!")
        else:
            print("\nYou are not good enough to date my grandchild!")
    except Exception:
        print("\nThis input is invalid, please, insert 'yes' or 'no'.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
