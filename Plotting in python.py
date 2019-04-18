import matplotlib
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline  

fig = plt.figure(figsize=(20,15))            # changing size of the figure 
plt.plot(Y_data_array_test, '*r')
plt.plot(result, 'ob')
plt.show()


###############################################################
# Theroshold bar chart 


import numpy as np
import matplotlib.pyplot as plt

# some example data
threshold = 43.0
values = np.array([30., 87.3, 99.9, 3.33, 50.0])
x = range(len(values))

# split it up
above_threshold = np.maximum(values - threshold, 0)
below_threshold = np.minimum(values, threshold)

# and plot it
fig, ax = plt.subplots()
ax.bar(x, below_threshold, 0.35, color="g")
ax.bar(x, above_threshold, 0.35, color="r",
        bottom=below_threshold)

# horizontal line indicating the threshold
ax.plot([0., 4.5], [threshold, threshold], "k--")

fig.savefig("look-ma_a-threshold-plot.png")

###############################################################

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(20,15))

plt.axhline(y=3.02, color='r', linestyle='-')
ax.plot(Y_data_array)
plt.show( )

###############################################################







