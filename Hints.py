#######################################################

the equality operator ==, as in 'a' == 'a'.

#  If the two single characters are the same, the expression returns True
#  Note that the expression 'a' == 'A' returns False as those are indeed two different strings.

'a' == 'A'   # returns False as those are indeed two different strings.

Split ===== Split returns eac indvidual field as type str, so we can convert any field element 
to a n int if we wish to do atithmatic on it

# we need varibale to hold our count of pairs , and we can initialiseze it to 0

##################################################################
# these are not the same we should change the place of return
def x_gen (x):
    lo=[]
    for i in range(len(x)):
        lo.append(x[:i])
    return lo
  
def x_gen (x):
    lo=[]
    for i in range(len(x)):
        lo.append(x[:i])
        return lo  
      
      
####################################################################### 

# the difference between list and array for indexing 

