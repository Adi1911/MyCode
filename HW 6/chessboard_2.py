"""
File Name:  chessboard.py
Author:     Aditya Ajit Tirakannavar (at2650@rit.edu)
Course:     CSCI-665 Foundations of Algorithms
HW 6.2:     Implement an O((d1d2)^3) algorithm that decides if it is possible to cover all of the empty squares on the chess board
            by non-overlapping dominos (the dominos cannot cover any of the occupied positions and they cannot “stick out” of
            the chess board).
            the first line contains d1 and d2, separated by a space. Then d1 lines follow.
            The i-th of these lines represents the i-th row of the chess board
            and it contains d2 numbers, each number is either 0 or 1
"""

import math
setA = []
setB = []

def BFS(s, t, parent, graph):
    """
    This BFS function checks if a path exists from source to Target and returns a boolean
    :param s: source
    :param t: target
    :param parent: parent array containing BFS paths
    :param graph: input graph
    :return: True/False
    """
    visited = [0] * len(graph)
    queue = list()
    queue.append(s)
    visited[s] = 1
    res = False

    while queue:
        temp = queue.pop(0)
        for ind, val in enumerate(graph[temp]):
            if not visited[ind] == 1 and not val == 0:
                visited[ind] = 1
                parent[ind] = temp
                queue.append(ind)
                if ind == t:
                    res = True
                    break
    return res

def FordFulkerson(source, sink , graph):
    """
    This function returns the maximum flow from s to t in the given graph
    :param source:
    :param sink:
    :param graph:
    :return: max_flow: maximum flow from s to t
    """

    parent = [0] * len(graph)
    max_flow = 0
    # Augmenting the flow while there exists a path from s to t in the given graph
    while BFS(source, sink, parent, graph):
        path_flow = math.inf
        temp = sink
        flag = True
        # finding the maximum flow through the path found.
        while flag:
            if not path_flow < graph[parent[temp]][temp]:
                path_flow = graph[parent[temp]][temp]
            temp = parent[temp]
            if temp == source:
                flag = False
        # Adding path flow to overall flow (max_flow)
        max_flow = max_flow + path_flow
        v = sink
        flag =True
        # updating residual capacities of the edges and reversing edges
        while flag:
            u = parent[v]
            graph[u][v] = graph[u][v] - path_flow
            graph[v][u] = graph[v][u] + path_flow
            v = parent[v]
            if v == source:
                flag = False
    return max_flow


def createAndColorBoard(row, column):
    """
    This function creates and returns a chessboard which is 2D list
    :param row:
    :param column:
    :return:
    """
    chessBoard = [[0 for i in range(column)] for j in range(row)]
    numberOfWhiteSpaces = 0
    numberOfBlackSpaces = 0

    for chessRow in range(row):
        for chessColumn in range(column):
            if (chessRow + chessColumn) % 2 == 0:
                chessBoard[chessRow][chessColumn] = 'BLACK'
                numberOfBlackSpaces += 1
            else:
                chessBoard[chessRow][chessColumn] = 'WHITE'
                numberOfWhiteSpaces += 1

    # print(chessBoard)
    return chessBoard, numberOfBlackSpaces, numberOfWhiteSpaces


def findOccupiedSpaces(builtArray, row, column, colouredChessBoard):
    """
    This function returns Occupied chessboard positions and their counts
    :param builtArray:
    :param row:
    :param column:
    :param colouredChessBoard:
    :return:
    """
    occupiedIndexesList = []
    for inputRow in range(row):
        for inputColumn in range(column):
            if builtArray[inputRow][inputColumn] == 1:
                occupiedIndexesList.append([inputRow, inputColumn])
    occupiedBlackCount , occupiedWhiteCount = 0,0
    for colorRow in range(row):
        for colorColumn in range(column):
            if [colorRow, colorColumn] in occupiedIndexesList:
                if colouredChessBoard[colorRow][colorColumn] == 'BLACK':
                    occupiedBlackCount += 1
                else:
                    occupiedWhiteCount += 1
    return occupiedIndexesList, occupiedBlackCount,occupiedWhiteCount


