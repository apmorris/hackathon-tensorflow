"""
Contains general purpose functions that would clutter up the main source file.
"""


def print_blue(string, string2):
    print "".join(["\033[94m", string, " ", string2, "\033[0m"])


def print_red(string, string2):
    print "".join(["\033[91m", string, " ", string2, "\033[0m"])
