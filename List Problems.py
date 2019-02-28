
# Python Expression                Results                 Description

len([1, 2, 3])                         3                     Length
[1, 2, 3] + [4, 5, 6]       	[1, 2, 3, 4, 5, 6]	       Concatenation
['Hi!'] * 4	             ['Hi!', 'Hi!', 'Hi!', 'Hi!']	    Repetition
3 in [1, 2, 3]	                     True	                 Membership
for x in [1, 2, 3]: print x,       	1 2 3	                  Iteration


# Difference between append vs. extend list methods in Python?
# What's the difference between the list methods append() and extend()?
# append adds an element to a list, and extend concatenates the first list with another list (or another iterable, not necessarily a list.)
append: Appends object at the end.
x = [1, 2, 3]
x.append([4, 5])
print (x)

gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])
print (x)

gives you: [1, 2, 3, 4, 5]

##################################################################################

# How do I check if a list is empty?

if len(li) == 0:
    print('the list is empty')
    
# Using the implicit booleanness of the empty list is quite pythonic 

if not a:
  print("List is empty")
 
 ##################################################################################
 
 # How to concatenate two lists in Python?
 
listone = [1, 2, 3]
listtwo = [4, 5, 6]

You can use the + operator to combine them

mergedlist = listone + listtwo

[1,2,3,4,5,6]


##################################################################################
    
a = [[1,2,3], [4,5,6], [7,8,9]] 
[x for xs in a for x in xs]

-- [1, 2, 3, 4, 5, 6, 7, 8, 9]

map(str, (x for xs in a for x in xs))

['1', '2', '3', '4', '5', '6', '7', '8', '9']

##################################################################################

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

c = []
a = [1, 2, 3]
b = [4, 5, 6]

c += (a + b)

##################################################################################

# Finding the index of an item given a list containing it in Python

["foo", "bar", "baz"].index("bar")

--1

[i for i, e in enumerate([1, 2, 1]) if e == 1]

-- [0, 2]

for i, j in enumerate(['foo', 'bar', 'baz']):
    if j == 'bar':
        print(i)

# As a list comprehension:

[i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'bar']

##################################################################################

# Getting the last element of a list in Python

# How can I count the occurrences of a list item?

# If you only want one item's count, use the count method:
 
[1, 2, 3, 4, 1, 4, 1].count(1)
--3

dict((i,a.count(i)) for i in a)

# is really, really slow for large lists. My solution

def occurDict(items):
    d = {}
    for i in items:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
return d
####################
import time
from collections import Counter


def countElement(a):
    g = {}
    for i in a:
        if i in g: 
            g[i] +=1
        else: 
            g[i] =1
    return g
####################

a = [1,2,3,45,6,7,7,8,9,99,2,0,8,0,0,2,111,2,2]
countElement(a)
{0: 3, 1: 1, 2: 5, 3: 1, 6: 1, 7: 2, 8: 2, 9: 1, 45: 1, 99: 1, 111: 1}


a = [1,2,3,45,6,7,7,8,9,99,2,0,8,0,0,2,111,2,2,"salaa"]
countElement(a)


{0: 3,
 1: 1,
 2: 5,
 3: 1,
 6: 1,
 7: 2,
 8: 2,
 9: 1,
 45: 1,
 99: 1,
 111: 1,
 'salaa': 1}
##################################################################################
# Accessing the index in 'for' loops?

for idx, val in enumerate(ints):
    print(idx, val)

# Use enumerate to get the index with the element as you iterate:

for index, item in enumerate(items):
    print(index, item)
    
 index = 0            # Python's indexing starts at zero
for item in items:   # Python's for loops are a "for each" loop 
    print(index, item)
    index += 1   

index = 0
while index < len(items):
    print(index, items[index])
    index += 1    
    
for index in range(len(items)):
    print(index, items[index])    

 # Old fashioned way:    
    
 for ix in range(len(ints)):
    print ints[ix] 

 # List comprehension:   
    
 [ (ix, ints[ix]) for ix in range(len(ints))] 
    
    
    
    
# It's pretty simple to start it from 1 other than 0:

for index, item in enumerate(iterable, start=1):
   print index, item


for i in range(len(ints)):
   print i, ints[i]

##################################################################################

enumerate():

S = [1,30,20,30,2]
for index, elem in enumerate(S):
        print(index, elem)

##################################################################################

# How do I remove an element from a list by index in Python?

# Use del and specify the index of the element you want to delete:

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[-1]

a = ['a', 'b', 'c', 'd']
a.pop(1)

a = [1, 2, 3, 4, 5, 6]
index = 3 # Only positive index

a = a[:index] + a[index+1 :]
# a is now [1, 2, 3, 5, 6]

##############################################
a = ['a', 'b', 'c', 'd'] 

   def remove_element(list_,index_):
       clipboard = []
       for i in range(len(list_)):
           if i is not index_:
               clipboard.append(list_[i])
       return clipboard

   print(remove_element(a,2))

##################################################################################

# How to read a file line-by-line into a list?

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

with open('filename') as f:
    lines = f.readlines()

lines = [line.rstrip('\n') for line in open('filename')]

###########################################
with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
        
###########################################        
lines = tuple(open(filename, 'r'))
        

with open("myfile.txt", encoding="utf-8") as file:
       x = [l.strip() for l in file]

        
x = []
with open("myfile.txt") as file:
    for l in file:
        x.append(l.strip())        

##################################################################################
# How to clone or copy a list?

b = a[:]               
b = a.copy()            
b = []; b.extend(a)     
b = a[0:len(a)]         
b, = a                 
b = list(a)            
b = [i for i in a]      
b = copy.copy(a)        
b = []
for item in a:
  b.append(item) 

newList = oldList[:]

##################################################################################

# How to trim a list in Python

# Suppose I have a list with X elements

# [4,76,2,8,6,4,3,7,2,1...]

[1,2,3,4,5,6,7,8][:5]
[1, 2, 3, 4, 5]

[1,2,3][:5]
[1, 2, 3]

x = [6,7,8,9,10,11,12]
x[:5]
[6, 7, 8, 9, 10]

# To trim a list in place without creating copies of it, use del:

t = [1, 2, 3, 4, 5]
# delete elements starting from index 4 to the end
del t[4:]

t
[1, 2, 3, 4]

del t[5:]

t
[1, 2, 3, 4]


range(10)[3::2] => [3, 5, 7, 9]

test[3:] = [3, 4, 5, 6, 7, 8, 9]
test[:3] = [0, 1, 2]

print(mylist[len(mylist) - 1])

##################################################################################

# Break A List Into N-Sized Chunks

# Create a list of first names
first_names = ['Steve', 'Jane', 'Sara', 'Mary','Jack','Bob', 'Bily', 'Boni', 'Chris','Sori', 'Will', 'Won','Li']

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]
        
# Create a list that from the results of the function chunks:
list(chunks(first_names, 5))

####################################################################################
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
