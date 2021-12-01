import matplotlib.pyplot as plt
import utils as ut

cmap = plt.get_cmap("tab10").colors

print('Type amount of groups')
groups = int(input())

print('Type amount of iterations')
iterations = int(input())

data = ut.txt_num_read("spiralka.txt")
avgs = data[0:groups]

for i in range(iterations):
    # if first loop - get random elements as cluster avg
    if i == 0:
        avgs = ut.get_random_avgs(groups, data)

    # dictionary having group index => points
    grouped_point = {}

    # get avg point closest to point
    for point in data:
        closestAvgIndex = ut.get_closest_avg(point, avgs)
        if closestAvgIndex in grouped_point.keys():
            grouped_point[closestAvgIndex].append(point)
        else:
            grouped_point[closestAvgIndex] = [point]

    # draw a graph
    for j in grouped_point.keys():
        xyArr = ut.transform_to_x_y_arrays(grouped_point[j])
        plt.plot(xyArr[0], xyArr[1], "o", color=cmap[j])
        plt.plot(avgs[j][0], avgs[j][1], "*", color=cmap[j])

    avgs = ut.get_avgs_of_clusters(grouped_point)
    plt.show()
