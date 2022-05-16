import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
num_x_cells = np.linspace(0,1,2)
num_y_cells = np.linspace(0,1,2)
num_z_cells = np.linspace(0,1,2)
fig = plt.figure()
ax = Axes3D(fig)
c = []
for i in num_x_cells:
    for j in num_y_cells:
        for k in num_z_cells:
            b = [i,j,k]
            c.append(b)
G = []
H = []
for i in range(0,len(c)):
    for j in range(0,len(c)):
        d = np.array(c[i])
        e = np.array(c[j])
        f = d-e
        if np.sqrt(f[0]**2+f[1]**2+f[2]**2) == 1:
            G.append(c[i])
            H.append(c[j])   
            print(G)
            print(H)         
for i in range(0,len(G)):
    k = 0; l = 2;
    s = []
    t = []
    u = []
    for j in range(k,l+1):
        s.append((G[i])[0])
        s.append((H[i])[0])
        t.append((G[i])[1])
        t.append((H[i])[1])
        u.append((G[i])[2])
        u.append((H[i])[2])
        ax.plot3D(s,t,u,color='blue')
        k+=3
        l+=2
plt.show() 