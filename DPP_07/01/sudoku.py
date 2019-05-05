import numpy as matrix


def sudoku(table, nrColumn, nrRow):

    sudokuTable = matrix.array(table)
    finaleSum = 0
    check = checkTable(table, nrColumn, nrRow)
    sum = 0
    numbers = []
    if (check == False):
        print("Not a sudoku table")
        return None

    for i in range(sudokuTable.shape[0]):
        finaleSum += sudokuTable[0][i]


    # ilosc kafelków oraz ilosć liczb w kafelku
    n = nrColumn * nrRow

    # check vertically
    for i in range(sudokuTable.shape[0]):
        sum = 0
        numbers.clear()
        for j in range(sudokuTable.shape[1]):
            sum += sudokuTable[i][j]
            numbers.append(sudokuTable[i][j])
            if j == sudokuTable.shape[1]:
                if(check_duplicates(numbers, n) == False):
                    return False
                elif sum != finaleSum:
                    return False

    # check horizontally
    for i in range(sudokuTable.shape[1]):
        sum = 0
        numbers.clear()
        for j in range(sudokuTable.shape[0]):
            sum += sudokuTable[j][i]
            numbers.append(sudokuTable[j][i])
            if j == sudokuTable.shape[0]:
                if (check_duplicates(numbers, n) == False):
                    return False
                elif sum != finaleSum:
                    return False

    # check title
    for x in range(0, sudokuTable.shape[0],nrColumn):
        for y in range(0, sudokuTable.shape[1],nrRow):
            sum = 0
            numbers.clear()
            for i in range(columnNumber):
                for j in range(rowNumber):
                    sum += sudokuTable[x + i][y + j]
                    numbers.append(sudokuTable[x +i][y +j])
                if i == columnNumber-1:
                    if not check_duplicates(numbers, n):
                        return False
                    elif sum != finaleSum:
                        return False

    return True


def check_duplicates( matrixTmp, n):
    # check if there are duplicates
    numbers = set()
    for number in matrixTmp:
        numbers.add(number)

    OK_numbers = set(range(1, n+1))

    if numbers == OK_numbers:
        return True
    else:
        return False

def checkTable(table, nrColumn, nrRow):
    size = nrColumn * nrRow
    sudokuTable = matrix.array(table)
    answer = False
    x = sudokuTable.shape[0]
    y = sudokuTable.shape[1]
    if (x == size and y == size):
        answer = True
    else:
        answer = False

    return answer


if __name__ == '__main__':
    rowNumber = 3
    columnNumber = 3

    table = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 3, 1, 5, 6, 4, 8, 9, 7],
             [5, 6, 4, 8, 9, 7, 2, 3, 1],
             [8, 9, 7, 2, 3, 1, 5, 6, 4],
             [3, 1, 2, 6, 4, 5, 9, 7, 8],
             [6, 4, 5, 9, 7, 8, 3, 1, 2],
             [9, 7, 8, 3, 1, 2, 6, 4, 5]]

    answer = sudoku(table, columnNumber, rowNumber)
    print(answer)