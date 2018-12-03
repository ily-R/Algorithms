# use python 3

import numpy as np
import operator


def parentheses(n):
    global m
    global M
    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = max_min(i, j)

    return M[0][n-1]


def max_min(i, j):
    min_value = 2 ^ 32
    max_value = -(2 ^ 32)
    for k in range(i, j):
        a = ops[operators[k]](M[i][k], M[k+1][j])
        b = ops[operators[k]](M[i][k], m[k + 1][j])
        c = ops[operators[k]](m[i][k], M[k + 1][j])
        d = ops[operators[k]](m[i][k], m[k + 1][j])
        min_value = np.min([min_value, a, b, c, d])
        max_value = np.max([max_value, a, b, c, d])

    return min_value, max_value


def putting_parantheses(i, j, max_value=True):
    if j-i <= 1:
        return
    if max_value is True:
        value = M[i][j]
    else:
        value = m[i][j]
    global number_indices
    global expression
    for k in range(i, j):
        a = ops[operators[k]](M[i][k], M[k+1][j])
        b = ops[operators[k]](M[i][k], m[k + 1][j])
        c = ops[operators[k]](m[i][k], M[k + 1][j])
        d = ops[operators[k]](m[i][k], m[k + 1][j])
        if value == a:
            expression.insert(number_indices[i], '(')
            number_indices[i:] += 1
            expression.insert(number_indices[k]+1, ')')
            number_indices[k+1:] += 1
            expression.insert(number_indices[k+1], '(')
            number_indices[k+1:] += 1
            expression.insert(number_indices[j]+1, ')')
            putting_parantheses(i, k)
            putting_parantheses(k+1, j)
            break
        elif value == b:
            expression.insert(number_indices[i], '(')
            number_indices[i:] += 1
            expression.insert(number_indices[k]+1, ')')
            number_indices[k+1:] += 1
            expression.insert(number_indices[k+1], '(')
            number_indices[k+1:] += 1
            expression.insert(number_indices[j]+1, ')')
            putting_parantheses(i, k,)
            putting_parantheses(k+1, j, max_value=False)
            break
        elif value == c:
            expression.insert(number_indices[i], '(')
            number_indices[i:] += 1
            expression.insert(number_indices[k]+1, ')')
            number_indices[k+1:] += 1
            expression.insert(number_indices[k+1], '(')
            number_indices[k+1:] += 1
            expression.insert(number_indices[j]+1, ')')
            putting_parantheses(i, k, max_value=False)
            putting_parantheses(k+1, j)
            break
        elif value == d:
            expression.insert(number_indices[i], '(')
            number_indices[i:] += 1
            expression.insert(number_indices[k]+1, ')')
            number_indices[k+1:] += 1
            expression.insert(number_indices[k+1], '(')
            number_indices[k+1:] += 1
            expression.insert(number_indices[j]+1, ')')
            putting_parantheses(i, k, max_value=False)
            putting_parantheses(k+1, j, max_value = False)
            break


ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
expression = input()
numbers = [int(x) for i, x in enumerate(expression) if i % 2 == 0]
operators = [x for i, x in enumerate(expression) if i % 2 == 1]
expression = list(expression)
n = len(numbers)
number_indices = np.array([2*x for x in range(n)])
m = np.zeros((n, n), dtype=np.int64)
M = np.zeros((n, n), dtype=np.int64)
counter = 0
print(parentheses(n))
putting_parantheses(0, n-1)
for e in expression:
    print(e, end = '')