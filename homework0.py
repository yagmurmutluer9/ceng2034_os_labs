import os.path, time
from pathlib import Path


#change path to home directory and create "os_lab_0" 
home = str(Path.home())
os.chdir(home)
os.mkdir('os_lab_0')
os.chdir('os_lab_0')


#create  empty files 

f=open('a.txt', "w+").close()
f=open('b.txt', "w+").close()
f=open('z.py', "w+").close()

#this is for printing files in the directory with their last modified time. 
for root,  dirs, files in os.walk("."):
    for filename in files:
         print( "Last modified time of %s : %s" %  (filename, time.ctime(os.path.getmtime(filename))))


print()
print()
# this is for finding files end with txt. 
counter = 0

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(os.path.join('/os_lab_0', file))
        counter+=1

print('\ntotal number of ".txt" files found: %d' % counter)
