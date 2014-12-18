"""
PrintScreen program to capture the screen to a graphics file in a
folder when the PrintScreen button is pressed.
"""
__author__ = 'dalem'

import os

if os.name == "nt":
    print("Yea Windows, I run here.")
else:
    print("Bummer; I don't run here " + os.name + "!")
    exit()

import withWIN32


if __name__ == "__main__":
    withWIN32.main()
    #main()

