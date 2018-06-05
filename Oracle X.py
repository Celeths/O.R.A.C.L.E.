"""Operational Revelator And Change Likeliness Estimator 2.0
            Made by Leveles"""

import re
import importlib
import sys
import random
from random import randint
import magic_conch_shell
import vocab

exit = 0

while exit == 0:
    response = input("What do you want to know?\n")
    response = str(response).lower()
    starter = re.sub("[^\w]", " ",  response).split()
    if response == "end":
        exit = 1
    else:
        magic_conch_shell.teller(starter)
        print(magic_conch_shell.answer)
        if magic_conch_shell.error == "record":
            manager = open("Error log", "a")
            manager.write(response + "\n")
            manager.close()