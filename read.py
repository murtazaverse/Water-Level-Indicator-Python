import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

fig = plt.figure()
def animate(i):
    pullData = open(&quot;text.txt&quot;,&quot;r&quot;).read()
    dataArray = pullData.split(&#39;\n&#39;)
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)&gt;1:
            x,y = eachLine.split(&#39;,&#39;)
            xar.append(float(x))
            yar.append(float(y))
    
    mur=plt.plot(xar,yar)
    
    y_corr=np.correlate(yar,yar,mode=&#39;full&#39;)
    
    plt.subplot(2,1,1)
    plt.stem(xar,yar)
    plt.title(&#39;Actual Graph&#39;)
    
    plt.subplot(2,1,2)
    plt.stem(y_corr,maxlags=11)
    plt.title(&#39;Correlated Distance&#39;)
ani = animation.FuncAnimation(fig, animate,
interval=1000)
plt.show()