import csv 
import os
import pandas as pd
from config import config as conn 
from . import  dir_helper as dirs
from . import filename_handler as fileh
from prettytable import PrettyTable as table

x = table()
y = table()

def CSV_exsist(file_name):
    if dirs.CSVFileExsist(file_name,conn.CSV_FILES_PATH):
        return True
    else:
        return False

def CSV_file_Create(file_name):
    csvfile = file_name + '.csv'
    with open(conn.CSV_FILES_PATH + conn.ROOT + csvfile,'w') as filecreate:
        writer = csv.writer(filecreate)
        writer.writerow(['Name','yeardate','time'])

def CSV_Row_Write(name,yrs,times):
    csvfile = name + '.csv'
    with open(conn.CSV_FILES_PATH + conn.ROOT + csvfile,'a') as csvwritefile:
        writer = csv.writer(csvwritefile)
        writer.writerow([name,yrs,times])
        return True

def make_friends_csv():
        csvfile = 'friends.csv'
        with open(conn.FRIENDS_CSV_PATH + conn.ROOT + csvfile,'w') as csvwritefile:
                writer = csv.writer(csvwritefile) 
                writer.writerow(['Name'])
                return True


def update_friends_to_csv():
        csvfile = 'friends.csv'
        if dirs.isDir(conn.CSV_FILES_PATH + conn.ROOT):
                if dirs.isContains(conn.CSV_FILES_PATH + conn.ROOT):
                        files = dirs.GetFiles(conn.CSV_FILES_PATH + conn.ROOT)
                        temp_name_list = []
                        for n in files:
                                name_parse = fileh.fileNeedName(n)
                                temp_name_list.append(name_parse)
                        
                        if dirs.friends_csv_check(conn.FRIENDS_CSV_PATH + conn.ROOT):
                                for names in temp_name_list:
                                        with open(conn.FRIENDS_CSV_PATH + conn.ROOT + csvfile,'a') as csvwritefile:
                                                writer = csv.writer(csvwritefile) 
                                                writer.writerow([names])
                        else:
                                if make_friends_csv():
                                        for name in temp_name_list:
                                                with open(conn.FRIENDS_CSV_PATH + conn.ROOT + csvfile,'a') as csvwritefile:
                                                        writer = csv.writer(csvwritefile) 
                                                        writer.writerow([name])

#Get the friends names and display it to the user
def read_friends_name():
        print('**** Firends Name are ****')
        print()
        csv_file = conn.FRIENDS_CSV_PATH + conn.ROOT +'friends.csv'
        with open(csv_file,'r') as read_csv:
                reader = csv.reader(read_csv)
                rows = list(reader)
                for names in range(1,len(rows)):
                        print(rows[names][0])

#Get the specific friend amr file record details
def read_specific_user_rec(sweet_name):
        target_csv = conn.CSV_FILES_PATH + conn.ROOT + sweet_name + '.csv'
        with open(target_csv,'r') as read_csv:
                reader = csv.reader(read_csv)
                rows = list(reader)
                x.field_names = [rows[0][0], rows[0][1], rows[0][2]]
                for details in range(1,len(rows)):
                        year = rows[details][1][0] + rows[details][1][1] + rows[details][1][2] + rows[details][1][3]
                        month = rows[details][1][4] + rows[details][1][5]
                        day = rows[details][1][6] + rows[details][1][7]
                        time_meridiean = None
                        if int(rows[details][2][0] + rows[details][2][1]) > 12:
                                sr = int(rows[details][2][0] + rows[details][2][1]) - 12
                                hr = '0' + str(sr)
                                time_meridiean = "PM"
                        else:
                                hr = rows[details][2][0] + rows[details][2][1]
                                time_meridiean = "AM"        
                        mit = rows[details][2][2] + rows[details][2][3]
                        sec = rows[details][2][4] + rows[details][2][5]
                        x.add_row([rows[details][0],day + "/" + month + "/" + year,str(hr) + ":" + mit + ":" + sec + "-" + time_meridiean])
                print(x)
                
                


def get_specific_friend_rec():
        date = str(input("Enter the date for needed record : "))
        name = str(input("Enter the person name : "))
        need_day = date[0:2]
        need_month = date[3:5]
        need_year = date[6:]
        need_date_str = need_year+need_month+need_day
        csv_file = conn.CSV_FILES_PATH + conn.ROOT + name + '.csv'
        with open(csv_file,'r') as read_csv:
                reader = csv.reader(read_csv)
                rows = list(reader)
                index = 0
                need_file = []
                for n in range(0,len(rows)):
                        if rows[index][1] == need_date_str:
                                need_file.append(rows[index])
                        index = index + 1
                print(" ***** Available Records ***** ")
                y.field_names = ["Record","Name", "Year", "Time"]
                index_state = 1
                for n in need_file:
                        time_meridiean_status = None 
                        for_time = n[2][0:2]
                        for_min = n[2][2:4]
                        for_sec = n[2][4:]
                        for_year = n[1][0:4]
                        for_month = n[1][4:6]
                        for_day = n[1][6:]
                        if int(for_time) > 12:
                                sr = int(for_time) - 12
                                hr = '0' + str(sr)
                                time_meridiean_status = "PM"
                        else:
                                hr = str(for_time)
                                time_meridiean_status = "AM"
                        y.add_row([index_state,n[0],for_day + "/" + for_month + "/" + for_year, hr + ":" + for_min + ":" + for_sec + "-" + time_meridiean_status])
                        index_state = index_state + 1
                print(y)
                rec_get_access = int(input("Enter the record no you want to play : "))
                need_enc_file = need_file[rec_get_access - 1][1] + "_" + need_file[rec_get_access - 1][2] + "-" + need_file[rec_get_access - 1][0] + conn.AES_AMR_REF
                need_enc_file_name = need_file[rec_get_access - 1][1] + "_" + need_file[rec_get_access - 1][2] + "-" + need_file[rec_get_access - 1][0]
                return need_enc_file,need_enc_file_name






                
                                
                                
                                        

                                




    