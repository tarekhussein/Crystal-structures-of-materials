import numpy as np
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D

ai = 2.856
aj = 2.856
ak = 2.856
R = 15
num_x_cells = np.linspace(-R,R,30)
num_y_cells = np.linspace(-R,R,30)  
num_z_cells = np.linspace(-R,R,30)

x_values = []
y_values = []
z_values = []
for i in num_x_cells:
    for j in num_y_cells:
        for k in num_z_cells:
          if ((ai*i)**2)+((aj*j)**2)+((ak*k)**2)<=(R**2):
            x_values.append(ai * i)
            y_values.append(aj* j)
            z_values.append(ak * k)

            x_values.append(ai * (i + 1.0/2))
            y_values.append(aj * (j + 1.0/2))
            z_values.append(ak * (k + 1.0/2))

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('x[Å]')
ax.set_ylabel('y[Å]')
ax.set_zlabel('z[Å]')
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
ax.set_zlim(-15,15)
ax.scatter(x_values, y_values, z_values)
ax.set_title("BCC Crystal")
plt.show()
fig.savefig('Crystal_Lattice.png')


