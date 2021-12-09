from helpers.fileLoader import *


def p1():
    fileData = readFile("q4")
    winningNumbers = fileData[0].split(',')
    winningSets = []
    fileData = fileData[2:]
    bingoBoards = [fl.split(' ') for fl in fileData if len(fl) > 0]
    for board in bingoBoards:
        setData = list(filter(None, board[0:]))

