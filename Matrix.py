
import numpy as np

T = np.array([[1, 0],
              [0, 1]])

C = np.array([[1, 2],
             [0, 1]])


Cinv = np.linalg.inv(C)

# print(T.diagonal())
# print(Cinv)

# D = Cinv@T@C
# D = np.round(D , decimals = 2)
# print((D))


# print(T@T@T@T@T)


D = C@T@Cinv
D = np.round(D , decimals = 2)
print((D))