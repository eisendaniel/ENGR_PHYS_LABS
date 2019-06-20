from matplotlib import pyplot as plt


ti = 0.0                   # s
tf = 15.0                   # s
numPts = 1000
dt = (tf - ti) / numPts

xi = 500.0                      # m
vi = 0                    # m/s
m = 5*(10**-4)              # kg
d = 2*(10**-5)              # kg/m
g = -9.8

Fg = m * g                  # N

terminalV = -15.7            # m/s
ansPrinted = False


time = [ti]
xPos = [xi]
vel = [vi]

for i in range(numPts - 1):
    Fd = d * vel[i]**2
    acc = (Fd + Fg) / m

    newTime = time[i] + dt
    time.append(newTime)
    newX = xPos[i] + vel[i]*dt
    xPos.append(newX)
    newV = vel[i] + acc*dt
    vel.append(newV)

    if (newV < .95 * terminalV) and (ansPrinted == False) :
        print("It took {} s for the hailstones V to reach ~95% terminal".format(time[i]))
        print("The hailstone fell {} m before it's  ~95% terminal V".format(xPos[i+1]))
        ansPrinted = True


# plots displacment vs time
plt.plot(time, xPos)
plt.xlabel("Time (s)")
plt.ylabel("displacment (m)")
plt.show()

# plots velocity vs time
plt.plot(time, vel)
plt.xlabel("Time (s)")
plt.ylabel("velocity (m/s)")
plt.show()
