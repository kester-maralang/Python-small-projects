import os
import pandas as pd

########################################################
#Script Configuration
#########################################################

# Folder to search from e.g C:\Users
search_dir = "Y:\\cloi\\"
# Folder to find subfolders under e.g. CrystalFund
main_folder_name = "CrystalFund"
# Output csv file name
#csv_file_name = "proto.csv"

########################################################
#End Configuration
#########################################################

# Get all directory addresses

directory_list = list()

for root, dirs, files in os.walk(search_dir, topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

# Get folder names

folder_names= list()

# Concatenate string using for loops
for cur_dir in directory_list:
    if "\\"+main_folder_name+"\\" in cur_dir:
        split_dir = cur_dir.split("\\")
        for i, folder in enumerate(split_dir):
            if folder == main_folder_name:
                folder_name = split_dir[i+1]
                if folder_name not in folder_names:
                    folder_names.append(folder_name)
                break

#print folder_names

# Create CSV file

folder_names = pd.DataFrame(folder_names)

folder_names.to_csv("C:\\Users\\kmaralang\\Desktop\\Transfer\\Workload\\Python\\results.csv")

