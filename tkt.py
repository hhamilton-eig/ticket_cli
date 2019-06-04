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

# Handles errors related to file path of ticket_list.txt


def checkFileExistByException(file_path):
    try:
        file_object = open(file_path, 'r')
        file_object.read()
    except FileNotFoundError:
        answer = input(
            file_path + " does not exist. Do you want to create it? [yY/nN]\n")
        if answer == "y" or answer == "Y":
            create_file = open(file_path, "w+")
            create_file.close()
        else:
            print("Exiting...\n")
            sys.exit()
    except PermissionError:
        print("Do not have permission to read file " + file_path)
        sys.exit()
    except IOError:
        print(file_path + " can not be read. ")
        sys.exit()


# Increments today's ticket total


def tick_list_up():
    for line in fileinput.input(file_path, inplace=True):
        if line.strip().startswith(str(nowdate)):
            total = int(re.search(': (\\d+)', line).group(1))
            total += 1
            line = str(nowdate) + " tickets:\tTotal: " + str(total) + "\n"
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)

# Adds entry for today's date and total if missing


def date_check(path):
    if str(nowdate) not in open(path).read():
        print("It's a new day! Adding " + str(nowdate) + " to ticket_list...")
        stamp_date = open(path, "a+")
        stamp_date.write("\n" + str(nowdate) +
                         " tickets:\tTotal: " + str(ticket_total) + "\n")
        stamp_date.close()
        return
    else:
        return

# Preliminary file checks


checkFileExistByException(file_path)
date_check(file_path)

# Captures total for the day

with open(file_path, 'r') as input_file:
    for line in input_file:
        if re.match(str(nowdate)+'.*', line):
            total = int(re.search(': (\\d+)', line).group(1))

# Argument definitions

parser = argparse.ArgumentParser()

parser.add_argument('ticket_number',
                    metavar='<ticket_number>',
                    type=int,
                    # action=AddTicket,
                    help='appends <ticket number> and timestamp to ~/ticket_list.txt')

parser.add_argument('--note',
                    '-n',
                    # action=NotateTicket,
                    help='notates a ticket')
args = parser.parse_args()

# Logic for handling arguments

if args.note:
    tick_list_up()
    ticky_list = open(file_path, "a+")
    ticky_list.write(str(args.ticket_number) + " " +
                     str(nowtime) + " " + str(args.note) + "\n")
    total += 1
    print("Adding " + str(args.ticket_number) +
          " to ticket list with note. Total for today is " + str(total))
    ticky_list.close()
else:
    if args.ticket_number:
        tick_list_up()
        ticky_list = open(file_path, "a+")
        ticky_list.write(str(args.ticket_number) + " " + str(nowtime) + "\n")
        total += 1
        print("Adding " + str(args.ticket_number) +
              " to ticket list. Total for today is " + str(total))
        ticky_list.close()
