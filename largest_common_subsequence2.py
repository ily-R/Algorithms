# created by ilyas Aroui on 23/ 10/ 2018
import numpy as np


def longest_subsequence(n, m):
    """ Fill in the matrix D such that D[i, j] is the longest subsequence size between A[0:i] and B[0:j]
    D, A and B are passed to this function by reference.
        n : the length of the string input A
        m: the length of the string input B
    :return:
        D[n, m]: the longest subsequence size between A[0:n] and B[0:m]
    """
    for i in range(1, n+1):
        for j in range(1, m+1):

            if A[i-1] == B[j-1]:
                D[i, j] = D[i-1, j-1] + 1
            else:
                D[i, j] = max([D[i-1, j], D[i, j-1]])
    return D[n, m]


def output_alignment(i, j):
    """ Backtrack from the the cell D[i, j] up to [0, 0] to find the longest common subsequence.
    :param i: row index in matrix D
    :param j: column index in matrix D
    :return:
        it doesn't return a result. However it fills in the the string common_sequence which is a global variable.
    """
    global common_sequence
    if i == 0 and j == 0:
        return
    if i > 0 and D[i, j] == D[i-1, j]:
        output_alignment(i - 1, j)
    elif j > 0 and D[i, j] == D[i, j - 1]:
        output_alignment(i, j - 1)
    else:
        output_alignment(i-1, j-1)
        if i >=j:
            common_sequence += A[i-1]
        else:
            common_sequence += B[j-1]


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
common_sequence = ''
D = np.zeros((n + 1, m + 1), dtype=np.uint64)
longest_sequence_size = longest_subsequence(n, m)
output_alignment(n, m)

print(longest_sequence_size)
print(common_sequence)
