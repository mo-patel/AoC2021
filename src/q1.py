from helpers.fileLoader import *


def p1():
    fileData = read_fileInt("q1")
    prevNum = None
    increaseCount = 0
    for num in fileData:
        if prevNum is None:
            prevNum = num
        else:
            if num > prevNum:
                increaseCount += 1
            prevNum = num
    print(increaseCount)


def calculateNums(data, currentPos):
    if currentPos + 2 > len(data):
        return False
    return sum(data[currentPos:currentPos + 3])


def p2():
    fileData = read_fileInt("q1")
    prevNum = None
    increase = 0
    for idx, num in enumerate(fileData):
        total = calculateNums(fileData, idx)
        if total is False:
            print(increase)
            return
        else:
            if prevNum is None:
                prevNum = total
            else:
                if total > prevNum:
                    increase += 1
                prevNum = total
