# Rearrange the files by deleting the digits 0-9

import os
def rename_files():
    #step1
    file_list=os.listdir(r"Your home directory")
    saved_path=os.getcwd()
    os.chdir(r"Your home driectory")
    #step2
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print(file_name.translate(None,"0123456789"))
rename_files()
