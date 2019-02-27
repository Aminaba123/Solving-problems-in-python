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
