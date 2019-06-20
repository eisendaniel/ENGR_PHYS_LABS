# Calculate the position as a function of time for a driven harmonic oscillator
from matplotlib import pyplot as plt
import numpy as np

ti = 0
tf = 120000.0                      # Use 15.0, not 15 to tell Python what kind of variable to use for the time
NumPts = 850000
dt = (tf - ti)/NumPts          # Time step

xi = 0                         # Starting x-position (m)
yi = 4.2081E7                         # Starting y-position (m)
vxi = 3100                        # Starting x-component of velocity (m/s)
vyi = 0                       # Starting y-component of velocity (m/s)

#Moon added by Max
#xmoon = 7E7
#ymoon = 0
#Moonmass = 8E30

mass = 1            # Object mass
EarthMass = 6E24    # Mass of the Earth
GG = 6.7E-11        # Gravitational constant
Earth_R = 6E6       # Approximate radius of Earth

# Now do a numerical approximation to the solution
time = [ti]                     # Begin a list which will contain the values of time from ti to tf
xx = [xi]                       # Begin a list which will contain the values of x from ti to tf
yy = [yi]                       # Begin a list which will contain the values of y from ti to tf
vvx = [vxi]                     # Begin a list which will contain the values of vx from ti to tf
vvy = [vyi]                     # Begin a list which will contain the values of vy from ti to tf

for i in range(NumPts - 1):
    # Calculate the x- and y-components of the gravitational force...(including Moon)
    Fgrav = -GG*EarthMass*mass/((yy[i]**2)+(xx[i]**2)) 
    theta = np.arctan2(yy[i], xx[i])
    
    #Fgravm = -GG*massm*mass/((ym-yy[i])**2+(xm-xx[i])**2) Moon stuff
    #thetam = np.arctan2((yy[i]-ym), xx[i]-xm) Moon stuff
    
    Fgrav_x = Fgrav * np.cos(theta) #+ Fgravm*np.cos(thetam)      Moon stuff             
    Fgrav_y = Fgrav * np.sin(theta) #+ Fgravm*np.sin(thetam)      Moon stuff            
    
    
    
    
    accx = Fgrav_x/mass # Acceleration along x is is net force along x divided by mass
    accy = Fgrav_y/mass # Acceleration along y is is net force along y divided by mass
    
    if i > 2:
        if (yy[i-1] > yy[i]) & (yy[i-1] > yy[i-2]):
            print(dt*(i-1))
    
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
    
    if np.sqrt(yy[i]**2+xx[i]**2) < Earth_R:
        print("Broken")
        break
    
    if ((i+1)%50000==0):
        L=mass*(xx[i]*vvy[i] - yy[i]*vvx[i])
        print(L)
    
    xx.append(newx)             # Add the next x-position to the list of x-position values
    yy.append(newy)             # Add the next y-position to the list of y-position values
    vvx.append(newvx)           # Add the next x-velocity to the list of x-velocity values
    vvy.append(newvy)           # Add the next y-velocity to the list of y-velocity values

xE = np.linspace(-Earth_R,Earth_R,500)
yE = np.sqrt(Earth_R**2 - xE**2)


fig1 = plt.figure()
plt.plot(xx,yy,'r.',markersize=2)
plt.fill(xE,yE,'b-')
plt.fill(xE,-yE,'b-')
plt.axis('equal')

plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
fig1.savefig('2DNewtonII.jpg')

# Calculate the angular momentum to see if it's conserved (this is a test of whether the numerical code is accurate)
Lz = mass*(np.multiply(xx,vvy) - np.multiply(yy,vvx))
fig2 = plt.figure()
plot(time,Lz)
plt.xlabel('Time (s)')
plt.ylabel('Ang. mtm (kg m/s)')
