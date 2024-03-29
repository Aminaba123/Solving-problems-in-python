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

def rotate(self, matrix):
        """
        rotate matrix n*n
        1. flip along the diagonal
        2. flip along x-axis
        :param matrix: a list of lists of integers
        :return: a list of lists of integers
        """
        n = len(matrix)
        for row in range(n):
            for col in range(n-row):
                matrix[row][col], matrix[n-1-col][n-1-row] = matrix[n-1-col][n-1-row], matrix[row][col]  # by diagonal
        for row in range(n/2):
            for col in range(n):
                matrix[row][col], matrix[n-1-row][col] = matrix[n-1-row][col], matrix[row][col]  # by x-axis

        return matrix

###############################################################

def sortColors(self, A):
        """
        Algorithm: pivoting. Similar concept as QuickSort
        constant space
        [W, R, B]
        :param A: a list of integers
        :return: nothing, sort in place
        """
        RED, WHITE, BLUE = 0, 1, 2
        red_end_ptr = -1
        blue_start_ptr= len(A)

        i = 0
        while i<blue_start_ptr:
            if A[i]==WHITE: # pivot set
                i += 1
            elif A[i]==RED:
                red_end_ptr+=1
                A[red_end_ptr], A[i] = A[i], A[red_end_ptr]
                i += 1
            else:
                blue_start_ptr -= 1
                A[blue_start_ptr], A[i] = A[i], A[blue_start_ptr]
                # no i+=1, since you need to examine A[i] again

###############################################################

# finding square root Function

    def sqrt(self, x):
        """
        Newton's method
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \
        http://en.wikipedia.org/wiki/Newton's_method
        :param x: Integer
        :return: Integer
        """
        if x==0: return 0  # avoid Division by zero
        m = x
        while True:
            m_before = m
            m = m - float(m*m-x)/(2*m)
            if abs(m-m_before)<1e-7: break

        return int(m)

###############################################################
# search word

    def exist(self, board, word):
        """
        dfs
        :param board: a list of lists of 1 length string
        :param word: a string
        :return: boolean
        """
        if not board:
            return
        # unpack
        # board = [item[0] for item in board]

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]  # avoid loop
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j]==word[0]:
                    visited[i][j] = True
                    if self.search(board, i, j, word[1:], visited):
                        return True
                    visited[i][j] = False
        return False

    def search(self, board, pre_row, pre_col, word, visited):
        if not word:
            return True
        # searching for word[0]
        m = len(board)
        n = len(board[0])
        next_positions = [(pre_row-1, pre_col), (pre_row+1, pre_col), (pre_row, pre_col-1), (pre_row, pre_col+1)]  # four directions
        for next_position in next_positions:
            if 0<=next_position[0]<m and 0<=next_position[1]<n:  # pre-checking
                if visited[next_position[0]][next_position[1]]==False and board[next_position[0]][next_position[1]]==word[0]:
                    visited[next_position[0]][next_position[1]] = True
                    if self.search(board, next_position[0], next_position[1], word[1:], visited):
                        return True
                    visited[next_position[0]][next_position[1]] = False  # restore
        return False

###############################################################

def data_to_plotly(x):
    k = []
    
    for i in range(0, len(x)):
        k.append(x[i][0])
        
    return k
###############################################################
def f(x):
    """The function to predict."""
    return x * np.sin(x)

###############################################################

#  skip the first line of the file and I'm not sure if I'm returning it as a dictionary
#  Reading csv file and returning as dictionary

# First thing we do is delete the first line of the list.

# Then we run a function to do exactly as you say, make a dictionary with list of tuples as values.

# You can keep the function you have and run this operation on the lines variable.

# Alright run the following code and you should be good

def convertLines(lines):
    head = lines[0]
    del lines[0]
    infoDict = {}
    for line in lines: #Going through everything but the first line
        infoDict[line.split(",")[0]] = [tuple(line.split(",")[1:])]
    return infoDict

def read_file(filename):
    thefile = open(filename, "r")
    lines = []
    for i in thefile:
        lines.append(i)
    thefile.close()
    return lines

mydict = convertLines(read_file(filename))
print(mydict)       

###############################################################

# Codes for linear regresion 

def predict_sales(radio, weight, bias):
    return weight*radio + bias

# What we need is a cost function so we can start optimizing our weights

###############################################################

x = 2
def f(a):
    x = a * a
    return x

y = f(3)
print(x,y)

###############################################################

# What will be the output of the following program?

x = 1
def f():
    y = x
    x = 2
    return x + y


print(x)
print(f())
print(x)

UnboundLocalError: local variable 'x' referenced before assignment

###############################################################

# Write a function count_digits to find number of digits in the given number.

def count_digits(n):
    return len(str(n))

print(count_digits(345))

###############################################################
def squareRoot(a):
    x = 2
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y 
    return y
