a=1.602**2

A = [0,1,2,3,4,5,6,7,8,9,10]
n = len(A)

B = [A[i]+3 for i in range(n)]

from matplotlib import pyplot as plt
plt.plot(A,B)
plt.ylabel("an axis")

plt.show()
