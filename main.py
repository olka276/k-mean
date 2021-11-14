import time

import matplotlib.pyplot as plt
import utils as ut

colors = {
    0: "yellow",
    1: "violet",
    2: "red",
    3: "green",
    4: "blue",
    5: "pink",
    6: "orange"
}

print('Type amount of groups')
groups = int(input())

print(groups)

data = ut.txt_num_read("spiralka.txt")
x_y_array = ut.transform_to_x_y_arrays(data)

avgs = data[0:groups]
x_y_avgs = ut.transform_to_x_y_arrays(avgs)

clusters = {}

for i in range(100):
    for i in range(len(avgs)):
        plt.plot(avgs[i][0], avgs[i][1], "*", color=colors[i])

    for point in data:
        closestAvgIndex = (ut.get_closest_avg(point, avgs))
        clusters.setdefault(closestAvgIndex, []).append(point)
    print(clusters.keys())
    for index in clusters:
        x_y_pts = ut.transform_to_x_y_arrays(clusters[index])
        plt.plot(x_y_pts[0], x_y_pts[1], "o", color=colors[index])

    avgs = ut.get_avgs_of_clusters(clusters)
    plt.show()
    time.sleep(1)
    plt.clf()

