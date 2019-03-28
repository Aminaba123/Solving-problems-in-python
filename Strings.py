############## The particular format for strptime: ############################
datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
datetime.datetime(2013, 9, 28, 20, 30, 55, 782000)

string_date = "2013-09-28 20:30:55.78200"
abc = datetime.datetime.now()

if abc  > string_date :
    print True

############### How to convert a date string to different format #####################

datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')

############### Converting string into datetime ###############

# datetime.strptime is the main routine for parsing strings into datetimes. It can handle all sorts of formats, 
# with the format determined by a format string you give it

from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

#######################################################################################
# Print
"{} is {} years old".format("Bill",25)

import math
"{} is nice but {} is divine!".format(1, math.pi)
'1 is nice but 3.141592653589793 is divine!'

#######################################################################################
# Print 
print('{:>10s} is {:<10d} years old.' format('Bill', 25))

#######################################################################################
# Print
for i in range(5):
print("{:10d} --> {:4d}".format(i,i**2))

#######################################################################################
# Print
for n in range(3,11):
    print('{:4}-sides:{:6}{:10.2f}{:10.2f}'.format(n,180*(n-2),180*(n-2)/n,360/n))

#######################################################################################
# Print

for n in range(3,11):
    print('{:4}-sides:{:6}{:10.2f}{:10.2f}'.format(n,180*(n-2),180*(n-2)/n,360/n))    



#######################################################################################

>>> for n in range(3,11):
print(n,180*(n-2),180*(n-2)/n,360/n)

#######################################################################################

original_str = 'amin'
modified_str = 'nima'

print(\
'The original string is: {}\n\
the modified string is: {}\n\
the reversal is: {}\n\
String is a palindrome'.format(original_str, modified_str, modified_str[::-1]))

#######################################################################################
import math
print(math.pi) # unformatted print ing
3.141592653589793
print("Pi is {:.4f}".format(math.pi)) # floating−point pr e c i s i o n 4
Pi is 3.1416
print("Pi is {:8.4f}".format(math.pi)) # spe c i f y both p r e c i s i o n and width
Pi is 3.1416
print("Pi is {:8.2f}".format(math.pi))
Pi is 3.14

#######################################################################################

#We can find the first letter 'p' using the find method:
>>> river = "Mississippi"
>>> river.find("p")

#######################################################################################

amin= 'amin'
for index in range(len(amin)):
    print(amin[index])

#######################################################################################    
#  range(len(river)) does nicely as a nested call.

1 # Our implementation of the find function . Print s the index where
2 # the t a r g e t i s found ; a f a i l u r e message , i f i t i sn ' t found .
3 # This version only s ear che s for a s ing l e character .
4
5 river = 'Mississippi'
6 target = input('Input a character to find: ')
7 for index in range(len(river)): # for each index
8 if river[index] == target: # check i f the t a r g e t i s found
9 print("Letter found at index: ", index) # i f so , print the index
10 break # stop searching
11 else:
12 print('Letter',target,'not found in',river)

#######################################################################################
# We frequently look for both an index and the character, so Python provides the
# enumerate iterator, which provides both the index of the character and the character 
# itself as it steps through the string. Let’s try it:

# for index, letter in enumerate(river):
#   print(index,letter)
#######################################################################################

# Our implementation of the find function . Print s the index where
# the t a r g e t i s found ; a f a i l u r e message , i f i t i sn ' t found .
# This version only s ear che s for a s ing l e character .
river = 'Mississippi'
target = input('Input a character to find: ')
for index,letter in enumerate(river): # for each index
if letter == target: # check i f the t a r g e t i s found
print("Letter found at index: ", index) # i f so , print the index
break # stop searching
else:
print('Letter',target,'not found in',river)

#######################################################################################

# Our implementation of the find function . Print s the index where
# the t a r g e t i s found ; a f a i l u r e message , i f i t i sn ' t found .
# This version only s ear che s for a s ing l e character .
river = 'Mississippi'
target = input('Input a character to find: ')
for index,letter in enumerate(river): # for each index
if letter == target: # check i f the t a r g e t i s found
print("Letter found at index: ", index) # i f so , print the index
# break
else:
print('Letter',target,'not found in',river)
#######################################################################################

# we can use the split method to break the string object associated with name into parts
# where the split character is any whitespace character
# We can then combine those results with Python’s ability to do multiple
# assignments in the same lin

name = 'John Marwood Cleese'
first, middle, last = name.split()
transformed = last + ', ' + first + ' ' + middle
print(transformed)
Cleese, John Marwood

# The split method returns the three substrings from name when splitting at whitespace.

first, middle = name.split() # error : not enough pieces

#The split method can be useful for comma-separated data such as those generated by
#spreadsheets and databases

#######################################################################################
>>> line = 'bob,carol,ted,alice'
>>> first, second, third, fourth = line.split(',')
>>> print(first, second, third, fourth)
bob carol ted alice
>>> op1, op2 = "A+B".split('+')
>>> print(op1, op2)
A B
#######################################################################################

# Remember, string reversal is a slice from beginning
#to end with a -1 step

>>> pal 1 = "Madam, I'm Adam"
>>> pal 2 = "A man, a plan, a canal, Panama"
>>> print("Forward: {} \nBackward: {}".format(pal 1,pal 1[::-1]))
Forward: Madam, I'm Adam
#######################################################################################    

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('pgf')
from matplotlib import rc

rc('text',usetex=True)
rc('text.latex', preamble=r'\usepackage{color}')

a = "all unicorns poop rainbows ! ! !".split()
c = ['red', 'orange', 'brown', 'green', 'blue', 'purple', 'black']
st = ''
for i in range(len(a)):
    st = st + r'\textcolor{'+c[i]+'}{'+a[i]+'}'
plt.text(0.5,0.5,st)
plt.show()

#######################################################################################




























