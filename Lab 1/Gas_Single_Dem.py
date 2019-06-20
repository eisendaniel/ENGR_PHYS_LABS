#the first thing we want to do is define some constants that we will use later
#on. These will be the Volume of the bulb
#the area of the opening and the pressure at which the effusion regime begins.

##Remember that I can 'comment out' code by using the # so the program won't
#try to run it. As you read through you'll see lots of print commands commented
#out, these were included to check the code was working.

V=2.03*10**-3
A=5.55113*10**-8
ef_begin=0.26

#So first we want to load up the data that we have in our CSVs if you remember
#back to the experiment the data is pressure as a function of time.
#To do this we use a package called numpy, so let import that

import numpy as np

#Now we want to use numpy to import our data, the command we are going to use
#is called genfram text. We will import the data into a varible, called rawdata:


rawdata=np.genfromtxt('Nitrogen 28_2.csv', delimiter='cat')
#note that the delimiter argument tells Python how the data is sepperated

#now lets print our data to check its all working, we should get two columns,
#one time one pressure

######################################print(rawdata)

#we now want tot split this array up into two vectors, one for time and one
#for pressure, we can do that using the indexing we learned before

time=rawdata[:,0]
pressure=rawdata[:,1]

#lets print these too to check everything is working then run the code

######################################print(time)
######################################print(pressure)

#now lets plot them, first we need to import the plotting module


from matplotlib import pyplot as plt

# we will have multiple figures so lets designate this as figure 1

######################################plt.figure(1)

#now we can plot pressure as a function of time

######################################plt.plot(time,pressure)

#now if you remember the experiment we needed to subtract the base pressure
#(the lowest pressure reached) from each value in the pressure column
#(or vector)
# first we need to find the minium pressure and save that as a varible, to do
#that we sue the min function

baseP=min(rawdata[:,1])

#again lets print the result

#####################################print(baseP)

# we are now going to use a list comprehension to subtract the base pressure
#from each value in raw data as I'm going to take the log of this later I want
#to aviod 0 values, and as baseP is in raw data it will return a zero, so
#I'll just multiply it by 0.99 to aviod this

P_minus_baseP=[i-0.99*baseP for i in pressure]

#now again I'll print the result

#################################print(P_minus_baseP)

#Now we have our pressure minus base pressure we need to find the point at
#which the effusion reigme begins, to do this we are going to
#make a new vector of residuals. We already know the pressure at which the
#effusion regime begins, we called it ef_begin, what we don't know is the
#INDEX of
#this value in the pressure vector. We are going to find this using residuals.
#This will be a vector where we take ef_begin from all values of the pressure
#vector
# the smallest value of this vector will have an index equal to that of when
#the effusion regime begins.

res=[abs(i-ef_begin) for i in P_minus_baseP]

#we now want to find the minium value in this vector

minres=min(res)

#lets rpint res and minres to check everything worked

######################################print(res)
######################################print(minres)

#we now need to find the index of the minium value, for this we will use a for
# loop, we want the loop to run for as many entries as we ahve in res
# so we can make it run for len(res)
# we then want to use an if statment, so when res[i]=minres we assign that i
#to a varible, then stop.

for i in range (len(res)):
    if res[i]==minres:
        Peff_index=i
        break

#lets print this index varible to check it worked

######################################print(Peff_index)

#now we ahev the value fo the index where the effusion regime begins we can
#move on.
#The next step is to take the log of our data, to do this we need to import
#another module called math

from math import log
import math

#we are going to use another list comprehension to log create a new vector
#with all the logged values

LogP=[log(i) for i in P_minus_baseP]

#again lets print the result

############print(logP)

#now we have logged our data we can plot it as a function of time, to do
#this we will import the matplotlib module

#lets call this figure 2
plt.figure(2)
plt.plot(time,LogP)

#we can also plot only the data after we reach the effusion regime

plt.plot(time[Peff_index:],LogP[Peff_index:],'r')

#Now I want to fit a trendline to the section of the data in the effusion
#regime. To do this I'll use a fitting tool and create a new varible

fit=np.polyfit(time[Peff_index:1400],LogP[Peff_index:1400],1)

#Now I'll print this

####################################print(fit[0])

#the fit function returns two values, one is the gradient and one is the
#intercept, we can make these into their own varible

m=fit[0]
c=fit[1]

#now we can add this to the plot

plt.plot(time[Peff_index:1400],time[Peff_index:1400]*m+c,'k--')

#we now can calculate the velocity from the fit, and print it

v=-4*V*m/A
print(v)

plt.show()
