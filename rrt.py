# Rapidly-Exploring Random Tree project
# run "ipython" in terminal becuase you'll forget

import time
import random
import numpy as np
import matplotlib.pyplot as plt

#domain=np.zeros([100,100],dtype=int) # creates 100x100 domain of zeros
start=(random.randint(0,99),random.randint(0,99)) # randomly creates origin
#fig=plt.figure(figsize=(100,100))
plt.plot(start[0],start[1],'rx') # plots origin

i=0
spotx=start[0]
spoty=start[1]
food=(0,0)

tree=[None]*10
foodlist=[None]*10

while i<10:

    # randomly creates point to move towards
    foodx=random.randint(0,99)
    foody=random.randint(0,99)
    deltax=start[0]-food[0]
    deltay=start[1]-food[1]

    if deltax<0:
        spotx=spotx+1
    else:
        spotx=spotx-1

    if deltay<0:
        spoty=spoty+1
    else:
        spoty=spoty-1

    print foodx, foody
    #print foody
    tree[i]=[spotx,spoty]
    foodlist[i]=(foodx,foody)

    i=i+1

#print(tree)
print(foodlist)

plt.xlim(0,100) # sets x axis range
plt.ylim(0,100) # sets y axis range
plt.grid()
#plt.plot(domain)
#plt.plot(spotx,spoty,'bx')
index=0
while index<len(foodlist):
    plt.scatter(foodlist(index),'bo')
#plt.plot(tree[:],'bx')
plt.show()
