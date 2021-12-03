import os
from os.path import dirname

filesDir = os.path.abspath(__file__ + "/../..") + "/inputs/"

def read_fileInt(question):
    data = []
    for ln in readFile(question):
        data.append(int(ln))
    return data

def readFile(question):
    with open(filesDir + question + ".txt", "r") as file:
        lines = [line.replace('\n', '') for line in file.readlines()]
    return lines