import random
import time

from matplotlib import pyplot as plt

import metrics as m

cmap = plt.get_cmap("tab10").colors


def txt_num_read(path):
    f = open(path, 'r')

    data = []

    for line in f:
        temp = line.strip().split()
        data.append([float(temp[0]), float(temp[1])])

    return data


def transform_to_x_y_arrays(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])

    return [x, y]


# returns associative array of x array and y array
def get_random_avgs(group_amount, data):
    dict = {}
    avgs = random.sample(data, group_amount)
    for i in range(group_amount):
        dict[i] = avgs[i]
    return dict


def get_closest_avg(point, avgs):
    distances = []
    for i in avgs.keys():
        distances.append(m.euclidean(point, avgs[i]))

    return get_index_of_the_smallest_value(distances)


def get_index_of_the_smallest_value(distances):
    smallest_index = 0
    for i in range(1, len(distances)):
        if distances[smallest_index] > distances[i]:
            smallest_index = i

    return smallest_index


def get_avgs_of_clusters(groups):
    dict = {}
    for group in groups:
        dict[group] = get_avg_of_arrays(groups[group])
    return dict


def get_avg_of_arrays(arr):
    length = len(arr)
    sum_x = 0
    sum_y = 1

    for elem in arr:
        sum_x += elem[0]
        sum_y += elem[1]
    return [sum_x / length, sum_y / length]


def draw(grouped_point, avgs):
    for j in grouped_point.keys():
        xyArr = transform_to_x_y_arrays(grouped_point[j])
        plt.plot(xyArr[0], xyArr[1], "o", color=cmap[j])
        plt.plot(avgs[j][0], avgs[j][1], "*", color=cmap[j])

    plt.show()
