from helpers.fileLoader import *

def p1():
    splitData = readFile("q5")
    diag = [[0] * 1000 for i in range(1000)]
    counter = 0

    for line in splitData:
        data = line.split(' ')
        num1Split = data[0].split(',')
        # converting to ints from string
        num1Split[0] = int(num1Split[0])
        num1Split[1] = int(num1Split[1])
        num2Split = data[2].split(',')
        num2Split[0] = int(num2Split[0])
        num2Split[1] = int(num2Split[1])

        if num1Split[0] == num2Split[0]:
            yMin = min(num1Split[1], num2Split[1])
            yMax = max(num1Split[1], num2Split[1])
            for i in range(yMin, yMax + 1):
                diag[num1Split[0]][i] += 1

        elif num1Split[1] == num2Split[1]:
            xMin = min(num1Split[0], num2Split[0])
            xMax = max(num1Split[0], num2Split[0])
            for i in range(xMin, xMax + 1):
                diag[i][num1Split[1]] += 1

    for row in diag:
        for item in row:
            if item >= 2:
                counter += 1

    print(counter)