import random
import metrics as m
import numpy as np


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
    avgs = []
    for i in range(group_amount):
        avg = (random.choice(data))

        while avg in avgs:
            avg = (random.choice(data))

        avgs.append(avg)
    return avgs


def get_closest_avg(point, avgs):
    distances = {}
    for i in range(len(avgs)):
        distances[i] = m.euclidean(point, avgs[i])

    return get_index_of_the_smallest_value(distances)


def get_index_of_the_smallest_value(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)

    for w in sorted_keys:
        sorted_dict[w] = dict[w]

    return list(sorted_dict.keys())[0]


def get_avgs_of_clusters(clusters):
    avgs = []
    for i in range(len(clusters)):
        avgs.append(get_avg_of_arrays(np.array(clusters[i])))
    return avgs


def get_avg_of_arrays(arr):
    length = len(arr)
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return [sum_x / length, sum_y / length]