def createIndexedChessBoard(numberOfBlackSpaces, numberOfWhiteSpaces, row, column):
    """
    This function creates an index based chessboard
    :param numberOfBlackSpaces:
    :param numberOfWhiteSpaces:
    :param row:
    :param column:
    :return:
    """

    for setIndex1 in range(numberOfBlackSpaces):
        setA.append(setIndex1)
    for setIndex2 in range(numberOfBlackSpaces, numberOfWhiteSpaces+ numberOfBlackSpaces):
        setB.append(setIndex2)

    indexedChessBoard = [[0 for i in range(column)] for j in range(row)]
    setAIndex = 0
    setBIndex = 0
    for indexBoardRow in range(row):
        for indexBoardColumn in range(column):
            if (indexBoardRow + indexBoardColumn) % 2 == 1:
                indexedChessBoard[indexBoardRow][indexBoardColumn] = setB[setBIndex]
                setBIndex += 1
            elif (indexBoardRow + indexBoardColumn) % 2 == 0:
                indexedChessBoard[indexBoardRow][indexBoardColumn] = setA[setAIndex]
                setAIndex += 1
    return indexedChessBoard


def main():

    inputData = input().split()
    row = int(inputData[0])
    column = int(inputData[1])

    rowColData = []
    currentRowData = []

    for index1 in range(row):
        eachRowData = [int(k) for k in input().split()]
        for index2 in range(len(eachRowData)):
            currentRowData.append(eachRowData[index2])
        rowColData.append(currentRowData)
        currentRowData = []

    chessDetails = createAndColorBoard(row, column)

    colouredChessBoard,numberOfBlackSpaces , numberOfWhiteSpaces = chessDetails

    occupiedResult, occupiedBlackCount ,occupiedWhiteCount = findOccupiedSpaces(rowColData, row, column, colouredChessBoard)

    indexedChessBoard = createIndexedChessBoard(numberOfBlackSpaces, numberOfWhiteSpaces, row, column)

    graphArray = [[0 for i in range((column * row) + 2)] for j in range(((row * column) + 2))]

    for graphRow in range(row):
        for graphColumn in range(column):
            if (graphRow + graphColumn) % 2 == 0:
                if [graphRow, graphColumn] not in occupiedResult:
                    if not graphRow == 0:
                        graphArray[indexedChessBoard[graphRow][graphColumn]][
                            indexedChessBoard[graphRow - 1][graphColumn]] = 1
                    if not graphColumn == 0:
                        graphArray[indexedChessBoard[graphRow][graphColumn]][
                            indexedChessBoard[graphRow][graphColumn - 1]] = 1
                    if not graphRow + 1 == row :
                        graphArray[indexedChessBoard[graphRow][graphColumn]][
                            indexedChessBoard[graphRow + 1][graphColumn]] = 1
                    if not graphColumn + 1  == column:
                        graphArray[indexedChessBoard[graphRow][graphColumn]][
                            indexedChessBoard[graphRow][graphColumn + 1]] = 1

    for x in range(numberOfBlackSpaces):
        graphArray[row * column][x] = 1
    for y in range(numberOfWhiteSpaces):
        graphArray[y + numberOfBlackSpaces][(row * column) + 1] = 1

    occupiedIndexList = []
    for var in occupiedResult:
        occupiedIndexList.append(indexedChessBoard[var[0]][var[1]])

    for i in range(len(occupiedIndexList)):
        for t in range((row * column) + 2):
            graphArray[t][occupiedIndexList[i]] = 0
            graphArray[occupiedIndexList[i]][t] = 0

    if FordFulkerson(row * column, (row * column)+1 , graphArray) == max(len(setA) - occupiedBlackCount, len(setB) - occupiedWhiteCount):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
