"""
File Name:  queens.py
Author:     Aditya Ajit Tirakannavar (at2650@rit.edu)
Course:     CSCI-665 Foundations of Algorithms
HW 2.5:     Write a program that finds if the placement of n # of queens on nxn board is a valid solution
            or the queens are placed in non-attacking postion.
            The first line of the input will be the board size and #queens, n, .
            This will be followed by n input lines,
            each line containing 2 numbers from range [1,n], which are cordinates / row and column postions of queen.
"""


def queens_validity_check(n, row,column ):
    '''
    The function gives the pairing of first grp element and second grp elements
    according to first grp element's preference.
    @:param : board size/queens
    @:param : rows in which queens are placed
    @:param : columns in which queens are placed
    @:return : String Value: 'YES': if placements are valid; 'NO': if placements are invalid
    Complexity :  O(n)
    '''
    # As the queen can move in 8 directions we have to check if the queen
    # is placed safely and free from any threat from any of the 8 positions
    row_index_check = [0]*(n)
    column_index_check = [0]*(n)
    left_diag_check = [0]*(2*n)
    right_diag_check = [0]*(2*n)
    # Checking if there are conflicting queens placed in the same row
    for i in range(n):
        if row[i] != row_index_check[row[i]-1]:
            row_index_check[row[i]-1] = row[i]
        else:
            # print('row')
            return 'NO'

    # Checking if there are conflicting queens placed in the same column
    for i in range(n):
        if column[i] != column_index_check[column[i]-1]:
            column_index_check[column[i]-1] = column[i]
        else:
            # print("col")
            return 'NO'

    left_diag_check = [0] * (2 * n)
    right_diag_check = [0] * (2 * n)
    # Checking if there are conflicting queens placed in the same left diagonal
    for i in range(n):
        if row[i]+column[i] != left_diag_check[row[i]+column[i]]:
            left_diag_check[(row[i] + column[i])] = row[i] + column[i]

        else:
            # print("left")
            return 'NO'
    # Checking if there are conflicting queens placed in the same right diagonal
    for i in range(n):
        if column[i]+(n-row[i]+1) != right_diag_check[column[i]+(n-row[i])-1]:
            right_diag_check[column[i]+(n-row[i])-1] = column[i]+(n-row[i]+1)
        else:
            # print("right")
            return 'NO'
    return "YES"

def main():
    # board size/queens
    n = int(input())
    row = []
    column = []
    # queen postions
    if n<= 10000000:
        for i in range(n):
            data = input().strip().split()
            row.append(int(data[0]))
            column.append(int(data[1]))
        print(queens_validity_check(n, row, column))
    else:
        exit()

if __name__ == '__main__':
    main()




