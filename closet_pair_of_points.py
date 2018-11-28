# created by ilyas Aroui 02/10/2018

from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


def euclidean_distance(p1, p2):
    """ Find the euclidean distance between two points in the plane.

        p1: coordinates of a point. tuple (x, y)
        p2: coordinates of a point. tuple (x, y)

    return:
        dist: the distance between p1 and p2

    """
    dist = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return dist


def strip(left_points, right_points, minimum_distance, x_axis):
    """ find the points in strip of width 2*minimum distance, and centered at the x_axis that splits the plane.
            left_points : list of sorted coordinates (tuples), with respect to y, containing all the point to the left
                                                                                                    of the x_axis.
            right_points : list of sorted coordinates (tuples), with respect to y, containing all the point to the right
                                                                                                    of the x_axis.
        return:
            strip_points: list of coordinates of the points that are on the strip. sorted with respect to the y.
            strip_size: the number of points in the strip.


    """
    strip_points = []
    left_index = 0
    right_index = 0
    l_left = len(left_points)
    l_right = len(right_points)
    strip_size = 0

    """ we merge the left_points and the right_points in strip_points, in an ascending order with respect to y.
         Making sure all the points added to the strip have a distance to the x_axis less than minimum_distance"""
    while left_index < l_left and right_index < l_right:
        if left_points[left_index][1] <= right_points[right_index][1]:
            if np.abs(left_points[left_index][0] - x_axis) < minimum_distance:
                strip_points.append(left_points[left_index])
                strip_size += 1
            left_index += 1

        else:
            if np.abs(right_points[right_index][0] - x_axis) < minimum_distance:
                strip_points.append(right_points[right_index])
                strip_size += 1
            right_index += 1

    """ now we check with the remaining points on either the right_points list OR the left_point list"""

    while right_index < l_right:
        if np.abs(right_points[right_index][0] - x_axis) < minimum_distance:
            strip_points.append(right_points[right_index])
            strip_size += 1
        right_index += 1
        return strip_points, strip_size

    while left_index < l_left:
        if np.abs(left_points[left_index][0] - x_axis) < minimum_distance:
            strip_points.append(left_points[left_index])
            strip_size += 1
        left_index += 1
        return strip_points, strip_size


def minimum_distance(points_sorted_x, points_sorted_y, n):
    """ (recursive divide & conquer function)
            find the distance between the closest points in points_sorted_x

            points_x_sorted = a sorted list of tuples with respect to the x coordinate.
                            each tuple contains the coordinates of a single point.
            points_y_sorted = a sorted list of tuples with respect to the y coordinate.
                            each tuple contains the coordinates of a single point.
            n: the number of points.
        return:
            d: the distance between the closest points in points_sorted_x
    """
    if n == 2:
        return euclidean_distance(points_sorted_x[0], points_sorted_x[1])
    if n == 3:
        da = euclidean_distance(points_sorted_x[0], points_sorted_x[1])
        db = euclidean_distance(points_sorted_x[0], points_sorted_x[2])
        dc = euclidean_distance(points_sorted_x[1], points_sorted_x[2])
        return min(da, db, dc)

    m = floor(n/2)
    x_axis = (points_sorted_x[m - 1][0] + points_sorted_x[m][0]) / 2  # split the plane and solve each part separately.
    left_points_y_sorted = []
    right_points_y_sorted = []
    for point in points_sorted_y:
        if point[0] <= x_axis:
            left_points_y_sorted.append(point)
        else:
            right_points_y_sorted.append(point)

    d_left = minimum_distance(points_sorted_x[:m], left_points_y_sorted, m)
    d_right = minimum_distance(points_sorted_x[m:], right_points_y_sorted, n-m)
    d = np.min([d_left, d_right])
    strip_points, strip_size = strip(left_points_y_sorted, right_points_y_sorted, d, x_axis)
    for i in range(strip_size-1):
        for j in range(i+1, min(i+6, strip_size)):  # check only up to the sixth point on the strip.
            d = min(d, euclidean_distance(strip_points[i], strip_points[j]))
    return d


def read_data():
    """ Read n points from the keyboard point by point.

    return:
        n: the number of points.
        points_x_sorted = a sorted list of tuples with respect to the x coordinate.
                            each tuple contains the coordinates of a single point.

        points_y_sorted = a sorted list of tuples with respect to the y coordinate.
                            each tuple contains the coordinates of a single point.
    """
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple([int(x) for x in input().split()]))

    points_x_sorted = sorted(points)
    points_y_sorted = sorted(points, key=lambda x: x[1])
    return n, points_x_sorted, points_y_sorted



n, points_x_sorted, points_y_sorted = read_data()
print(minimum_distance(points_x_sorted, points_y_sorted, n))





