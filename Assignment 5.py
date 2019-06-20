from matplotlib import pyplot as plt
import math

ti = 0.0                     # s
tf = 80.0                    # s
numPts = 50000
dt = (tf - ti) / numPts

m = 1.0                      # kg
A = 2                      # m
b = 0.4                     # kg/s
k = 4                      # N/m
a = b/2*m
w0 = math.sqrt(k/m)  # rad/s
wd = 3.0 #rad/s
xi = 2                   # m
vi = 0

stableA = []

def compute(b, wd):

    time = [ti]
    xPos = [xi]
    vel = [vi]
    stableX = []
    for i in range(numPts - 1):
        Fd = b * vel[i]                 # Calculating the force of drag
        Fdr = 2*math.cos(wd*time[i])    # Driving oscillating force
        Fk = -k * xPos[i]               # Calculating the force, according to hooks law
        Ft = Fdr + Fk - Fd                  # Summing total force
        acc = Ft/m                      # Calculating acceleration

        newTime = time[i] + dt
        time.append(newTime)
        newX = xPos[i] + vel[i]*dt
        xPos.append(newX)
        if newTime > 60:
            stableX.append(newX)
        newV = vel[i] + acc*dt
        vel.append(newV)

    # plots displacment vs time
    plt.plot(time, xPos)
    print("max stable dis of {:.2f} rad/s: {}".format(wd, max(stableX)))
    stableA.append(max(stableX))

# A
# compute(0.4, 2.0)
# compute(0.4, w0)

# B
ww = []

for i in range(10):
    W = i*(6/9)
    ww.append(W)
    compute(0.4, W)


plt.xlabel("Time (s)")
plt.ylabel("displacment (m)")
plt.title("Displacment of an Oscillating System")
plt.show()

plt.xlabel("Angular frequency (rad/s)")
plt.ylabel("stable Amplitude (m)")
plt.plot(ww, stableA)
plt.show()
