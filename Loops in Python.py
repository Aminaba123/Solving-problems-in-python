count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

#######################################################

var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"

#######################################################

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
#######################################################   
   
   # Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
#######################################################

# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
#######################################################      

for counter in range(1, 6):
    print counter

#can also be written like this:

numbers = range(1,6)
	for count in numbers:
	    print (count)
#######################################################

word = "computer"
   for letter in word:
      print letter       
#######################################################

a = 0		
while a < 10:	
   a = a + 1	
   print a
   
#######################################################   
while True:
    reply = raw_input('Enter text, [tpye "stop" to quit]: ')
    print reply.lower()
    if reply == 'stop':
        break   
#######################################################      
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')      
#######################################################

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
#######################################################

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

#######################################################

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')


#######################################################

# Infinite loop

while True:
    print('foo')

#######################################################
# Nested while Loops

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

#######################################################

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))
#######################################################

# One-Line while Loops
n = 5
while n > 0: n -= 1; print(n)
	
#######################################################	

# But you can’t do this:

while n > 0: n -= 1; if True: print('foo')
		
#######################################################

while len(sample) < n_sample:
		index = randrange(len(dataset))
		sample.append(dataset[index])
		
#######################################################

ratio = 0.10
for size in [1, 10, 100]:
	sample_means = list()
	for i in range(size):
		sample = subsample(dataset, ratio)
		sample_mean = mean([row[0] for row in sample])
		sample_means.append(sample_mean)
	print('Samples=%d, Estimated Mean: %.3f' % (size, mean(sample_means)))

#####################################################################################

for c in citynames:
    
    dat = crimedict[c]
   
    crimenums_city = list(dat.values())
    crime_city = 0
#####################################################################################


n = 5
while n > 0:
  print("Hello World!!")

#####################################################################################

i = 1
while i < 6:
    print(i)
    i += 1
#####################################################################################

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#####################################################################################

i = 0
while i < 6:
    i += 1 
    if i == 3:
        continue
	print(i)

#####################################################################################

import random

n = 10
ten = 10
for i in range(1, n):
    ten = ten * 10

#####################################################################################

 while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

#####################################################################################

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
#####################################################################################

n = [1, 2, 3, 4, 5]

i = 0
s = len(n)

while i < s:
    print (n[i], end=" ")
    i = i + 1

print ()

#####################################################################################

for i in range(5):
        n = 0
        if i != 1:
            n += 1
        if i == 3:
            n += 1
        if i == 4:
            n += 1
        if i != 4:
            n += 1
        if n == 3:
            print(64 + i)

#####################################################################################

    monkey = 5
    peach5th = 1
    peach = 1

    while monkey > 1:
        total = peach * 5 + 1
        if total % 4 == 0:
            monkey -= 1
            peach = total / 4
        else:
            # 从第5只猴开始算
            peach5th += 1
            peach = peach5th
            monkey = 5

    print("沙滩上最少有：%d个桃子。" % (int(peach * 5 + 1)))


#####################################################################################

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(matrix[1])

col2 = [x[1] for x in matrix]
print(col2)

col2even = [x[1] for x in matrix if x[1] % 2 == 0]
print(col2even)

#####################################################################################

or i in xrange(length):
            if A[i]!=i+1:
                return i+1
        return A[-1]+1

#####################################################################################

CSV = ""
for k,v in d.items():
    line = "{},{}\n".format(k, ",".join(v))
    CSV+=line
print CSV 

#####################################################################################

def data_to_plotly(x):
    k = []
    
    for i in range(0, len(x)):
        k.append(x[i][0])
        
    return k

#####################################################################################

import csv
reader = csv.reader(open('CamCloseM6 4V300E10.csv'))

result = {row[0]:row[1:] for row in reader if row and row[0]}
print result

#####################################################################################

import csv
reader = csv.reader(open('test.csv'))

result = {row[0]:[i for i in row[1:] if i] for row in reader if row and row[0]}
print result

#####################################################################################

number_str = input('Find the square root of integer:')
number_int = int(number_str)
guess_str = input ('initial guess:')
guess_float = float(guess_str)
tolerance_float = float(input("what tolerance:"))

original_guess_float = guess_float
count_int = 0
previous_float = 0

while abs(previous_float - guess_float) > tolerance_float:
	previous_float = guess_float
	quotient_float = number_int /guess_float
	guess_float = (quotient_float + guess_float)/2
	count_int = count_int +1 
print (number_int, guess_float)
print (count_int, tolerance_float)
print (original_guess_float )

#####################################################################################

	result = []
	num.sort()
	length = len(num)

        h = 0
        while h<length-3:
            i = h+1
            while i<length-2:
                j = i+1
                k = length-1
                while j<k:
                    lst = [num[h], num[i], num[j], num[k]]
                    summation = sum(lst)
                    if summation==target:
                        result.append(lst)
                        k -= 1
                        j += 1
                        # remove duplicate
                        while j<k and num[j]==num[j-1]:
                            j += 1
                        while j<k and num[k]==num[k+1]:
                            k -= 1
                    elif summation>target:
                        k -= 1
                    else:
                        j += 1
    
                i += 1
                # Jump, remove duplicate
                while i<length-2 and num[i]==num[i-1]:
                    i += 1
            h += 1
            # Jump, remove duplicate
            while h<length-3 and num[h]==num[h-1]:
                h += 1

        return result

#####################################################################################
total = 0
for i in range(len(l)):
    total += l[i]
    l[i] = total
#####################################################################################	
















