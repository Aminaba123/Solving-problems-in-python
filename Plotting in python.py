import matplotlib
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline  

fig = plt.figure(figsize=(20,15))            # changing size of the figure 
plt.plot(Y_data_array_test, '*r')
plt.plot(result, 'ob')
plt.show()
