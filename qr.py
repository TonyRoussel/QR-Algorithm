import numpy as np

def qr(toCompute, maxIter):
    A = []
    A.append(None)
    A.append(toCompute)
    for k in range(maxIter):
        A[0] = A[1]
        Q, R = qrDecomposition(A[0])
        A[1] = np.dot(R, Q)
        print k, "/", maxIter
    return A[1]

# QR DECOMPOSITION
def qrDecomposition(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householderOriginal(A[i:, i])
#         H[i:, i:] = make_householderSimplification(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A
 
def make_householderOriginal(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    beta = 2 / np.dot(v, v)
    vtv = np.dot(v[:, None], v[None, :])
    H -= beta * vtv
#     print "V:", v
#     print "Beta:", beta
#     print "vtv:", vtv
#     print "H:", H
    return H

def make_householderSimplification(a):
    u = a + np.copysign(np.linalg.norm(a), a[0])
    v = a / u[0]
    v[0] = 1
    H = np.eye(a.shape[0])
    beta = 2 / (np.dot(v, v.transpose()))
    vtv = np.dot(np.matrix(v).transpose(), np.matrix(v))
    H -= np.dot(beta, vtv)
#     print "u:", u
#     print "Beta:", beta
#     print "vtv:", vtv
#     print "H:", H
    return H
# !QR DECOMPOSITION

 
# a = np.array(((
#     (12, -51,   4),
#     ( 6, 167, -68),
#     (-4,  24, -41),
# )))
 
# q, r = qr(a)
# print 'q:\n', q.round(6)
# print 'r:\n', r.round(6)
