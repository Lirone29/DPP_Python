import numpy as matrix

def spirall(table):
    spitallTable = matrix.array(table)
    height = spitallTable.shape[0]
    width = spitallTable.shape[1]

    endSpirall = []

    for i in range(height):
        endSpirall.append([])
        for j in range(width):
            endSpirall[i].append(0)

    spirallX = 0
    spirallY = 0
    stepX = 1
    stepY = 0
    minValueX = 0
    minValueY = 0
    maxValueX = height
    maxValueY = width

    for i in range(0, width):
        for j in range(0, height):
            endSpirall[spirallX][spirallY] = spitallTable[i][j]
            spirallX += stepX
            spirallY += stepY
            if (spirallX == maxValueX):
                stepX = 0
                stepY = 1
                spirallX +=-1
                spirallY +=1
                minValueY +=1
            if(spirallY == maxValueY):
                stepX = -1
                stepY = 0
                spirallX -= 1
                spirallY -= 1
                maxValueX += -1
            if (spirallX < minValueX):
                stepX = 0
                stepY = -1
                spirallY += -1
                spirallX += 1
                maxValueY += -1
            if(spirallY < minValueY):
                spirallX += 1
                spirallY +=1
                stepX = 1
                stepY = 0
                minValueX += 1


    for i in range(height):
        for j in range(width):
            value = endSpirall[i][j]
            print("{}".format(value).rjust(5), end='')
        print("")

    #print(list)

if __name__ == '__main__':

    table = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

    table2 = [[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14],
              [15,16, 17, 18, 19, 20, 21],
              [22, 23, 24, 25, 26, 27, 28],
              [29, 30, 31, 32, 33, 34, 35],
              [36, 37, 38, 39, 40, 41, 42],
              [43, 44, 45, 46, 47, 48, 49]]
    spirall(table2)
