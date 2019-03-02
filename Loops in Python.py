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






















