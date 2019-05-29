%matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt
import time

def pltsin(ax, colors=['b']):
    x = np.linspace(0,1,100)
    if ax.lines:
        for line in ax.lines:
            line.set_xdata(x)
            y = np.random.random(size=(100,1))
            line.set_ydata(y)
    else:
        for color in colors:
            y = np.random.random(size=(100,1))
            ax.plot(x, y, color)
    fig.canvas.draw()

fig,ax = plt.subplots(1,1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
for f in range(5):
    pltsin(ax, ['b', 'r'])
    time.sleep(1)
    
    
###################################################################################

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2) 
plt.close('all')

for i in range (0,3):
    y  = y + np.pi/2
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
    ax1.plot(x, y)     
    ax1.set_title('Title: i=%s' % (i))
    ax1.set_xlabel('X_plot1 title')
    ax1.set_ylabel('Y_plot1 title')    
    ax1.set_xlim ([0.0, 5])
    ax1.set_ylim ([0.0, 6])
    ax2.scatter(x, y)    
    ax2.set_xlabel('Y_plot2 title') 
    ax2.set_ylabel('X_plot2 title')
    plt.show()

###################################################################################

%matplotlib inline
import time
import pylab as pl
from IPython import display
for i in range(10):
    pl.plot(pl.randn(100))
    display.clear_output(wait=True)
    display.display(pl.gcf())
    time.sleep(1.0)

###################################################################################

import numpy as np
import matplotlib.pyplot as plt
import pylab 
fig = plt.figure(figsize=(20,15))
pylab.grid(True)

a = f_mean[0:2184]*250
b = yy[0:2184]*250

pylab.plot(a[a>100]  , '-r', label= 'Predicted Values' )
pylab.ylim([250,500])
pylab.plot(b[b>100]  , '-b', label= 'Actual Values' )
pylab.xlim([2160,2184])

#pylab.plot(f_mean*250 , '-r', label='Predictive values (Testing from zero to i+24)')
#plt.axhline(y=2.9*250, color='r', linestyle='-')
#  to change the font of axis\n",

pylab.title('Predicted Vs Actual values in GPR \n Enterprise\Duct1',fontsize=28)
pylab.ylabel('Pressure drop (Pascal)',fontsize=28)
pylab.xlabel('Samples \n Number of Predicted samples : 24 \n Number of observed samples : 2160',fontsize=28)
pylab.legend(loc='bottom left',fontsize=22)

#  to change the font of axis \n",

pylab.tick_params(axis = 'both', which = 'major', labelsize = 22)
pylab.tick_params(axis = 'both', which = 'minor', labelsize = 22)

###################################################################################

import numpy as np
import matplotlib.pyplot as plt
import pylab 
fig = plt.figure(figsize=(20,15))
pylab.grid(True)

#a = s
#b = yy[0:2184]*250

pylab.plot(s  , '-r', label= 'Accumulative Dust' )

pylab.title('Accumulative Dust over time in Enterprise Dataset ',fontsize=28)
pylab.ylabel('Accumulative Dust',fontsize=28)
pylab.xlabel('Time',fontsize=28)
pylab.legend(loc='bottom left',fontsize=22)

#  to change the font of axis \n",

pylab.tick_params(axis = 'both', which = 'major', labelsize = 22)
pylab.tick_params(axis = 'both', which = 'minor', labelsize = 22)


###################################################################################

import numpy as np
import matplotlib.pyplot as plt
import pylab 
fig = plt.figure(figsize=(20,15))
pylab.grid(True)

#a = s
#b = yy[0:2184]*250



pylab.plot(T1_0   , '-r', label= 'Humidity' )

pylab.title('Dati_SEGRETISSIMI Dataset ',fontsize=28)
pylab.ylabel('Temperature ',fontsize=28)
pylab.xlabel('Time',fontsize=28)
pylab.legend(loc='bottom left',fontsize=22)

#  to change the font of axis \n",

pylab.tick_params(axis = 'both', which = 'major', labelsize = 22)
pylab.tick_params(axis = 'both', which = 'minor', labelsize = 22)

###################################################################################





