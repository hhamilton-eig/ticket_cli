#!/usr/bin/python3

# Importing libraries

import sys
import datetime

ticket_total = 0

stamp = datetime.datetime.now()
nowtime = stamp.strftime("%X")
nowdate = datetime.date.today()

def date_check():
    if str(nowdate) not in open("ticket_list.txt").read():
        print("It's a new day! Adding " + str(nowdate) + " to ticket_list...")
        stamp_date = open("ticket_list.txt","a+")
        stamp_date.write("\n" + str(nowdate) + " tickets: \n")
        stamp_date.close()
        return
    else:
        return
date_check()

if sys.argv[1] == "add":
    print("Adding " + str(sys.argv[2]) + " to ticket list.")
    ticky_list = open("ticket_list.txt","a+")
    ticky_list.write("\n" + sys.argv[2] + " " + str(nowtime) )
    ticky_list.close()
    ticket_total += 1

# Ticket total should exist by date for each date, and be incremented via the file

# Adding ticket to total

# Adding a note to ticket?
