import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ai=1
aj=1
ak=1

num_x_cells=1
num_y_cells=1
num_z_cells=1

x_values=[]
y_values=[]
z_values=[]

for i in range(0,num_x_cells+2):
     for j in range(0,num_y_cells+2):
        for k in range(0,num_z_cells+2):
         x_values.append(ai*i)
         y_values.append(aj*j)
         z_values.append(ak*k)
         
        if i != j and j == k == 0.5 : 
                  x_values.append (i)
                  y_values.append (j)
                  z_values.append (k)
                  
        if j != k and i == k == 0.5 :
                  x_values.append (i)
                  y_values.append (j)
                  z_values.append (k)
                  
        if i != j and j == k == 0.5 :
                  x_values.append (i)
                  y_values.append (j)
                  z_values.append (k)

fig=plt.figure()
ax=Axes3D(fig)

ax.scatter(x_values, y_values, z_values)
plt.show()