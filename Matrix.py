
import numpy as np

T = np.array([[2, 7],
              [0, -1]])

C = np.array([[7, 1],
             [-3, 0]])


Cinv = np.linalg.inv(C)

# print(T.diagonal())
# print(Cinv)

D = Cinv@T@C
D = np.round(D , decimals = 2)
print((D))