###############################################################
my_str = input("Input a string: ")
index_int = 0
result_str = '' # empty string
while index_int < (len(my_str) - 1): # Line 1
    if my_str[index_int] > my_str[index_int + 1]:
        result_str = result_str + my_str[index_int]
    else:
	result_str = result_str * 2
    index_int += 1 # Line 2
print(result_str) # Line 3

###############################################################

import csv

def read_file(filename, col_list):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        final_dict = { col_name: [] for col_name in col_list }

        for row in reader:
            for col_name in col_list:
                final_dict[col_name].append(row[col_name])

        print final_dict

###############################################################
	
def partition(vector, fold, k):
    size = vector.shape[0]
    start = (size/k)*fold
    end = (size/k)*(fold+1)
    validation = vector[start:end]
    if str(type(vector)) == "<class 'scipy.sparse.csr.csr_matrix'>":
        indices = range(start, end)
        mask = np.ones(vector.shape[0], dtype=bool)
        mask[indices] = False
        training = vector[mask]
    elif str(type(vector)) == "<type 'numpy.ndarray'>":
        training = np.concatenate((vector[:start], vector[end:]))
    return training, validation

###############################################################

def Sigmoid(z):
    return 1/(1 + np.exp(-z))

def Hypothesis(theta, x):   
    return Sigmoid(x @ theta)

def Cost_Function(X,Y,theta,m):
    hi = Hypothesis(theta, x)
    _y = Y.reshape(-1, 1)
    J = 1/float(m) * np.sum(-_y * np.log(hi) - (1-_y) * np.log(1-hi))
    return J

def Cost_Function_Regularisation(X,Y,theta,m,alpha):
    hi = Hypothesis(theta,X)
    _y = Y.reshape(-1, 1)
    J = alpha/float(m) * X.T @ (hi - _y)
    return J

def Cost_Function_Regularisation(X,Y,theta,m,alpha):
    hi = Hypothesis(theta,X)
    _y = Y.reshape(-1, 1)
    J = alpha/float(m) * X.T @ (hi - _y)
    return J

def Gradient_Descent(X,Y,theta,m,alpha):
    new_theta = theta - Cost_Function_Regularisation(X,Y,theta,m,alpha)
    return new_theta

def Accuracy(theta):
    correct = 0
    length = len(X_test)
    prediction = (Hypothesis(theta, X_test) > 0.5)
    _y = Y_test.reshape(-1, 1)
    correct = prediction == _y
    my_accuracy = (np.sum(correct) / length)*100
    print ('LR Accuracy CV: ', my_accuracy, "%")


def Logistic_Regression(X,Y,alpha,theta,num_iters):
    m = len(Y)
    for x in range(num_iters):
        new_theta = Gradient_Descent(X,Y,theta,m,alpha)
        theta = new_theta
        if x % 100 == 0:
            print #('theta: ', theta)    
            print #('cost: ', Cost_Function(X,Y,theta,m))
    Accuracy(theta)

###############################################################
def maps(list):
    list_integer = []
    for i in list:
        list_integer.append(len(i))
    return list_integer

###############################################################

def max_in_list(list):
    max = 0
    for i in range(len(list)-1):
        if list[i] > list [i+1] and list [i] > max:
            max = list[i]
        elif list[i+1] > max:
            max = list [i+1]
    return max

###############################################################
####   RMSE

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

###############################################################

def text_with_circle(text_obj, axis, color, border=1.5):
    # Get the box containing the text
    box1 = text_obj.get_window_extent()
    # It turned out that what you get from the box is 
    # in screen pixels, so we need to transform them 
    # to "data"-coordinates.  This is done with the 
    # transformer-function below
    transformer = axis.transData.inverted().transform
    # Now transform the corner coordinates of the box
    # to data-coordinates
    [x0, y0] = transformer([box1.x0, box1.y0])
    [x1, y1] = transformer([box1.x1, box1.y1])
    # Find the x and y center coordinate
    x_center = (x0+x1)/2.
    y_center = (y0+y1)/2.
    # Find the radius, add some extra to make a nice border around it
    r = np.max([(x1-x0)/2., (y1-y0)/2.])*border
    # Plot the a circle at the center of the text, with radius r.
    circle = Circle((x_center, y_center), r, color=color)
    # Add the circle to the axis.
    # Redraw the canvas.
    return circle 

###############################################################

# Summation 

def sumation(a):
    s= []
    t=0
    for i in (a):
        t += i
        s.append(t)
    print i, t , s

###############################################################
# Tokenizer 

def tokenize(str):
    idx = [x for x, v in enumerate(str) if v == '\"']
    if len(idx) % 2 != 0:
        idx = idx[:-1]
    memory = {}
    for i in range(0, len(idx), 2):
        val = str[idx[i]:idx[i+1]+1]
        key = "_"*(len(val)-1)+"{0}".format(i)
        memory[key] = val
        str = str.replace(memory[key], key, 1)        
    return [memory.get(token, token) for token in str.split(",")]  


###############################################################



