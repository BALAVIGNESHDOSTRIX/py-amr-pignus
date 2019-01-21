import pyAesCrypt
from config import config as conn

bufferSize = conn.BUFFERSIZE
password = conn.SALT


def FileEncrypt(file_name,file_path):
    pyAesCrypt.encryptFile(file_path +conn.ROOT +file_name, conn.ENCRYPTED_FILE_PATH + file_name +  conn.AES_FILE_REF, password, bufferSize)
    return True

def FileDecrypt(file_name,file_path,name):
    pyAesCrypt.decryptFile(file_path + conn.ROOT + file_name , conn.NEEED_VOICE_PATH + name + conn.AMR_FILE_REF, password, bufferSize)
    return True

