# importing the required modules 
import matplotlib.pyplot as plt
import numpy as np

# setting the max and min
min_range = 0
max_range = 20

# setting the x - coordinates 
x_1 = np.arange(min_range, max_range, 0.25)
#x_2 = np.arange(min_range, max_range, 0.25)

# setting the corresponding y - coordinates 
y_1 = 200*x_1**2+420*x_1+800
#y_2 = np.cos(x_2)

# style
plt.style.use('dark_background')

# naming the x axis 
plt.xlabel('x - axis')
# naming the y axis 
plt.ylabel('y - axis')
# giving a title to my graph 
plt.title('Ploter')

# potting the points
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white
plt.axhline(y=0, color='w')
# plt.stem(x_1,y_1, 'b')
plt.plot(x_1, y_1, label='line 1', marker='o', color='b')
#plt.plot(x_2, y_2, label='line 2', marker='o', color='y')

# shows the grid
plt.grid(alpha=4, linestyle='--')

# show a legend on the plot 
plt.legend()

# function to show the plot 
plt.show()
