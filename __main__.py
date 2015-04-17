import numpy as np
from qr import qr

toCompute = np.array([
        [12, -51,   4],
        [ 6, 167, -68],
        [-4,  24, -41], 
        ])
print "Computing for:"
print toCompute
result = qr(toCompute, 10000)

print "Your result"
print np.diagonal(result)
print result

print "Numpy result"
w, v = np.linalg.eig(toCompute)
print w
print v
