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

##################################################################################




