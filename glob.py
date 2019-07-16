# The glob module finds all the path names matching a specified pattern

import glob
import errno
path = '/home/download/*.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
            pass # do what you want
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise

#########################################################

filenames = [...]
files = {}
 
for filename in filenames:
    with open(filename, "r") as file:
        if filename in files:
            continue
        files[filename] = file.read()
 
for filename, text in files.items():
    print(filename)
    print("=" * 80)
    print(text)
    
    
#########################################################    
