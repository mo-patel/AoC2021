import os
from os.path import dirname

filesDir = os.path.abspath(__file__ + "/../..") + "/inputs/"


def readFile(question):
    with open(filesDir + question + ".txt", "r") as file:
        lines = file.readlines()
    return lines