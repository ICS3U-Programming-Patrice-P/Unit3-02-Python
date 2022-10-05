#!/usr/bin/env python3
# Created by : Patrice Pat-Odita
# Created on : Oct 5, 2022
# This program asks the user to guess my favorite
# number and if they get it wrong they are told so.
from builtins import int, print
from numbers import Integral
import constants


def main():
    # Get number from user
    number_guessed = int(input("Guess my favorite number from 0-9: "))
    print("")

    # Check to see if they got the right number or wrong
    if number_guessed == constants.FAVORITE_NUMBER:
        print("YOU GOT IT RIGHT!")
    else:
        print(
            "You got it wrong, my favorite number is {} ".format(
                constants.FAVORITE_NUMBER
            )
        )


if __name__ == "__main__":
    main()
