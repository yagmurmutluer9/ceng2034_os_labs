import os.path, time

#this is for printing files in the directory with their last modified time. 
for root,  dirs, files in os.walk("."):
    for filename in files:
        #print(filename)
         print("Last modified: %s" % time.ctime(os.path.getmtime(filename)),filename)

# this is for finding files end with txt. 
for file in os.listdir("."):
    if file.endswith(".txt"):
        print(os.path.join(".", file))
