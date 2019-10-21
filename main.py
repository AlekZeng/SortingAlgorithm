import csv
from funcs import Result as re, analyze as an

mydict = []


def LibUpdate():  # compiles csv file to dict
    reader = csv.DictReader(open('PF Prefs.csv', 'r'))
    for line in reader:
        mydict.append(line)


def EmailPull():  # sample function to test format correctness

    for x in mydict:
        print(x['What is your 1st choice session?'],
              x['What is your FIRST name?'])


LibUpdate()

tfTop = 5  # To be assigned as tf variable
tfBot = 4  # To be assigned as tf variable
"""
Prioritizing vars
"""

firstTop = an.tops(tfTop, 1)
firstBot = an.bots(tfBot, 1)

secTop = an.tops(tfTop, 2)
secBot = an.bots(tfBot, 2)

triTop = an.tops(tfTop, 3)
triBot = an.bots(tfBot, 3)

quadTop = an.tops(tfTop, 4)
quadBot = an.bots(tfBot, 4)

pentTop = an.tops(tfTop, 5)
pentBot = an.bots(tfBot, 5)

re.resultFormat()


for x in firstBot[0]:
    for a in mydict:
        if a["What is your 1st choice session?"] == x:

            re.resultInsert(a["Email Address"], x)

for x in secBot[0]:
    for a in mydict:
        if a["What is your 2nd choice session?"] == x:

            re.resultInsert(a["Email Address"], x)
