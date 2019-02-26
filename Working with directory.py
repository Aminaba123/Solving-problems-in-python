import os
cwd = os.getcwd()
print cwd

######################################################################

import os
print os.getcwd()

######################################################################
o/p:"C :\Users\admin\myfolder"

1.To get the current directory folder name alone

import os
str1=os.getcwd()
str2=str1.split('\\')
n=len(str2)
print str2[n-1]

######################################################################
