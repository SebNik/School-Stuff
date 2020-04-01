import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

fig = plt.figure()
ax = plt.axes(projection='3d')

# configs for animation
max_angle_y = 180
max_angle_z = [20, 40, 75]

# path of pictures
path = '/home/niklas/Desktop/School-Stuff/Data/3d-plotter-simple-data/'
folder = str(datetime.datetime.now())

# create folder for today
os.mkdir(path + folder)

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = [5] * 1000
yline = [4] * 1000
ax.plot(xline, yline, zline, 'b')

# animation for pictures
for angle2 in max_angle_z:
    last_angle = 0
    for angle in range(0, max_angle_y):
        if last_angle != angle2:
            file = 'pic' + str(angle2) + str(angle)
            plt.savefig(path + folder + '/' + file)
        ax.view_init(angle2, angle)
        plt.draw()
        plt.pause(.01)
        last_angle = angle2
