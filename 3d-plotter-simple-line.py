import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot(xline, yline, zline, 'b')

# Data for three-dimensional scattered points
#zdata = 15 * np.random.random(100)
#xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
#ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
#ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
#ax.view_init(elev=10., azim=10)
# plt.savefig("movie%d.png" % 10)
#ax.view_init(elev=10., azim=80)
#plt.show()
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