from helpers.fileLoader import *


class Q5:
    splitData = readFile("q5")

    def run(self, diag, p2=False):
        for line in self.splitData:
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

            elif p2 == True:
                xMax = max(num1Split[0], num2Split[0])
                xMin = min(num1Split[0], num2Split[0])
                yMax = max(num1Split[1], num2Split[1])
                yMin = min(num1Split[1], num2Split[1])
                yTrackerMin = yMin
                yTrackerMax = yMax
                xTrackerMin = xMin
                if num1Split[0] > num2Split[0] and num1Split[1] > num2Split[1]:
                    for x in range(xMin, xMax + 1):
                        for y in range(yTrackerMin, yMax + 1):
                            yTrackerMin += 1
                            diag[x][y] += 1
                            break
                elif num1Split[0] < num2Split[0] and num1Split[1] < num2Split[1]:
                    for x in range(xTrackerMin, xMax + 1):
                        for y in range(yTrackerMin, yMax + 1):
                            yTrackerMin += 1
                            xTrackerMin += 1
                            diag[x][y] += 1
                            break
                else:
                    for x in range(xMin, xMax + 1):
                        for y in range(yTrackerMax, yMin - 1, -1):
                            yTrackerMax -= 1
                            diag[x][y] += 1
                            break

    def p1(self):
        counter = 0
        diag = [[0] * 1000 for i in range(1000)]
        self.run(diag)
        for row in diag:
            for item in row:
                if item >= 2:
                    counter += 1

        return counter

    def p2(self):
        counter = 0
        diag = [[0] * 1000 for i in range(1000)]
        self.run(diag, True)
        for row in diag:
            for item in row:
                if item >= 2:
                    counter += 1

        return counter
