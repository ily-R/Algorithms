#   Created by ilyas Aroui on 14/10/2018.

import numpy as np
import matplotlib.pyplot as plt
import random
import time


def partition3(a, l, r):
    """Partition a list of integers into 3 parts with respect to the pivot (a[l]).

        a: a list of integers.
        l: lefmost index of list 'a'.
        r: rightmost index of list 'a'.

    return:
        j: all integers from list 'a' in range(l, j+1) are less than the pivot.
        k: all integers from list 'a' in range(k, r+1) are greater than the pivot.

    so all integers from list 'a' in range(j+1,k) are equal to the pivot.
    """
    pivot = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if j > k:
            k = j
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

        elif a[i] == pivot:
            k += 1
            a[i], a[k] = a[k], a[i]

    a[l], a[j] = a[j], a[l]
    return j, k


def partition2(a, l, r):
    """Partition a list of integers to 2 parts with respect to the pivot (a[l]).

        a: a list of integers.
        l: lefmost index of list 'a'.
        r: rightmost index of list 'a'.

    return:
        j: all integers from list 'a' in range(l, j+1) are less then the pivot.


    so all integers from list 'a' in range(j+1,r) are equal or greater than the pivot.
    """
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort3(numbers, l, r):
    """sort a list of integers (which has many equal elements) using
    randomized_quick_sort and partition3.

        numbers: a list of integers.
        l: lefmost index of list 'numbers'.
        r: rightmost index of list 'numbers'.

    return:
        numbers: the sorted version of 'numbers' in the ascending order.
    """

    if l >= r:
        return
    k = random.randint(l, r)
    numbers[l], numbers[k] = numbers[k], numbers[l]
    m1, m2 = partition3(numbers, l, r)
    randomized_quick_sort3(numbers, l, m1 - 1)
    randomized_quick_sort3(numbers, m2 + 1, r)
    return numbers


def randomized_quick_sort2(numbers, l, r):
    """sort a list of integers (which does not have many equal elements) using
    randomized_quick_sort and partition2.

        numbers: a list of integers.
        l: lefmost index of list 'numbers'.
        r: rightmost index of list 'numbers'.

    return:
        numbers: the sorted version of 'numbers' in the ascending order.
    """
    if l >= r:
        return
    k = random.randint(l, r)
    numbers[l], numbers[k] = numbers[k], numbers[l]
    m = partition2(numbers, l, r)
    randomized_quick_sort2(numbers, l, m - 1)
    randomized_quick_sort2(numbers, m + 1, r)
    return numbers


def randomized_quick_sort_complexity():
    """randomized_quick_sort_complexity
        plot the running time of randomized_quick_sort2 and
        randomized_quick_sort3 versus the list size.

        for each size n generate n random integers uniformly in range (0, 10000) and
        apply random_quick_sort2 and random_quick_sort3 and measure the running time.

        as n increases randomized_quick_sort2 tend to O(n²) as there are more and more equal numbers in the list.
        but randomized_quick_sort3 stays around O(n*log(n))
    """
    N = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,200000,300000,400000,500000,
         700000, 1000000]
    timings3 = []
    timings2 = []
    for n in N:
        T3 = 0
        T2 = 0
        print(n)
        for i in range(20):
            numbers = np.random.random_integers(0, 10000, n)
            t3 = time.time()
            output3 = randomized_quick_sort3(numbers, 0, n-1)
            t_elapsed3 = time.time() - t3
            T3 += t_elapsed3

            t2 = time.time()
            output2 = randomized_quick_sort2(numbers, 0, n-1)
            t_elapsed2 = time.time() - t2
            T2 += t_elapsed2

        timings3.append(T3/20)
        timings2.append(T2/20)

    plt.plot(N, timings3, 'r--')
    plt.plot(N, timings2, 'b--')
    plt.show()


print(randomized_quick_sort2([3, 5, 1, 0, -1, 5, 4, 4, 4], 0, 8))
#  randomized_quick_sort_complexity()
