# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# style
plt.style.use('dark_background')

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Ploter')

x_1= np.arange(0,10,0.1)
y_1=np.arange(0,10,0.1)

# plotting the points
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white
plt.plot(x_1, y_1, label='y={}sin({}x)+{}', marker='', color='b')

# shows the grid
plt.grid(alpha=4, linestyle='--')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()