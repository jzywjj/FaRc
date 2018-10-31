import numpy as np
from numpy import dtype

a=np.array([12.12,12.55,13.33],dtype=np.float)

print(a)
astr=a.tostring()
print(astr)
s=np.fromstring (astr,dtype=np.float)
print(s)