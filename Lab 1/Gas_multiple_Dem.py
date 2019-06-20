#So I've gone through and deleted all my comments and plots, I've also moved
#importing modules to the top, I'll quickly print v again just to check its
#still all going.

V=2.03*10**-3
A=5.55113*10**-8
ef_begin=0.26

import numpy as np
from matplotlib import pyplot as plt
from math import log
import math

#What we are going to do here is run a for loop over all the code we wrote
#for all files in a specific folder. This will be the folder we are in, so
#to start we need to import
#The module we a re going to use.

#os (or Miscellaneous Operating system interfaces) Lets us look up file
#paths and floder locations

#Glob lets us find all files matching a pattern
#Simply these are file organisation tools

import os
import glob

#The first thing we want to do is set the location of our folder which is
#where the script is stored i.e. CWD or current working directory

folder = os.getcwd()

#now we know where the files are stored we need to set the pattern
#(or type of files) for Glob to look for

fileformat=folder+str('/*.csv')

#This will make the script only look for csv files in the correct folder

#we now want to create an array of the filenames, these are nameed after the
#gasses and mass numbers

files = glob.glob(fileformat)

#Create an array of masses from filenames to use later, as filenames are
#strings we need to set them as intergers
#(-ve indicies run from the end)

masses = [int(f[-6:-4]) for f in files]

#lets print this list of files to check its working

#################################################print(files)

#we now need to find out how many files we have in the folder

n=len(files)

# we also need to create an empty array to populate later

v=np.zeros(n)

#we now want to simply run though the previous code for all files in the folder

for j in range(n):

    #we need to indent all this code and change the argument in genfromtext
    #to files[j]

    rawdata=np.genfromtxt(files[j], delimiter=',')
    time=rawdata[:,0]
    pressure=rawdata[:,1]
    baseP=min(rawdata[:,1])
    P_minus_baseP=[i-0.99*baseP for i in pressure]
    res=[abs(i-ef_begin) for i in P_minus_baseP]
    minres=min(res)
    for i in range (len(res)):
        if res[i]==minres:
            Peff_index=i
            break
    LogP=[log(i) for i in P_minus_baseP]
    fit=np.polyfit(time[Peff_index:1400],LogP[Peff_index:1400],1)
    m=fit[0]
    c=fit[1]


    #now we put each of these in one of the spots in the vector v

    v[j]=-4*V*m/A


#now lets print v

######################print(v)

#we can then plot v as a function of mass number

plt.scatter(masses,v)

#we can now create a theoritical line to match these to

#first we need a range of mass numbers



#now we simply complete the theoritical calculation

vtheory=[math.sqrt(8/math.pi*1.38*(10**-23)*300/i/(1.67*10**-27)) for i in range(10,90)]

#and plot the result on our plot

plt.plot(range(10,90),vtheory,'k--')

#we can add some labels

plt.xlabel('Mass Number')
plt.ylabel('Velocity')
