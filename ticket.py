#!/usr/bin/python3

# Importing libraries

import sys
import os
import fileinput
import datetime
import re
import argparse

ticket_total = 0

stamp = datetime.datetime.now()
nowtime = stamp.strftime("%X")
nowdate = datetime.date.today()

file_path = os.environ['HOME'] + "/ticket_list.txt"

# handles errors related to file path of ticket_list.txt

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

# Increments today's ticket total

def tick_list_up():
   for line in fileinput.input(file_path, inplace=True):
       if line.strip().startswith(str(nowdate)):
            total = int(re.search(': (\d+)',line).group(1))
            total += 1
            line = str(nowdate) + " tickets:\tTotal: " + str(total) + "\n"
            sys.stdout.write(line)
       else:
            sys.stdout.write(line)

# Adds entry for today's date and total if missing

def date_check(path):
    if str(nowdate) not in open(path).read():
        print("It's a new day! Adding " + str(nowdate) + " to ticket_list...")
        stamp_date = open(path,"a+")
        stamp_date.write("\n" + str(nowdate) + " tickets:\tTotal: " + str(ticket_total) + "\n")
        stamp_date.close()
        return
    else:
        return

# Preliminary file checks

checkFileExistByException(file_path)
date_check(file_path)

# Handles appending tickets + timestamps to list, increments total for the day

if (sys.argv[1] == "add") or (sys.argv[1] == "--add") or (sys.argv[1] == "-a") or (sys.argv[1] == "a"):
    if (sys.argv[3] == "note") or (sys.argv[3] == "--note") or (sys.argv[3] == "-n") or (sys.argv[3] == "n"):
        ticky_list = open(file_path,"a+")
        ticky_list.write(sys.argv[2] + " " + str(nowtime) + sys.argv[4] + "\n" )
        tick_list_up()
        print("Adding " + str(sys.argv[2]) + " to ticket list. Total for today is ")
        ticky_list.close()
        exit
    else:
        ticky_list = open(file_path,"a+")
        ticky_list.write(sys.argv[2] + " " + str(nowtime) + "\n" )
        tick_list_up()
        print("Adding " + str(sys.argv[2]) + " to ticket list. Total for today is ")
        ticky_list.close()




