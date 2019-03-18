with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

########################################################

with open('filename') as f:
    lines = f.readlines()
# or with stripping the newline character:

lines = [line.rstrip('\n') for line in open('filename')]    

########################################################

with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

########################################################

lines = tuple(open(filename, 'r'))

########################################################

input_file = open("input.txt","r")
output_file = open("output.txt","w")

for line_str in input_file :
    new_str = ''
    line_str = line_str.strip()
    for char in line_str:
        new_str =char+new_str
    print (new_str, file= output_file)    

########################################################
# open the data file for reading 

poker_file = open ("poker-hand-testing.data",'r')

total_count_int = 0  # create variable to hold the count --initialized it

# step through each line of the file

for line_str in poker_file:
    total_count_int = total_count_int+1  # at each line increament the counter 
    
print("total hands in file:",total_count_line)   

########################################################
a = "amin, abbasnejad "
b = a.split()
print b
########################################################

# For CSv file the separtion charecter is comma (","), so we get 11 different string fields for each line
# and we store those fileds in the fileds varibale. Because a list indexes in the same way as  astring 
# we can use an index of -1 to refernce the last field.


















    

