# Calculate the position as a function of time for a driven harmonic oscillator
from matplotlib import pyplot as plt
import numpy as np

ti = 0
tf = 20.1                      # Use 15.0, not 15 to tell Python what kind of variable to use for the time
NumPts = 5000
dt = (tf - ti)/NumPts          # Time step

xi = 0              # Starting x-position (m)
vxi = 9.8            # Starting x-component of velocity (m/s)
yi = 20
vyi = 98
mass = 1            # Object mass
gg = -9.8           # Gravitational acceleration at surface of Earth

time = [ti]                     # Begin a list which will contain the values of time from ti to tf
xx = [xi]                       # Begin a list which will contain the values of x from ti to tf
vvx = [vxi]                     # Begin a list which will contain the values of vx from ti to tf
yy = [yi]
vvy = [vyi]

for i in range(NumPts - 1):
    Fgrav_x = 0                 # No acceleration along the x-direction
    accx = Fgrav_x/mass         # Acceleration along x is is net force along x divided by mass
    
    Fgrav_y = gg
    accy = Fgrav_y/mass
    
    newtime = time[i] + dt      # Find the next time
    time.append(newtime)        # Add the next time to the list of time values

    dx = vvx[i]*dt              # Calculate how far the object moves along x in the short time interval between time[i] and time [i+1]
    newx = xx[i] + dx           # Find the new position by adding dx to the present position 
    dvx = accx*dt               # Calculate how much vx changes between time[i] and time [i+1]
    newvx = vvx[i] + dvx        # Find the new vx by adding dvx to the present vx
    
    dy = vvy[i]*dt
    newy = yy[i] + dy
    dvy = accy*dt
    newvy = vvy[i] + dvy

    xx.append(newx)             # Add the next x-position to the list of x-position values
    vvx.append(newvx)           # Add the next x-velocity to the list of x-velocity values
    yy.append(newy)
    vvy.append(newvy)


fig1 = plt.figure()
plt.plot(xx,yy,'r.')

plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
fig1.savefig('2DNewtonII.jpg')

