'''
            DEVELOPER NAME : BALAVIGNESH.M

            IMPLEMENTED DATE : 20/01/2019

            SCOPE OF IMPLEMENTATION :
            
             For encrypt and decrypt the amr
            file using python and play when you want!..:)


'''

from tools import file_encrypt_decrypt as endypt
from tools import dir_helper as dird
from config import config as conn
from tools import filename_handler as filehand
from tools import csvfile_helper as csv
from tools import player as play
import os 
import getpass

class SweetVoicer:

    def __init__(self):
       
        conn.SALT = getpass.getpass('Enter your Salt : ')
        if conn.SALT != "":
            print("Salt Setuped Successfully !....")
        self.dir_list = [conn.ORGINAL_FILE_PATH,conn.NEEED_VOICE_PATH,conn.ENCRYPTED_FILE_PATH,conn.CSV_FILES_PATH,conn.FRIENDS_CSV_PATH]

        for x in self.dir_list:
            self.choice_decidor(x + conn.ROOT,self.dir_list.index(x))


    def choice_decidor(self,file_path,index):
        if dird.isDir(file_path):
            self.warning_alert(file_path)
        else:
            self.make_original_file_dir(file_path)

   

    def warning_alert(self,path):
        print(path , "Already Exsists")

    
    def make_original_file_dir(self,path_name):
        path = path_name
        
        try:
            os.mkdir(path)
        except OSError:  
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)

    def FileDecrypt(self):
        filename = str(input("Enter the file name : "))
        endypt.FileDecrypt(filename + conn.AES_AMR_REF,conn.ENCRYPTED_FILE_PATH,filename)

    def FileEncryptor(self):
        if dird.isDir(conn.ORGINAL_FILE_PATH):
            if dird.isContains(conn.ORGINAL_FILE_PATH):
                files = dird.GetFiles(conn.ORGINAL_FILE_PATH)
                for filed in files:
                    yrdate = filehand.yrDateExtractor(filed)
                    timeEx = filehand.timeSecExtractor(filed)
                    nameEx = filehand.personNameExtractor(filed)
                    needName = filehand.fileNeedName(filed)

                    if csv.CSV_exsist(nameEx):
                        if csv.CSV_Row_Write(nameEx,yrdate,timeEx):
                            if endypt.FileEncrypt(needName + conn.AMR_FILE_REF,conn.ORGINAL_FILE_PATH):
                                dird.File_Remove(needName + conn.AMR_FILE_REF,conn.ORGINAL_FILE_PATH + conn.ROOT)
                          

                    else:
                        csv.CSV_file_Create(nameEx)
                        if csv.CSV_Row_Write(nameEx,yrdate,timeEx):
                            if endypt.FileEncrypt(needName + conn.AMR_FILE_REF,conn.ORGINAL_FILE_PATH):
                                dird.File_Remove(needName + conn.AMR_FILE_REF,conn.ORGINAL_FILE_PATH + conn.ROOT)

                            
                print("All files are encrypted successfully...")
                print()
                print("Records also created successfully")
            else:
                print("The Folder Doen't contains any files")
        else:
            print("Directory doe not exsist....")

    def make_friends_list(self):
        csv.update_friends_to_csv()
    
    def display_friends_list(self):
        csv.read_friends_name()

    def show_friend_records(self):
        friend_name = str(input("Give me the friend Name: "))
        csv.read_specific_user_rec(friend_name)

    def get_voice(self):
        enc_file_name,nee_name = csv.get_specific_friend_rec()
        if endypt.FileDecrypt(enc_file_name,conn.ENCRYPTED_FILE_PATH,nee_name):
            play.amr_player(nee_name + conn.AMR_FILE_REF)
    
    def shutdown(self):
        for x in self.dir_list:
            os.rmdir(x + conn.ROOT)
        quit()



dostrix = SweetVoicer()


print("choice 1 for Full Encryption")
print("choice 2 for make friends list")
print("choice 3 for display friends name")
print("choice 4 for show sweet person record details")
print("choice 5 for quit")
print("choice 6 for show specific person record details")


def TargetSyncronizer(choice):
    {
        1 : dostrix.FileEncryptor,
        2 : dostrix.make_friends_list,
        3 : dostrix.display_friends_list,
        4 : dostrix.show_friend_records,
        5 : dostrix.shutdown,
        6 : dostrix.get_voice
    }.get(choice)()

while True:
    choice = int(input("Enter your choice : "))
    TargetSyncronizer(choice)   
