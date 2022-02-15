import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

fig = plt.figure()

def animate(i):
    pullData = open("text.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    
    mur=plt.plot(xar,yar)
    
    y_corr=np.correlate(yar,yar,mode='full')
    
    plt.subplot(2,1,1)
    plt.stem(xar,yar)
    plt.title('Actual Graph')
    
    plt.subplot(2,1,2)
    plt.stem(y_corr,maxlags=11)
    plt.title('Correlated Distance')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
