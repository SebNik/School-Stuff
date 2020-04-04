import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

def plot_surface_cube(x,y,z,a=0.5):
    X=(0,x)
    Y=(0,y)
    X, Y = np.meshgrid(X, Y)
    one = np.zeros(4).reshape(2, 2)
    one = one+z
    ax.plot_surface(X,Y,one, alpha=0.3)
    ax.plot_wireframe(X,Y,-one, alpha=0.5)
    ax.plot_wireframe(X,-one,Y, alpha=0.5)

def plot_line(x,y,z,a=0.5):
    # Data for a three-dimensional line
    zline = np.linspace(0, 2, 1000)
    xline = [0] * 1000
    yline = [0] * 1000
    #ax.plot(xline, yline, zline, 'b')

def animation(max_angle_z,max_angle_y,path,folder,state=True):
    # animation for pictures
    for angle2 in max_angle_z:
        last_angle = 0
        for angle in range(0, max_angle_y):
            if last_angle != angle2 and state:
                file = 'pic' + str(angle2) + str(angle)
                plt.savefig(path + folder + '/' + file)
            ax.view_init(angle2, angle)
            plt.draw()
            plt.pause(.01)
            last_angle = angle2

fig = plt.figure()
ax = plt.axes(projection='3d')

# configs for animation
max_angle_y = 180
max_angle_z = [90]

# path of pictures
path = '/home/niklas/Desktop/School-Stuff/Data/3d-plotter-simple-data/'
folder = str(datetime.datetime.now())

# create folder for today
os.mkdir(path + folder)

# setting the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plot_surface_cube(2,3,4)
plt.show()
