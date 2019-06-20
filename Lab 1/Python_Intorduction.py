#Lets learn Python

3+4

#if we want to see the result we need to print it

print(3+4)

#Printing text needs 'quote marks'

print('abc')

#assign a varible

a=1.602**2

print(a+3)

#can have creative names

newvariblewithmorecreativename=4

print(a+newvariblewithmorecreativename)

#Arrays

A=[1,2,3,4,5]

print(A)

#indexing arrays, printing entry in position [1]

print(A[1])

#printing multiple values in A

print(A[2:5])


print(A[1]+3)

#what if we want to add 3 to each value in A

#print(A+3) 

for i in range(5):
    print(i)
    
#what if we don't know how long A is?

n=len(A)

print(n)

#simple for loop

for i in range(n):
    print(i)
    
#lets add 3 to A[i]

for i in range(n):
    print(A[i]+a)

#list comprehension (for loop in one line of code)

B=[A[i]+3 for i in range(n)]

print(B)

#Import Pyplot from Matplotlib

from matplotlib import pyplot as plt

plt.plot(A,B)

#search python matlab plot label axes

plt.ylabel("an axis")

#search change colour
