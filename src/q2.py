from helpers.fileLoader import *


def p1():
    fileData = readFile("q2")
    horizontal = depth = 0
    for line in fileData:
        lineData = line.split()
        numVal = int(lineData[1])
        match lineData[0]:
            case 'forward':
                horizontal += numVal
            case 'down':
                depth += numVal
            case 'up':
                depth -= numVal
    print(horizontal * depth)

def p2():
    fileData = readFile("q2")
    horizontal = depth = aim = 0
    for line in fileData:
        lineData = line.split()
        numVal = int(lineData[1])
        match lineData[0]:
            case 'forward':
                horizontal += numVal
                depth += aim * numVal
            case 'down':
                aim += numVal
            case 'up':
                aim -= numVal
    print(horizontal * depth)