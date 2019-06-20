
from matplotlib import pyplot as plt

ti = 0
tf = 15.0                       # Use 15.0, not 15 to tell Python what kind of variable to use for the time
NumPts = 1000
dt = (tf - ti)/NumPts           # Time step

xi = 500                        # Starting height
vi = 0                          # Starting velocity
gg = -9.8                       # Gravitational acceleration
eta = 2*10**-5
mass = 5*10**-4

time = [ti]                     # Begin a list which will contain the values of time from ti to tf
xx = [xi]                       # Begin a list which will contain the values of position from ti to tf
vv = [vi]                       # Begin a list which will contain the values of velocity from ti to tf

for i in range(NumPts - 1):
    # Change the following lines to treat a problem with different forces, e.g., add a spring force Fspr = -k*xx[i]
    Fdrag = eta*vv[i]**2        # Drag force is proportional to velocity squared
    Fgrav = mass*gg             # Gravitational force
    acc = (Fdrag + Fgrav)/mass  # Acceleration is net force divided by mass

    # The next lines can be used without alteration for any type of force
    newtime = time[i] + dt      # Find the next time
    time.append(newtime)        # Add the next time to the list of time values
    dx = vv[i]*dt               # Calculate how far the object moves in the short time interval between time[i] and time [i+1]
    newx = xx[i] + dx           # Find the new position by adding dx to the present position
    dv = acc*dt                 # Calculate how much the velocity changes between time[i] and time [i+1]
    newv = vv[i] + dv           # Find the new velocity by adding dv to the present velocity
    xx.append(newx)             # Add the next position to the list of position values
    vv.append(newv)             # Add the next velocity to the list of velocity values

plt.plot(time,xx)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

plt.plot(time,vv)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()
