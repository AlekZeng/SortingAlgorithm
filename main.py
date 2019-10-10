import csv
from funcs import Result


mydict = []


def LibUpdate():  # compiles csv file to dict
  reader = csv.DictReader(open('PF Prefs.csv', 'r'))
  for line in reader:
    mydict.append(line)

def EmailPull():  # sample function to test format correctness
  
  for x in mydict:
    print(x['What is your 1st choice session?'], x['What is your FIRST name?']) 


LibUpdate()

Result.resultFormat()
Result.resultInsert("gsbrown@raleighcharterhs.org", 69)

#LeastPop()
#print(mydict)
