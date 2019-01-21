import os

# Checking the Path is valid or not
def isDir(file_path):
    if os.path.isdir(file_path):
        return True 
    else:
        return False

#Checking the path containes any files
def isContains(file_path):
    files = os.listdir(file_path)
    if files == []:
        return False 
    else:
        return True

#Getting the all the files from the folder
def GetFiles(file_path):
    files = os.listdir(file_path)
    return files

#Check if needed csv file is exsists or not 
def CSVFileExsist(file_name,file_path):
    cxv = file_name + '.csv'
    files = os.listdir(file_path)
    for filex in files:
        if cxv == filex:
            return True 
    return False

#Check if the friends csv file is exsists or not
def friends_csv_check(file_path):
        if isDir(file_path):
                if isContains(file_path):
                        return True 
                else:
                        return False
        else:
                print('Friends Directory not found')

#Removing the needed file
def File_Remove(filename,file_path):
        os.remove(file_path + filename)
         
