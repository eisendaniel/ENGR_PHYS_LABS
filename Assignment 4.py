from matplotlib import pyplot as plt
import math

ti = 0.0                     # s
tf = 12.0                    # s
numPts = 10000
dt = (tf - ti) / numPts

m = 1.0                      # kg
A = 2                      # m
b = 0.4                     # kg/s
k = 4                      # N/m
a = b/2*m
w = math.sqrt( (k/m) - (b**2 / 4*m**2) ) # rad/s

xi = 0                   # m
# vi = 0

phi = math.acos(xi/A)                      # rad
vi = -2*a*math.exp(-a*ti)*math.cos(w*ti+phi) - 2*math.exp(-a*ti)*w*math.sin(w*ti+phi) # m/s
print(vi)

def compute(b):

    time = [ti]
    xPos = [xi]
    vel = [vi]
    for i in range(numPts - 1):
        Fd = b * vel[i]                 # Calculating the force of drag
        Fk = -k * xPos[i]               # Calculating the force, according to hooks law
        Ft = Fk - Fd                    # Summing total force
        acc = Ft/m                      # Calculating acceleration

        newTime = time[i] + dt
        time.append(newTime)
        newX = xPos[i] + vel[i]*dt
        xPos.append(newX)
        newV = vel[i] + acc*dt
        vel.append(newV)
    # plots displacment vs time
    plt.plot(time, xPos)

compute(0.4)


plt.xlabel("Time (s)")
plt.ylabel("displacment (m)")

plt.show()
