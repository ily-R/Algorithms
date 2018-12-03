# use python 3

import numpy as np

n = int(input())
A = [x for x in input().split()]
m = int(input())
B = [x for x in input().split()]
t = int(input())
C = [x for x in input().split()]
D = np.zeros((n+1, m+1, t+1), dtype=np.uint64)


def longest_subsequence(s1, s2, s3):

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            for k in range(1, len(s3) + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    D[i][j][k] = D[i - 1][j - 1][k - 1] + 1
                else:
                    D[i][j][k] = max([D[i - 1][j][k], D[i][j - 1][k], D[i][j][k-1]])


    return D[len(s1)][len(s2)][len(s3)]

# commun_sequence = ''
# def output_alignment(i, j):
#     global  commun_sequence
#     if i == 0 and j == 0:
#         return
#     if i > 0 and D[i][j] == D[i-1][j]:
#         output_alignment(i - 1, j)
#     elif j > 0 and D[i][j] == D[i][j - 1]:
#         output_alignment(i, j - 1)
#     else:
#         output_alignment(i-1, j-1)
#         if i >=j:
#             commun_sequence += A[i - 1]
#         else:
#             commun_sequence += A[j - 1]
#


print(longest_subsequence(A, B, C))
