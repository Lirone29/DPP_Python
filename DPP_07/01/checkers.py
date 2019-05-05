
import numpy as matrix

def check(chessBoardTmp, playerID):
    chessBoard = matrix.array(chessBoardTmp)
    x = None
    y = None
    answer = verifyCheckers(chessBoardTmp, playerID)

    n = chessBoard.shape[0]
    if answer == False:
         return None

    coordinatesChecker = []

    if playerID == 1:
        opponentID = 2
    else:
        opponentID = 1

    for i, line in enumerate(chessBoard):
        for j, player in enumerate(line):
            if (player == playerID):
                if(i-1>0 and j+1 < n  and chessBoard[i-1][j+1] == opponentID):
                    if(i-2 > 0 and j+2 < n and chessBoard[i-2][j+2] == 0):
                        coordinatesChecker.append((i, j))
                elif (i-1 >0 and j-1 > 0 and chessBoard[i-1][j-1] == opponentID):
                    if (i - 2 > 0 and j - 2 > 0 and chessBoard[i - 2][j - 2] == 0):
                        coordinatesChecker.append((i, j))
                elif (i+1 < n and j -1 > 0 and chessBoard[i+1][j-1] == opponentID):
                    if (i + 2 < n and j - 2 > 0 and chessBoard[i + 2][j - 2] == 0):
                        coordinatesChecker.append((i, j))
                elif (i+1 < n and j +1 < n and chessBoard[i+1][j+1] == opponentID):
                    if (i + 2 < n  and j + 2<n and chessBoard[i + 2][j + 2] == 0):
                        coordinatesChecker.append((i, j))

    return coordinatesChecker

def verifyCheckers(chessBoardVerify, playerID):
    board = matrix.array(chessBoardVerify)
    #print(board)
    #chcek size of board


    if board.shape[0] !=8 or board.shape[0] != 8:
       return False

    #check if valuse of board are ok
    values = {0, 1, 2}
    for i, line in enumerate(chessBoardVerify):
        for j, value in enumerate(line):
            if value not in values:
                return False

    #chcek if player valuse are available
    counter = 0
    for i, line in enumerate(chessBoardVerify):
        for j, value in enumerate(line):
            if value is playerID:
                counter += 1
    if counter == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    checkersSample = [[1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 2, 0, 2, 0, 0],
                      [0, 0, 2, 0, 0, 0, 0, 0]]

    playerIDSample = 1
    endResult = check(checkersSample, playerIDSample)
    #for i in enumerate(endResult):
    print(endResult)