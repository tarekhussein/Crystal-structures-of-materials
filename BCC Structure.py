import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ai=2.856
aj=2.856
ak=2.856
radius=15

num_x_cells=10
num_y_cells=10
num_z_cells=10

x_values = []
y_values = []
z_values = []

for i in range (-num_x_cells, num_x_cells+1):
     for j in range (-num_y_cells, num_y_cells+1):
       for k in range (-num_z_cells, num_z_cells+1):

        if ((ai*i)**2 + (aj*j)**2 + (ak*k)**2) <= radius**2:

         x_values.append (ai*i)
         y_values.append (aj*j)
         z_values.append (ak*k)

        if ((ai * (i + 1.0/2))**2 + (aj * (j +1.0/2))**2 + (ak * (k + 1.0/2))**2) <= radius**2:

         x_values.append(ai*(i + 1.0/2))
         y_values.append(aj*(j + 1.0/2))
         z_values.append(ak*(k + 1.0/2))

fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x_values, y_values, z_values)

ax.set_xlabel("x(A°)", color='b', fontsize=14)
ax.set_ylabel("y(A°)", color='b', fontsize=14)
ax.set_zlabel("z(A°)", color='b', fontsize=14)
ax.set_title("BCC Structure", color='r', fontsize=16)

plt.show()
plt.savefig("BCC crystal structure")