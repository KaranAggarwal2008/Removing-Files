import os
import shutil
import time

deleted_folders_count = 0
deleted_files_count = 0

path=input("Please tell the path you want to delete")
days = 30
seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    #Path exists
    for root_folder, folders, files in os.walk(path):
        folderTime = ctime = os.stat(path).st_ctime(root_folder)
        if seconds >= folderTime:
				# removing the folder
				# removing the folder
	        if not shutil.rmtree(path):
                # success message
		        print("f",{path},"is removed successfully")
                deleted_folders_count=deleted_folders_count+1
	        else:
                # failure message
		        print("Unable to delete the folder:- ",path)
			    # breaking after removing the root_folder
			    break
