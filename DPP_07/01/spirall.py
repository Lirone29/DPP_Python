import numpy as matrix

def print_spiral(table):
    tableSpirall = translate(table)
    for i, line in enumerate(tableSpirall):
        for j, value in enumerate(line):
            print("{}".format(value).rjust(7), end='')
        print("")


def translate(table):
    tableSpirall = matrix.array(table)
    spirall = []
    for i, line in enumerate(tableSpirall):
        spirall.append([])
        for j in enumerate(line):
            spirall[i].append(0)

    x_min = 0
    x_max = tableSpirall.shape[1]
    y_min = 0
    y_max = tableSpirall.shape[0]
    valueX = 0
    valueY = 0
    step_x = 1
    step_y = 0

    for i, line in enumerate(tableSpirall):
        for j, value in enumerate(line):
            spirall[valueY][valueX] = value
            valueX += step_x
            valueY += step_y
            if valueX == x_max:
                valueX -= 1
                valueY += 1
                step_x = 0
                step_y = 1
                y_min += 1
            if valueY == y_max:
                valueY -= 1
                valueX -= 1
                step_x = -1
                step_y = 0
                x_max -= 1
            if valueX < 0:
                valueX += 1
                valueY -= 1
                step_x = 0
                step_y = -1
                y_max -= 1
            if valueY < y_min:
                valueY += 1
                valueX += 1
                step_x = 1
                step_y = 0
                x_min += 1
    return spirall

if __name__ == '__main__':
    matrix1 = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    matrix2 = [[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19, 20, 21],
              [22, 23, 24, 25, 26, 27, 28],
              [29, 30, 31, 32, 33, 34, 35],
              [36, 37, 38, 39, 40, 41, 42],
              [43, 44, 45, 46, 47, 48, 49]]
    print_spiral(matrix2)
