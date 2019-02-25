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
