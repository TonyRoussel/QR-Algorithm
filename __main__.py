import numpy as np
from qr import qr
from sklearn.preprocessing import normalize

toCompute = np.array([
        [12, -51,   4],
        [ 6, 167, -68],
        [-4,  24, -41], 
        ])
print "Computing for:"
print toCompute
eigenvalue, eigenvector = qr(toCompute, 100)

print "Your result"
print eigenvalue
print eigenvector
#print normalize(eigenvector)

print "Numpy result"
w, v = np.linalg.eig(toCompute)
print w
print v
