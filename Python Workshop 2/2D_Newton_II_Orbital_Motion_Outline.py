# Calculate the position as a function of time for a driven harmonic oscillator
from matplotlib import pyplot as plt
import numpy as np
import math

ti = 0
tf = 120000.0                      # Use 15.0, not 15 to tell Python what kind of variable to use for the time
NumPts = 85000
dt = (tf - ti)/NumPts          # Time step

mass = 1            # Object mass
EarthMass = 6E24    # Mass of the Earth
GG = 6.7E-11        # Gravitational constant
Earth_R = 6E6       # Approximate radius of Earth

xi = 0                         # Starting x-position (m)
yi = 7.1E6                         # Starting y-position (m)
vxi = 0                       # Starting x-component of velocity (m/s)
vyi = 0                       # Starting y-component of velocity (m/s)

# Now do a numerical approximation to the solution


def orbit(n):
    time = [ti]                     # Begin a list which will contain the values of time from ti to tf
    xx = [xi]                       # Begin a list which will contain the values of x from ti to tf
    yy = [yi]                       # Begin a list which will contain the values of y from ti to tf
    vvx = [n]                     # Begin a list which will contain the values of vx from ti to tf
    vvy = [vyi]                     # Begin a list which will contain the values of vy from ti to tf

    for i in range(NumPts - 1):
        # Calculate the x- and y-components of the gravitational force...
        r = math.sqrt(xx[i]**2 + yy[i]**2)
        if (r <= Earth_R):
            break

        Fgrav = (GG*EarthMass*mass) / r**2

        theta = math.atan2(yy[i],xx[i])
        Fgrav_x = Fgrav*math.cos(theta)
        Fgrav_y = Fgrav*math.sin(theta)

        accx = -Fgrav_x/mass # Acceleration along x is is net force along x divided by mass
        accy = -Fgrav_y/mass # Acceleration along y is is net force along y divided by mass

        newtime = time[i] + dt      # Find the next time
        time.append(newtime)        # Add the next time to the list of time values

        dx = vvx[i]*dt              # Calculate how far the object moves along x in the short time interval between time[i] and time [i+1]
        newx = xx[i] + dx           # Find the new position by adding dx to the present position
        dvx = accx*dt               # Calculate how much vx changes between time[i] and time [i+1]
        newvx = vvx[i] + dvx        # Find the new vx by adding dvx to the present vx

        dy = vvy[i]*dt              # Calculate how far the object moves along y in the short time interval between time[i] and time [i+1]
        newy = yy[i] + dy           # Find the new position by adding dy to the present position
        dvy = accy*dt               # Calculate how much vy changes between time[i] and time [i+1]
        newvy = vvy[i] + dvy        # Find the new vy by adding dvy to the present vy

        xx.append(newx)             # Add the next x-position to the list of x-position values
        yy.append(newy)             # Add the next y-position to the list of y-position values
        vvx.append(newvx)           # Add the next x-velocity to the list of x-velocity values
        vvy.append(newvy)           # Add the next y-velocity to the list of y-velocity values


    plt.plot(xx,yy,markersize=2)


orbit(10000)

# # Calculate the angular momentum to see if it's conserved (this is a test of whether the numerical code is accurate)
# Lz = mass*(np.multiply(xx,vvy) - np.multiply(yy,vvx))
# fig2 = plt.figure()
# plt.plot(time,Lz)
# plt.xlabel('Time (s)')
# plt.ylabel('Ang. mtm (kg m/s)')

xE = np.linspace(-Earth_R,Earth_R,500)
yE = np.sqrt(Earth_R**2 - xE**2)
plt.fill(xE,yE,'b-')
plt.fill(xE,-yE,'b-')
plt.axis('equal')

plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
# fig1 = plt.figure()
# fig1.savefig('2DNewtonII.png')
plt.show()
