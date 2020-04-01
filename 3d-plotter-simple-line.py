import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

fig = plt.figure()
ax = plt.axes(projection='3d')

#configs for animation
max_angle_y=180
max_angle_z=[20,40,75]

# path of pictures
path='/home/niklas/Desktop/School-Stuff/Data/3d-plotter-simple-data/'
folder=str(datetime.datetime.now())

# create folder for today
os.mkdir(path+folder)

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = [5]*1000
yline = [4]*1000
ax.plot(xline, yline, zline, 'b')

#animation for pictures
for angle2 in max_angle_z:
    last_angle=0
    for angle in range(0, max_angle_y):
        if last_angle!=angle2:
            file='pic'+str(angle2)+str(angle)
            plt.savefig(path + folder + '/' + file)
        ax.view_init(angle2, angle)
        plt.draw()
        plt.pause(.01)
        last_angle==angle2
#----------------------------------------------------------------------------------------
# from matplotlib import pyplot as plt
# import numpy as np
# import mpl_toolkits.mplot3d.axes3d as p3
# from matplotlib import animation
#
# fig = plt.figure()
# ax = p3.Axes3D(fig)
#
# def gen(n):
#     phi = 0
#     while phi < 2*np.pi:
#         yield np.array([np.cos(phi), np.sin(phi), phi])
#         phi += 2*np.pi/n
#
# def update(num, data, line):
#     line.set_data(data[:2, :num])
#     line.set_3d_properties(data[2, :num])
#
# N = 100
# data = np.array(list(gen(N))).T
# line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
#
# # Setting the axes properties
# ax.set_xlim3d([-1.0, 1.0])
# ax.set_xlabel('X')
#
# ax.set_ylim3d([-1.0, 1.0])
# ax.set_ylabel('Y')
#
# ax.set_zlim3d([0.0, 10.0])
# ax.set_zlabel('Z')
#
# ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
# #ani.save('matplot003.gif', writer='imagemagick')
# plt.show()