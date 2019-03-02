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

def fibonacci():
    myList = []
    cont = 0
    num = int(input("Please, insert a number: "))

    if num == 1:
        myList.append(1)
    elif num >= 2:
        myList.extend((1,1))
        while (num-2 != cont):
            myList.append(myList[-1]+myList[-2])
            cont+=1
    elif num <= 0:
        print("Error, number should start above 1")

    print(myList)

fibonacci()

###############################################################


MY_DIR = r"c:\facedb\orl"
# function for read in the first 20 images of ORL Dataset
# orl1.bmp to orl10.bmp belong to one person, while orl11.bmp to orl20.bmp belong to another person.

def get_training_data(myDir):
    Training_data = []
    i = 0
    for img in os.listdir(myDir):
        try:
            img_array = cv2.imread(os.path.join(myDir,img) ,cv2.IMREAD_GRAYSCALE)
            label = 0 if i<10 else 1
            Training_data.append([img_array,label])
            i = i+1
        except Exception as e:
            print('error')
            break
        if i >= 20:
            break
    return Training_data


###############################################################

def myfun(x):
    if type(x) == str:
        return len(str.split(x))

###############################################################

def solution1():
	print(a)
	N = len(a)
	for i in range(N >> 1):
		a[i],a[N-1-i]=a[N-1-i],a[i]

###############################################################


