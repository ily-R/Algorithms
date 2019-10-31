# created by ilyas Aroui 12/11/2018

import numpy as np
import operator

# define a dictionary which maps an operator symbol to its actual operation.
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def parentheses(n):
    """ Fill in the matrices M and m such that M[i, j] is the maximum output of the expression with numbers(i:j+1)
    and m[i, j] is the minimum output of the expression with numbers(i:j+1). m and M are upper triangular matrices.
    M and m are passed to this function by reference.
        n : the length of the list that contains the numbers in the input expression
    :return:
        M[0, n-1]: the maximum output of the input expression with numbers(0:n)
    """
    global m
    global M
    for i in range(n):
        m[i, i] = numbers[i]
        M[i, i] = numbers[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i, j], M[i, j] = max_min(i, j)

    return M[0, n-1]


def max_min(i, j):
    """for an expression that contains the numbers with from index i to index j (included) check all the possibilities
    of operators in between. keep track of max and min, and return the optimal ones at the end of the loop
    :param i: the starting index of the expression
    :param j: the ending index of the expression
    :return:
        max_value:the maximum output of the expression with numbers(i:j+1)
        min_value:the minimum output of the expression with numbers(i:j+1)
    """
    min_value = 2 ^ 32
    max_value = -(2 ^ 32)
    for k in range(i, j):
        a = ops[operators[k]](M[i, k], M[k+1, j])
        b = ops[operators[k]](M[i, k], m[k + 1, j])
        c = ops[operators[k]](m[i, k], M[k + 1, j])
        d = ops[operators[k]](m[i, k], m[k + 1, j])
        min_value = np.min([min_value, a, b, c, d])
        max_value = np.max([max_value, a, b, c, d])

    return min_value, max_value


def putting_parantheses(i, j, max_value=True):
    """ Backtrack from the the cell M[n-1, n-1] to find right placement of the parentheses.
    The idea is to find the the two cells from matrices M and m that were used to get the value that we are 
    backtracking from.
    :param i: row index in matrix D
    :param j: column index in matrix D
    :param max_value: True if the value we want to backtrack from is in the matrix M.
                      False if the value we want to backtrack from is in the matrix m.
    :return:
        it doesn't return a result. However it fills in the the string expression which is a global variable.
        as well as it updates number_indices every recursive call (everytime a parentheses is added)
    """
    if j-i <= 1:
        return
    if max_value is True:
        value = M[i, j]
    else:
        value = m[i, j]
    global number_indices
    global expression
    for k in range(i, j):
        a = ops[operators[k]](M[i, k], M[k+1, j])
        b = ops[operators[k]](M[i, k], m[k + 1, j])
        c = ops[operators[k]](m[i, k], M[k + 1, j])
        d = ops[operators[k]](m[i, k], m[k + 1, j])
        if value == a:
            if k > i:
                expression.insert(number_indices[i], '(')
                number_indices[i:] += 1
                expression.insert(number_indices[k] + 1, ')')
                number_indices[k + 1:] += 1
            if j > k:
                expression.insert(number_indices[k + 1], '(')
                number_indices[k + 1:] += 1
                expression.insert(number_indices[j] + 1, ')')
                putting_parantheses(i, k)
                putting_parantheses(k + 1, j)
            break
        elif value == b:
            if k > i:
                expression.insert(number_indices[i], '(')
                number_indices[i:] += 1
                expression.insert(number_indices[k] + 1, ')')
                number_indices[k + 1:] += 1
                putting_parantheses(i, k)
            if j > k:
                expression.insert(number_indices[k + 1], '(')
                number_indices[k + 1:] += 1
                expression.insert(number_indices[j] + 1, ')')
                putting_parantheses(k + 1, j, max_value=False)
            break
        elif value == c:
            if k > i:
                expression.insert(number_indices[i], '(')
                number_indices[i:] += 1
                expression.insert(number_indices[k] + 1, ')')
                number_indices[k + 1:] += 1
                putting_parantheses(i, k, max_value=False)
            if j > k:
                expression.insert(number_indices[k + 1], '(')
                number_indices[k + 1:] += 1
                expression.insert(number_indices[j] + 1, ')')
                putting_parantheses(k + 1, j)

            break
        elif value == d:
            if k > i:
                expression.insert(number_indices[i], '(')
                number_indices[i:] += 1
                expression.insert(number_indices[k] + 1, ')')
                number_indices[k + 1:] += 1
                putting_parantheses(i, k, max_value=False)

            if j > k:
                expression.insert(number_indices[k + 1], '(')
                number_indices[k + 1:] += 1
                expression.insert(number_indices[j] + 1, ')')
                putting_parantheses(k + 1, j, max_value=False)
            break


def read_data():
    """
    :return:
    n: length of numbers
    operators: a list of all operators in the expression
    numbers: an int list that contains all the numbers in the expression
    expression : a string input
    """
    expression = input()
    numbers = [int(x) for i, x in enumerate(expression) if i % 2 == 0]
    operators = [x for i, x in enumerate(expression) if i % 2 == 1]
    n = len(numbers)
    expression = list(expression)
    return n, operators, numbers, expression


n, operators, numbers, expression = read_data()
number_indices = np.array([2*x for x in range(n)])
m = np.zeros((n, n), dtype=np.int64)
M = np.zeros((n, n), dtype=np.int64)
counter = 0
print(parentheses(n))
putting_parantheses(0, n-1)
for e in expression:
    print(e, end='')
