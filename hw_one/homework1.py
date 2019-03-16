import os
from pathlib import Path
import shutil
from shutil import copyfile
import subprocess
from distutils.dir_util import copy_tree


#FIRST GO TO HOME DIRECTORY AND CREATE A DIRECTORY FOR THE ROOT. 
#THAT CREATE FOLDERS THAT OUR SYSTEM NEEDED
#THEN CHANGE DIRECTORY TO NEW ONE
home = os.environ['HOME']
os.chdir(home)
os.makedirs('jail')
os.makedirs('jail/bin')
os.makedirs('jail/lib')
os.makedirs('jail/lib64')
os.chdir('jail')
#---------------------------------------------------------------
#COPY THE INFORMATION OF SYSTEM BASH TO THE NEW FOLDER
source_of_bash = '/bin/bash'
target_of_bash = os.path.join(str(home) + '/jail/bin/' + 'bash')
copyfile(source_of_bash, target_of_bash)



# I CREATE TWO PATH FOR LIBRARIES 

dest_of_lib = os.path.join(str(home) + '/jail/lib')
dest_of_lib64 = os.path.join(str(home) + '/jail/lib64')

#IN SUBPROCESS CODE, IT TAKE INFORMATION USING LDD 
#THEN IT COPY TO THE NEW FOLDERS
#---------------------------------------------------------------
process = subprocess.Popen(['ldd' ,'/bin/bash'], stdout=subprocess.PIPE)
for line in iter(process.stdout.readline, b''):	
	for info_of_lib64 in(line.decode().split()):
		if info_of_lib64[0:6] == "/lib64":	
				
			shutil.copy(info_of_lib64,dest_of_lib64)
			
	for info_of_lib in (line.decode().split()[2:3]):
		shutil.copy( info_of_lib ,dest_of_lib)

#---------------------------------------------------------------
# This is the bash script that will be run in jail. 
# Copy to inside to jail

source_of_script = (os.path.join(str(home) + '/hw_one' + '/bash_script.sh')  
target_of_script = os.path.join(str(home) + '/jail' + '/bash_script.sh')
copyfile(source_of_script, target_of_script)

#-------------------------------------------------
# NOW I CREATE ANOTHER PATH TO FOR CHROOT COMMAND
#THEN WE CAN ENTER THE NEW ROOT
chroot_dest =os.path.join( str(home)+ '/jail')

 #if we do not give permission, chroot failed to run /bin/bash
 # also we give permission to bash script to run.
subprocess.run(['chmod', '-R','755', 'bin', 'lib', 'lib64'])

subprocess.run([ 'chmod','-R','777', 'bash_script.sh'])

# this subprocess is for enter the chroot and run the script.
# if you enter "exit", you escape from jail
subprocess.run(['sudo', 'chroot', chroot_dest, '/bin/bash', './bash_script.sh'])







			




