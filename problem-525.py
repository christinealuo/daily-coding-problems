def problem_525(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])

    topRow = 0
    bottomRow = numRows - 1
    rightColumn = 0
    leftColumn = numCols - 1

    goingDownRow = True
    goingDownColumn = False

    onRow = True
    onColumn = False

    currentRow = 0
    currentColumn = 0

    counter = numRows * numCols

    while counter > 0:
        if onRow and goingDownRow:
            for i in range(rightColumn, leftColumn + 1):
                print(matrix[currentRow][i])
                counter -= 1
            onRow = False
            onColumn = True
            goingDownColumn = True
            topRow += 1
            currentColumn = leftColumn
        elif onColumn and goingDownColumn:
            for i in range(topRow, bottomRow + 1):
                print(matrix[i][leftColumn])
                counter -= 1
            onRow = True
            onColumn = False
            goingDownRow = False
            leftColumn -= 1
            currentRow = bottomRow
        elif onRow and not goingDownRow:
            for i in reversed(range(rightColumn, leftColumn + 1)):
                print(matrix[currentRow][i])
                counter -= 1
            onRow = False
            onColumn = True
            goingDownColumn = False
            bottomRow -= 1
            currentColumn = rightColumn
        elif onColumn and not goingDownColumn:
            for i in reversed(range(topRow, bottomRow + 1)):
                print(matrix[i][currentColumn])
                counter -= 1
            onRow = True
            onColumn = False
            goingDownRow = True
            rightColumn += 1
            currentRow = topRow

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
problem_525(matrix)