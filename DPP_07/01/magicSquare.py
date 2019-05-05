import numpy as matrix

def checkMagicSquare(squareTmp):
    global sum
    magicSquare = matrix.array(squareTmp)

    #check dimension
    if(magicSquare.shape[0] <3):
        return False
    elif (magicSquare.shape[1] <3):
        return False

    if (magicSquare.shape[0] != magicSquare.shape[1]):
        return False

    finalSum = sum(magicSquare[0])

    #check Horizontally
    for i in range(0, magicSquare.shape[0]):
        sum = 0
        for j in range(0, magicSquare.shape[0]):
            sum += magicSquare[i][j]
        if(sum!=finalSum):
            return False

    #check Vertically
    for i in range(0, magicSquare.shape[0]):
        sum = 0
        for j in range(0, magicSquare.shape[0]):
            sum += magicSquare[j][i]
        if (sum != finalSum):
            return False

   #check diagonally right to lefr
    sum =0
    for i in range(0, magicSquare.shape[0]):
        for j in range(0, magicSquare.shape[0]):
            if(i == j):
                sum += magicSquare[j][i]
    if (sum != finalSum):
        return False

    # check diagonally left to right
    sum = 0
    for i in range(magicSquare.shape[0]-1,-1,-1):
        for j in range(magicSquare.shape[0]-1,-1,-1):
            if (i == j):
                sum += magicSquare[i][j]
                #print(sum)

    if (sum != finalSum):
        return False
    else:
        return True


if __name__ == '__main__':
    table = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 3, 1, 5, 6, 4, 8, 9, 7],
             [5, 6, 4, 8, 9, 7, 2, 3, 1],
             [8, 9, 7, 2, 3, 1, 5, 6, 4],
             [3, 1, 2, 6, 4, 5, 9, 7, 8],
             [6, 4, 5, 9, 7, 8, 3, 1, 2],
             [9, 7, 8, 3, 1, 2, 6, 4, 5]]
    answer = checkMagicSquare(table)
    print(answer)