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

