def change(x):
    x+=3
    return x

import numpy as np
x=np.array([1,2,3,4])

[1 2 3 4]
[4 5 6 7]

###############################################################

# Shift elements in a numpy array
def shift(xs, n):
    if n >= 0:
        return np.r_[np.full(n, np.nan), xs[:-n]]
    else:
        return np.r_[xs[-n:], np.full(-n, np.nan)]


###############################################################   

def last(a_list):
    return a_list[-1]

###############################################################

def list_test2 (L):
    if not L      : print 'list is empty'
    else: print 'list has %d elements' % len(L)
        
###############################################################

