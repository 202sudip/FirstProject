import os
from string import digits

def rename_files():
    file_names = os.listdir("C:\prank\prank")
    print(file_names)
    current_working_directory = os.getcwd()
    print(current_working_directory)
    os.chdir("c:\\prank\prank")
    current_working_directory = os.getcwd()
    for filename in file_names:
        os.rename( filename, filename.translate(str.maketrans('','', "0123456789")))

    new_file_names = os.listdir("C:\prank\prank")
    print(new_file_names)


print("This is the copy of the original file)
rename_files()


