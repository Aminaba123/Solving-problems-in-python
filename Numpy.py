# style for reshaping

scores_mean = np.array(scores_mean).reshape(len(grid_param_2),len(grid_param_1))

##################################################################################

# numpy to list

a = np.array([1, 2])
a.tolist()
[1, 2]
a = np.array([[1, 2], [3, 4]])
list(a)
[array([1, 2]), array([3, 4])]
a.tolist()
[[1, 2], [3, 4]]

##################################################################################
#1) Make an array of arrays:

x=[[1,2],[1,2,3],[1]]
y=numpy.array([numpy.array(xi) for xi in x])

#2) Make an array of lists:

x=[[1,2],[1,2,3],[1]]
y=numpy.array(x)

# As this is the top search on Google for converting a list of lists into a Numpy array,
# I'll offer the following despite the question being 4 years old

x = [[1, 2], [1, 2, 3], [1]]
y = numpy.hstack(x)

##################################################################################

# To get a NumPy array, you should use the values attribute:



##################################################################################
# Stack to array together 

x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
X = np.vstack((x, y)).T


EX: 
  
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
np.vstack((a,b))
array([[1, 2, 3],
       [2, 3, 4]])
##################################################################################
# drop element 

import numpy as np
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 3, 4]
print("Original array:")
print(x)
print("Delete first, fourth and fifth elements:")
new_x = np.delete(x, index)
print(new_x)

##################################################################################

# In order to create the concatenation and work around the error, I initialized the array with None and 
# tested if it is None in the loop. Thereby you do not have to worry about not fitting dimensions. 
# However, i created some arrays for the ones you did only describe and ended up with a final 
# dimesion of (400, 30, 30, 3). This fits in here, since 20*20 = 400. Hope this helps for you 
new_one_arr1_list = []
new_one_arr2_list = []
one_arr1 = np.ones((20,30,30,3))
one_arr2 = np.ones((20,30,30,3))
all_arr1 = None
count = 0
for item in one_arr1: # 100 iterations
    item = np.reshape(item, (1, 30, 30, 3))
    new_one_arr1 = np.repeat(item, 20, axis=0)

    # print(all_arr1.shape, new_one_arr1.shape)
    if all_arr1 is None:
        all_arr1 = new_one_arr1
    else:
        all_arr1 = np.concatenate(([all_arr1 , new_one_arr1 ]), axis=0)
    ind = np.random.randint(one_arr2.shape[0], size=(20,))
    new_one_arr2= one_arr1[ind]

    new_one_arr1_list.append(new_one_arr1)
    new_one_arr2_list.append(new_one_arr2)
    count += 1
print(count)
all_arr1.shape

##################################################################################à


