# use python 3

import numpy as np

n = int(input())
A = [x for x in input().split()]
m = int(input())
B = [x for x in input().split()]
D = np.zeros((n+1, m+1), dtype=np.uint64)


def longest_subsequence():

    for i in range(1, n+1):
        for j in range(1, m+1):

            if A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max([D[i-1][j], D[i][j-1]])
    return D[n][m]


print(longest_subsequence())
