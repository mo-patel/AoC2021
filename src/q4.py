from helpers.fileLoader import *


def p1():
    print(run())

def p2():
    run(True)

def calculateNumbers(numberList, winningNum, p2 = False):
    unmarkedNums = [int(num) for num in sum(numberList, []) if num != 'X']  # flatten 1 lvl
    return sum(unmarkedNums) * int(winningNum)


def run(p2 = False):
    fileData = readFile("q4")
    winningNumbers = fileData[0].split(',')
    fileData = fileData[2:]
    bingoBoards = [fl.split(' ') for fl in fileData if len(fl) > 0]  # split by space and remove []
    bingoBoards = [list(filter(None, board[0:])) for board in bingoBoards]  # remove any '' in between
    lastWin = None
    lastWinNum = None
    winningSets = set()
    for num in winningNumbers:
        checkIdx = 0
        for idx, boardLine in enumerate(bingoBoards):

            if idx > 0 and idx % 5 == 0:
                checkIdx = idx
            if num in boardLine:
                bingoBoards[idx][boardLine.index(num)] = 'X'
        for ix, line in enumerate(bingoBoards):
            if len(set(line)) == 1 and line[0] == 'X':
                numsToSend = [bingoBoards[i] for i in range(checkIdx, checkIdx + 5)]

                if not p2:
                    return calculateNumbers(numsToSend, num)
                else:
                    if any((num, numsToSend) in item for item in winningSets):
                        break
                    else:
                        lastWinNum = num
                        lastWin = calculateNumbers(numsToSend, num)
                        winningSets.add((lastWinNum, lastWin))


            for x in range(0, 5):
                boardItems = []
                for i in range(checkIdx, checkIdx + 5):
                    boardItems.append(bingoBoards[i][x])
                    if len(boardItems) == 5:
                        if len(set(boardItems)) == 1 and boardItems[0] == 'X':
                            numsToSend = [bingoBoards[i] for i in range(checkIdx, checkIdx + 5)]

                            if not p2:
                                return calculateNumbers(numsToSend, num)
                            else:
                                if any((num, numsToSend) in item for item in winningSets):
                                    break
                                else:
                                    lastWinNum = num
                                    lastWin = calculateNumbers(numsToSend, num)
                                    winningSets.add((lastWinNum, lastWin))
                                    print(lastWin, lastWinNum)
    # print('Last Win')
    # print(lastWin, lastWinNum)