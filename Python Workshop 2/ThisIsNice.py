# Calculate the position as a function of time for a driven harmonic oscillator
from matplotlib import pyplot as plt
import numpy as np

ti = 0
tf = 10.0                      # Use 15.0, not 15 to tell Python what kind of variable to use for the time
NumPts = 5000
dt = (tf - ti)/NumPts          # Time step

xi = 2              # Starting x-position (m)
vxi = 20            # Starting x-component of velocity (m/s)
yi = 20
vyi=49
mass = 1            # Object mass
gg = -9.8           # Gravitational acceleration at surface of Earth

time = [ti]                     # Begin a list which will contain the values of time from ti to tf
xx = [xi]                       # Begin a list which will contain the values of x from ti to tf
vvx = [vxi]   
yy=[yi]
vvy=[vyi]                  # Begin a list which will contain the values of vx from ti to tf

for i in range(NumPts - 1):
    Fgrav_x = 0                 # No acceleration along the x-direction
    accx = Fgrav_x/mass         # Acceleration along x is is net force along x divided by mass
    
    newtime = time[i] + dt      # Find the next time
    time.append(newtime)        # Add the next time to the list of time values

    dx = vvx[i]*dt              # Calculate how far the object moves along x in the short time interval between time[i] and time [i+1]
    newx = xx[i] + dx           # Find the new position by adding dx to the present position 
    dvx = accx*dt               # Calculate how much vx changes between time[i] and time [i+1]
    newvx = vvx[i] + dvx        # Find the new vx by adding dvx to the present vx
    
    dy = vvy[i]*dt              # Calculate how far the object moves along y in the short time interval between time[i] and time [i+1]
    newy = yy[i] + dy           # Find the new position by adding dx to the present position 
    dvy = gg*dt                 # Calculate how much vy changes between time[i] and time [i+1]
    newvy = vvy[i] + dvy        # Find the new vy by adding dvy to the present vy

    xx.append(newx)             # Add the next x-position to the list of x-position values
    vvx.append(newvx)           # Add the next x-velocity to the list of x-velocity values
    
    yy.append(newy)             # Add the next x-position to the list of x-position values
    vvy.append(newvy)           # Add the next x-velocity to the list of x-velocity values


fig1 = plt.figure()
plt.plot(xx,yy,'r.')

plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
fig1.savefig('2DNewtonII.jpg')

