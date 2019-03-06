dic = {"key 1":"value 1","key b":"value b"}

#print the keys:
for key in dic:
    print key

#print the values:
for value in dic.itervalues():
    print value

#print key and values
for key, value in dic.iteritems():
    print key, value
    
###########################################################

mydic = {}
mydic['key_name'] = 'value_name'

print mydic.items()[0][0]

###########################################################

# iterate in dictionary  

for key in d:
	print key

# It gives us the key values    
for key in d:
	print d[key]    

###########################################################	
# If you want to just access first key of the first item in sampleDict.values(), this may be useful:

print sampleDict.values()[0].keys()[0]	

###########################################################
# Check if a given key already exists in a dictionary
# in is the intended way to test for the existence of a key in a dict
d = dict()

for i in xrange(100):
    key = i % 10
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

# If you wanted a default, you can always use dict.get():

d = dict()

for i in xrange(100):
    key = i % 10
    d[key] = d.get(key, 0) + 1

###############################	#############################

if 'key1' in dict:
  print "blah"
else:
  print "boo"

##########################################################

import csv
reader = csv.reader(open('CamCloseM6 4V300E10.csv'))

result = {}
for column in reader:
    key = column[0]
    if key in result:
        pass
    result[key] = column[1:]
print result

##########################################################

import csv
reader = csv.reader(open('CamCloseM6 4V300E10.csv'))

result = {row[0]:row[1:] for row in reader if row and row[0]}
print result

##########################################################

# How do I sort a list of dictionaries by a value of the dictionary?

newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 

import operator
# To sort the list of dictionaries by key='name':

list_of_dicts.sort(key=operator.itemgetter('name'))
# To sort the list of dictionaries by key='age':

list_of_dicts.sort(key=operator.itemgetter('age'))

##########################################################


























