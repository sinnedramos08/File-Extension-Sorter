import os as os
import shutil as shutil

#Input path to sort
path_name=input("Enter Path:")
dir_name=input("Directory Name:")
ext_name=input("Extension Name:")


#Create directory for the files to be sorted
def create_directory(path:str,dir:str):
    fullpath_folder_dir=os.path.join(path,dir)
    try:
        if not os.path.exists(fullpath_folder_dir):
            os.makedirs(fullpath_folder_dir)
        else:
            pass
    except:
        print("Could not create directory")
    return(fullpath_folder_dir)


#Copy files of a certain extension to a directory
def copy_files(path:str,path_folder_target:str, ext:str):
    extensions_list=[]
    ext_with_dots="."+ ext
    #Check for Extensions in the path
    for files in os.listdir(path):
        files_extension=os.path.splitext(files)[1] #Get the File Extension
        if files_extension not in extensions_list:
            extensions_list.append(files_extension)


    if ext_with_dots not in extensions_list:
            print("Extension not available in directory\n")
            print("Available Extensions: ")
            for extension in extensions_list:   
                 print(extension)
    else:
        extensions_list.clear()
        for files in os.listdir(path):
            if files.endswith(ext):
                shutil.copy(os.path.join(path,files),path_folder_target)
                os.remove(os.path.join(path,files))
        #Scan through the path again for available extensions
        for files in os.listdir(path):
            files_extension=os.path.splitext(files)[1] #Get the File Extension
            if files_extension not in extensions_list:
                extensions_list.append(files_extension)

        print("Copy Finished, Available extensions: ")
        for extension in extensions_list:   
                 print(extension)
                 




full_path_folder=create_directory(path_name,dir_name)
copy_files(path_name,full_path_folder, ext_name)



