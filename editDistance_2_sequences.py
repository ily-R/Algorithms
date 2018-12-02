# created by ilyas Aroui 10/10/2018

import numpy as np


def edit_distance(n, m):
    """ Fill in the matrix D such that D[i, j] is the minimal distance between A[0:i] and B[0:j]
    D, A and B are passed to this function by reference.
        n : the length of the string input A
        m: the length of the string input B
    :return:
        D[n, m]: the minimal editing distance between A[0:n] and B[0:m]
    """

    for index_i in range(n+1):  # we are doing insertion here as string D[index_i, 0] means B is empty.
        D[index_i, 0] = index_i
    for index_j in range(m+1):  # we are doing deletion here as string D[index_i, 0] means A is empty.
        D[0, index_j] = index_j
    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = D[i, j-1] + 1
            deletion = D[i-1, j] + 1
            match = D[i-1, j - 1]
            mismatch = D[i-1, j - 1] + 1
            if A[i-1] == B[j-1]:
                D[i, j] = np.min([insertion, deletion, match])
            else:
                D[i, j] = np.min([insertion, deletion, mismatch])
    return D[n, m]


def output_alignment(i, j):
    """ Backtrack from the the cell D[i, j] up to [0, 0] to find the output alignment that gives the minimal distance.
    :param i: row index in matrix D
    :param j: column index in matrix D
    :return:
        it doesn't return a result. However it fills in the the strings first_line and second_line passed by reference.
    """
    if i == 0 and j == 0:
        return
    if i > 0 and D[i][j] == D[i-1][j] + 1:  # means a deletion was performed.
        output_alignment(i - 1, j)
        first_line.append(A[i-1])
        second_line.append('_')
    elif j > 0 and D[i][j] == D[i][j - 1] + 1:  # means an insertions was performed.
        output_alignment(i, j - 1)
        first_line.append('_')
        second_line.append(B[j-1])
    else:
        output_alignment(i-1, j-1)
        first_line.append(A[i-1])
        second_line.append(B[j-1])


def read_data():
    """
    :return:
    n: length of sequence1
    m: length of sequence2
    sequence1: a string input
    sequence2: a string input
    """
    sequence1 = input()
    sequence2 = input()
    n = len(sequence1)
    m = len(sequence2)
    return n, m, sequence1, sequence2


n, m, A, B = read_data()
first_line, second_line = [], []
D = np.zeros((n+1, m+1), dtype=np.uint64)
minimal_distance = edit_distance(n, m)
output_alignment(n, m)

# print the content of first_line and second_line
[print(item, end=' ') for item in first_line]
print('')
[print(item, end=' ') for item in second_line]
print('')
print(D)
