# ticket_cli

### Python script for tracking my tickets

Installation:
```
git clone https://github.com/hhamilton-eig/ticket_cli
sudo cp ./ticket_cli/tkt.py /usr/local/bin/tkt
rm -rf ./ticket_cli
```

Usage:
```
tkt.py [-h] [--note NOTE] <ticket_number>

positional arguments:
  <ticket_number>       appends <ticket number> and timestamp to
                        ~/ticket_list.txt

optional arguments:
  -h, --help            show this help message and exit
  --note NOTE, -n NOTE  notates a ticket
  ```

Examples:
```
hhamilton@box:~$ tkt 14000000
/home/hhamilton/ticket_list.txt does not exist. Do you want to create it? [yY/nN]
y
It's a new day! Adding 2019-06-06 to ticket_list...
Adding 14000000 to ticket list. Total for today is 1

hhamilton@box:~$ tkt 15000000 --note escalation
Adding 15000000 to ticket list with note. Total for today is 2

hhamilton@box:~$ tail ~/ticket_list.txt

2019-06-06 tickets:     Total: 2
14000000 07:12:27
15000000 07:13:25 escalation
```
