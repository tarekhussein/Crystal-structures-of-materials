import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


ai=1.0
aj=1.0
ak=1.0

num_x_cells=1
num_y_cells=1
num_z_cells=1

x_values=[]
y_values=[]
z_values=[]

x_values1=[]
y_values1=[]
z_values1=[]

x_values2=[]
y_values2=[]
z_values2=[]

mid = [1,1,1]
base = [1,0,0]

for i in range(0,num_x_cells+1):
    for j in range(0,num_y_cells+1):
        for k in range(0,num_z_cells+1):
            x_values.append(ai*i)
            y_values.append(aj*j)
            z_values.append(ak*k)

#        if i != j and j == k == 0.5 : 
#                  x_values.append(i)
#                  y_values.append(j)
#                  z_values.append(k)
#                  
#        if j != k and i == k == 0.5 :
#                  x_values.append(i)
#                  y_values.append(j)
#                  z_values.append(k)
#                  
#        if i != j and j == k == 0.5 :
#                  x_values.append(i)
#                  y_values.append(j)
#                  z_values.append(k)

for i in range (0, len(x_values)):
    directions = [x_values[i], y_values[i], z_values[i]]
    X = np.array(directions) - np.array(base)
    dot_product = np.dot( (np.array( mid )), (np.array(X)) )

    if dot_product == 0:
        x_values1.append (x_values[i])
        y_values1.append (y_values[i])
        z_values1.append (z_values[i])
    else:
        x_values2.append (x_values[i])
        y_values2.append (y_values[i])
        z_values2.append (z_values[i])          
         
fig=plt.figure()
ax=Axes3D(fig)
ax2 = fig.gca(projection='3d')

for i,j,k in zip(x_values1, y_values1, z_values1):
    ax2.plot([1,0,0],[0,1,0],[0,0,1],color = "blue")
    ax2.plot([0,1,0],[1,0,0],[0,0,1],color = "blue")
    
    ax2.plot([0,0,0],[1,0,0],[1,1,0],color = "black") 
    ax2.plot([0,0,1],[1,0,0],[1,1,1],color = "black") 
    ax2.plot([0,0,1],[1,0,0],[0,0,0],color = "black")
    ax2.plot([1,1,1],[1,1,0],[0,1,1],color = "black")
    ax2.plot([1,1,1],[0,0,0],[0,0,1],color = "black")
    ax2.plot([1,1,1],[0,1,0],[0,0,0],color = "black")
    ax2.plot([0,0,1],[1,1,1],[0,1,1],color = "black")
    ax2.plot([1,0,1],[1,1,1],[0,0,0],color = "black")

ax.scatter(x_values, y_values, z_values)
ax.scatter(x_values1, y_values1, z_values1, color="green", s=400)
ax.scatter(x_values2, y_values2, z_values2, color="red", s=400)

ax.set_xlabel("x-axis", color='b', fontsize=14)
ax.set_ylabel("y-axis", color='b', fontsize=14)
ax.set_zlabel("z-axis", color='b', fontsize=14)
ax.set_title("Plane (1, 1, 1)", color='r', fontsize=16)

plt.show()
plt.savefig("Plane (1,1,1)")


