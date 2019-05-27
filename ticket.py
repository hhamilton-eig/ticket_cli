#!/usr/bin/python3

# Importing libraries

import sys
import os
import datetime

ticket_total = 0

stamp = datetime.datetime.now()
nowtime = stamp.strftime("%X")
nowdate = datetime.date.today()

def checkFileExistByException(file_path):
    ret = True
    try:
        # Open file object.
        file_object = open(file_path, 'r')
        # Read entire file content data.
        file_data = file_object.read()
    except FileNotFoundError:
        ret = False
        answer = input(file_path + " does not exist. Do you want to create it? [yY/nN]\n")
        if answer == "y" or answer == "Y":
            create_file = open(file_path,"w+")
            create_file.close()
        else:
            print("Exiting...\n")
            sys.exit()
    except IOError:
        ret = False
        print(file_path + " can not be read. ")
        sys.exit()    
    except PermissionError:
        ret = False
        print("Do not have permission to read file " + file_path)
        sys.exit()

file_path = os.environ['HOME'] + "/ticket_list.txt"
checkFileExistByException(file_path)

def date_check(path):
    if str(nowdate) not in open(path).read():
        print("It's a new day! Adding " + str(nowdate) + " to ticket_list...")
        stamp_date = open(path,"a+")
        stamp_date.write("\n" + str(nowdate) + " tickets:\n")
        stamp_date.close()
        return
    else:
        return
date_check(file_path)

if (sys.argv[1] == "add") or (sys.argv[1] == "-a"):
    print("Adding " + str(sys.argv[2]) + " to ticket list.")
    ticky_list = open(file_path,"a+")
    ticky_list.write(sys.argv[2] + " " + str(nowtime) + "\n" )
    ticky_list.close()

# Ticket total should exist by date for each date, and be incremented via the file

# Adding ticket to total

# Adding a note to ticket?
