# created by ilyas Aroui 20/10/2018

import numpy as np


def longest_subsequence3(n, m, l):
    """ Fill in the matrix D such that D[i, j, k] is the longest subsequence size between A[0:i], B[0:j] and C[0:k]
    D, A, B, C are passed to this function by reference.
        n : the length of the string input A
        m: the length of the string input B
        l: the length of the string input C
    :return:
        D[n, m, l]: the longest subsequence size between A[0:n], B[0:m] and C[0:l]
    """
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    D[i, j, k] = D[i - 1, j - 1, k - 1] + 1
                else:
                    D[i, j, k] = max([D[i - 1, j, k], D[i, j - 1, k], D[i, j, k-1]])

    return D[n, m, l]


def output_alignment(i, j, k):
    """ Backtrack from the the cell D[i, j, k] up to [0, 0, 0] to find the longest common subsequence.
    :param i: row index in matrix D
    :param j: column index in matrix D
    :param k: depth index in matrix D
    :return:
        it doesn't return a result. However it fills in the the string common_sequence which is a global variable.
    """
    global common_sequence
    if i == 0 and j == 0:
        return
    if i > 0 and D[i, j, k] == D[i-1, j, k]:
        output_alignment(i - 1, j, k)
    elif j > 0 and D[i, j, k] == D[i, j - 1, k]:
        output_alignment(i, j - 1, k)
    elif k > 0 and D[i, j, k] == D[i, j, k - 1]:
        output_alignment(i, j, k - 1)
    else:
        output_alignment(i-1, j-1, k-1)
        if i >= j and i >= k:
            common_sequence += A[i-1]
        elif j >= i and j >= k:
            common_sequence += B[j-1]
        else:
            common_sequence += C[k-1]


def read_data():
    """
    :return:
    n: length of sequence1
    m: length of sequence2
    sequence1: a string input
    sequence2: a string input
    sequence3: a string input
    """
    sequence1 = input("sequence1:")
    sequence2 = input("sequence2:")
    sequence3 = input("sequence3:")
    n = len(sequence1)
    m = len(sequence2)
    l = len(sequence3)
    return n, m, l, sequence1, sequence2, sequence3


n, m, l, A, B, C = read_data()
common_sequence = ''
D = np.zeros((n + 1, m + 1, l + 1), dtype=np.uint64)
longest_sequence_size = longest_subsequence3(n, m, l)
output_alignment(n, m, l)

print("longest_common sequence_size", longest_sequence_size)
print("common sequence: ", common_sequence)
