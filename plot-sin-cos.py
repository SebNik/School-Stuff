# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 

# setting the max and min
min_range=0
max_range=np.pi*4

#amplitude
amplitude=1
#periode
periode=2*np.pi

# f(x) = a*sin(b*x)+c 
a=amplitude # changing the amplitude
b=(1/periode)*(2*np.pi) # changing the periode
c=0 # changing the x-axis-intersecting-point
d=0 # changing the y-axis-intersecting-point

# setting the x - coordinates 
x_1 = np.arange(min_range, max_range, 0.25) 
x_2 = np.arange(min_range, max_range, 0.25)

# setting the corresponding y - coordinates 
y_1 = a*np.sin(b*x_1+c)+d
y_2 = np.sin(x_2)

# style
plt.style.use('dark_background')

# x-axises
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*3/2, np.pi*2, np.pi*5/2, np.pi*3, np.pi*7/2, np.pi*4],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$+2\pi$', r'$+5\pi/2$', r'$+3\pi$', r'$+7\pi/2$', r'$+4\pi$'])

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
#plt.stem(x_1,y_1, 'b')
plt.axhline(y=0, marker='o', color='w')
plt.plot(x_1, y_1, label='y={}sin({}+x)+{}'.format(a,b,c), marker='o', color='b') 
plt.plot(x_2, y_2, label='y=sin(x)', marker='o', color='y') 

# shows the grid
plt.grid(alpha=4,linestyle='--')
  
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 