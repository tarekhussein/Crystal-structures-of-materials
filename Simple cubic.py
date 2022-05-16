import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ai=1
aj=1
ak=1

num_x_cells=2
num_y_cells=2
num_z_cells=2

x_values=[]
y_values=[]
z_values=[]

for i in range(0,num_x_cells):
     for j in range(0,num_y_cells):
        for k in range(0,num_z_cells):
         x_values.append(ai*i)
         y_values.append(aj*j)
         z_values.append(ak*k)

fig=plt.figure()
ax=Axes3D(fig)

ax.scatter(x_values, y_values, z_values)
plt.show()