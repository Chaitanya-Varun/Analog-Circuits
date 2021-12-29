import numpy as np
import matplotlib.pyplot as plt
#Case-1
W = 1* 1e-6
#print(W)
L = 1e-6
Vgs0 = 577.709*1e-3
Vt = 315.12*1e-3
gm0 = 12.637*1e-6
beta = gm0/((W/L)*(Vgs0-Vt))
print("Beta : "+str(beta))
Ids = beta*(W/(2*L))*np.power(Vgs0-Vt,2)
print("Ids : "+str(Ids))
gds0 = 669.274*1e-9
lam = gds0/Ids
print("Lambda : "+str(lam))
gmin = gm0-gm0/2
gmax = gm0+gm0/2
print("Range of Gms in mmho: ("+str(gmin*1e6)+","+str(gmax*1e6)+")")

