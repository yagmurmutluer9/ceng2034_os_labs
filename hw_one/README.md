# A python script for chroot jail

1. when you run 'homework1.py' under hw_one directory, it will create a chroot jail. 
2. A bash_script will run inside the jail after you enter your passwd.
3. There's a simple game inside the bash but you can easily write "exit" to exit from jail.


## Bash script is only run under ceng2034_os_labs/hw_one
## If you run as home/hw_one, it will give you an error. 
 > In python file, 49th line, you can change the directory if you don't run under ceng24_os_labs
  49. source_of_script = os.path.join(str(home) + '/ceng2034_os_labs/hw_one' + '/bash_script.sh')
