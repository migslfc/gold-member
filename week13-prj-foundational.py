# we need the os module to work with files and directories, 
# the os module provides functions to work with files and directories. 

import os

# define your path. I'm using my repo since it has a good amount of files.

path = "/home/ec2-user/environment/gold-member"


file_list = [{
    "path": path,
    "name": file_name,
    "size": os.stat(path + '/' + file_name).st_size
} for file_name in os.listdir(path)]

# this list populates as it goes through the files in the cwd

for file_dict in file_list:
    print(file_dict)
    
# this prints each "dictionary file_dict" in our now populated list

# use the os.listdir() function to get information about files in the current working directory,. 
# it returns a list of all the files and directories in the current working directory. 
# we can loop through this list to get the name and size of each file.

# the os.stat() function returns an os.stat_result object that contains information about a file or directory. 
# this function takes a filename as its argument and returns a os.stat_result object that contains various file properties, 
# such as size, creation and modification time, and access permissions.
# access these properties using dot notation. For ex, to get the size of a file, use os.stat(file_name).st_size.