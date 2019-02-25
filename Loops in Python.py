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

