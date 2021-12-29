import numpy as np

# print("Hello World")
def convdb(val):
    return np.power(10,val/20)
# 1mv
db = [-43.313635,-64.505092,-74.744921,-84.448819,-111.03679]
# 50mV
# db = [-27.268479,-44.323985,-36.613191,-46.514257,-41.992662,-48.100156,-46.321828]
V = []
for i in db:
    V.append(convdb(i))
# print(V)
THD = 0
for i in V:
    THD = THD+np.power(i,2)
THD = np.sqrt(THD-np.power(V[0],2))/V[0]
print(THD)
# print(len(db))