import numpy as np
from scipy.linalg import svd

m1=np.array([[1,3,5,7],[9,11,13,15],
             [17,19,21,23],[25,27,29,31]])
print("Matrix:\n",m1)

X,B,T=svd(m1)
print("matrix X:\n",X)
print("matrix B:\n",B)
print("matrix T:\n",T)

ad=np.add(X,T)
print("Sum of X and T is:\n",ad)
st=np.subtract(X,T)
print("Difference of X and T is:\n",st)
dt=np.multiply(X,X)
cb=np.multiply(dt,X)
sc=np.multiply(2,cb)
print("The matrix 2X^3 is:\n",sc)