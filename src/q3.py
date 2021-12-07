from collections import Counter

from helpers.fileLoader import *


def p1():
    fileData = readFile("q3")

    binaryVals = {idx: {0: 0, 1: 0} for idx, val in enumerate([int(num) for num in fileData[0]])}
    for byte in fileData:
        splitNum = [int(num) for num in byte]
        for idx, bit in enumerate(splitNum):
            if bit == 1:
                binaryVals[idx][1] += 1
            else:
                binaryVals[idx][0] += 1

    finalBinaryMax = [max(val, key=val.get) for idx, val in binaryVals.items()]
    finalBinaryMax = int(''.join(str(val) for val in finalBinaryMax), 2)
    finalBinaryMin = [min(val, key=val.get) for idx, val in binaryVals.items()]
    finalBinaryMin = int(''.join(str(val) for val in finalBinaryMin), 2)
    print(finalBinaryMax * finalBinaryMin)


def createDigitList(idx, listData):
    tempList = []
    for item in listData:
        tempList.append(int(str(item[idx])))
    return tempList


def scanData(fileData, searchType):
    idx = 0
    while len(fileData) > 1:
        digitList = createDigitList(idx, fileData)
        data = Counter(digitList)
        common = data.most_common(2)
        commonOverride = None

        if common[0][1] == common[-1][1]:
            commonOverride = 1 if searchType == "most" else 0

        if commonOverride is not None:
            fileData = [num for num in fileData if int(str(num[idx])) == commonOverride]
        else:
            fileData = [num for num in fileData if int(str(num[idx])) == (common[0][0] if searchType == "most" else common[-1][0])]
        idx += 1
    return fileData[0]


def p2():
    fileData = readFile("q3")
    oxygenRate = scanData(fileData, "most")
    scrubberRate = scanData(fileData, "least")
    print(int(''.join(str(oxygenRate)), 2) * int(''.join(str(scrubberRate)), 2))
