import os

# Returns a list of dictionaries containing information about all files
# (including nested files) in the specified directory.
# If no directory is specified, the current working directory is used.


def get_file_info(path="."):
# Defines a function called get_file_info() that takes an optional path argument, with a default value of "." (the current working directory).
    file_list = []
    if os.access(path, os.R_OK):
# creates an empty list called file_list, and checks if the path exists and is readable using the os.access() function.
        for file_name in os.listdir(path):
            full_path = os.path.join(path, file_name)
            if os.path.isfile(full_path):
                file_stats = os.stat(full_path)
                file_dict = {
                    "path": path,
                    "name": file_name,
                    "size": file_stats.st_size
                }
                file_list.append(file_dict)
        # Iterates over all files and directories in the specified path using the os.listdir() function. 
        # For each file, it creates a dictionary containing the file's path, name, and size using the os.path.join() and os.stat() functions, 
        # and appends the dictionary to file_list.
                
            elif os.path.isdir(full_path):
                file_list += get_file_info(full_path)
            # If a subdirectory is encountered, the function recursively calls itself with the subdirectory as the new path.
        return file_list
    
#path = "/home/ec2-user/environment/gold-member"
file_list = get_file_info()

for file_dict in file_list:
    print(file_dict)