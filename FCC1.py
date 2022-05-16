import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import numpy as np
ai = 1.0
aj = 1.0
ak = 1.0
num_x_cells = np.linspace(0,1,2)
num_y_cells = np.linspace(0,1,2)
num_z_cells = np.linspace(0,1,2)
num_X_cells = np.linspace(0,1,3)
num_Y_cells = np.linspace(0,1,3)
num_Z_cells = np.linspace(0,1,3)
x_values = []
y_values = []
z_values = []
X_values=[]
Y_values=[]
Z_values=[]
plane = list()
print('Enter numbers in array: ')
for i in range(3):
    n = input("num :")
    plane.append(float(n))
print('plane: ',plane)
basis=np.array([0,0,0])
k=plane.index(1)
basis[k]= 1
for i in num_x_cells:
    for j in num_y_cells:
        for k in num_z_cells:
            x_values.append(ai * i)
            y_values.append(aj * j)
            z_values.append(ak * k)
for i in num_X_cells:
    for j in num_Y_cells:
        for k in num_Z_cells:
            if i!=j and j==k==0.5:
                x_values.append(i)
                y_values.append(j)
                z_values.append(k)
            if j!=k and i==k==0.5:
                x_values.append(i)
                y_values.append(j)  
                z_values.append(k)
            if i!=k and i==j==0.5:
                x_values.append(i)
                y_values.append(j)  
                z_values.append(k)
####################################################################
#for i in num_x_cells:
#    for j in num_y_cells:
#        for k in num_z_cells:
#            a = np.array([i,j,k])
#            X = a - basis
#            if np.dot(plane,X) == 0:
#                X_values.append(i)
#                Y_values.append(j)
#                Z_values.append(k)
#for i in num_X_cells:
#    for j in num_Y_cells:
#        for k in num_Z_cells:
#            if i!=j and j==k==0.5:
#                a = np.array([i,j,k])
#                X = a - basis
#                if np.dot(plane,X) == 0:
#                    X_values.append(i)
#                    Y_values.append(j)
#                    Z_values.append(k)
#            if j!=k and i==k==0.5:
#                a = np.array([i,j,k])
#                X = a - basis
#                if np.dot(plane,X) == 0:
#                    X_values.append(i)
#                    Y_values.append(j)
#                    Z_values.append(k)
#            if i!=k and i==j==0.5:
#                a = np.array([i,j,k])
#                X = a - basis
#                if np.dot(plane,X) == 0:
#                    X_values.append(i)
#                    Y_values.append(j)
#                    Z_values.append(k)
#fig = plt.figure()
#ax = Axes3D(fig)
##############################cube outline########################################################
#x = []
#y = []
#z = []
#c = []
#for i in num_x_cells:
#    for j in num_y_cells:
#        for k in num_z_cells:
#            b = [i,j,k]
#            c.append(b)
#            x.append(i)
#            y.append(j)
#            z.append(k) 
#G = []
#H = []
#for i in range(0,len(c)):
#    for j in range(0,len(c)):
#        d = np.array(c[i])
#        e = np.array(c[j])
#        f = d-e
#        if np.sqrt(f[0]**2+f[1]**2+f[2]**2) == 1:
#            G.append(c[i])
#            H.append(c[j])            
#for i in range(0,len(G)):
#    k = 0; l = 2;
#    s = []
#    t = []
#    u = []
#    for j in range(k,l+1):
#        s.append((G[i])[0])
#        s.append((H[i])[0])
#        t.append((G[i])[1])
#        t.append((H[i])[1])
#        u.append((G[i])[2])
#        u.append((H[i])[2])
#        ax.plot3D(s,t,u,color='orange')
#        k+=3
#        l+=2
###############################################################################################
ax.set_xlabel('x[Å]')
ax.set_ylabel('y[Å]')
ax.set_zlabel('z[Å]')
ax.scatter(X_values,Y_values,Z_values,s=800, c='b',label='plane \n \n')
ax.scatter(x_values, y_values, z_values,s=100,c='r',label='FCC points')
ax.legend()
sai = "FCC:",plane
ax.set_title(sai)
plt.show()
fig.savefig('FCC_crystal.png')