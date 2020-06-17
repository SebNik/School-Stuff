import numpy as np
import matplotlib.pyplot as plt
import datetime
import os


def plot_surface_cube(x, y, z, a=0.5):
    X = (0, x)
    Y = (0, y)
    X, Y = np.meshgrid(X, Y)
    one = np.zeros(4).reshape(2, 2)
    one = one + z
    ax.plot_surface(X, Y, one, alpha=0.3)
    ax.plot_wireframe(X, Y, -one, alpha=0.5)
    ax.plot_wireframe(X, -one, Y, alpha=0.5)


def plot_line(p, u, a=0.5, n=100):
    # 3d plotting a line with the equation g: x=p+u*t where p and u are vectors
    data = []
    p_vector = np.array(p)
    u_vector = np.array(u)
    for t in range(0, n):
        t = t * 0.1
        line = (p_vector + u_vector * t)
        data.append(line)
        # print(t, p_vector + u_vector * t)
    d = np.array(data)
    # print(d[:, 0])
    ax.plot(d[:, 0], d[:, 1], d[:, 2], 'b')


def animation(max_angle_z, max_angle_y, path, folder, state=True):
    # animation for pictures
    for angle2 in max_angle_z:
        last_angle = 0
        for angle in range(0, max_angle_y):
            if last_angle != angle2 and state:
                file = 'pic' + str(angle2) + str(angle)
                plt.savefig(path + folder + '/' + file)
            ax.view_init(angle2, angle)
            plt.draw()
            plt.pause(.001)
            last_angle = angle2


fig = plt.figure()
ax = plt.axes(projection='3d')

# configs for animation
max_angle_y = 180
max_angle_z = [50, 10]

# path of pictures
path = '/home/niklas/Desktop/School-Stuff/Data/3d-plotter-simple-data/'
folder = str(datetime.datetime.now())

# create folder for today
os.mkdir(path + folder)

# setting the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plot_line(p=[1, 2, 3], u=[1, 2, 3])
animation(max_angle_y=max_angle_y, max_angle_z=max_angle_z, path=path, folder=folder)
plt.show()
