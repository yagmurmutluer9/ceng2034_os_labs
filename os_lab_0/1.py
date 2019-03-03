import os.path, time

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
        print(os.path.join(root, file))
        counter+=1

print('\ntotal number of ".txt" files found: %d' % counter)
