import csv
import pprint

mydict = []


def LibUpdate():  # compiles csv file to dict
  reader = csv.DictReader(open('PF Prefs.csv', 'r'))
  for line in reader:
    mydict.append(line)

def EmailPull():  # sample function to test format correctness
  
  for x in mydict:
    print(x['What is your 1st choice session?'], x['What is your FIRST name?'])


def LeastPop():  # Pulls the least popular class based on first chioce
  choicesA = []
  countdictA = {}
  choicesB = []
  countdictB = {}
  for x in mydict:
    choiceA = x["What is your 1st choice session?"]
    choicesA.append(str(choiceA))

    choiceB= x["What is your 1.2st choice session?"]
    choicesB.append(str(choiceB))

  reduxchoicesA = list(dict.fromkeys(choicesA))
  reduxchoicesB = list(dict.fromkeys(choicesB))

  for x in reduxchoicesA:
    countA = choicesA.count(x)
    print(f'Class id #{x} has {countA} people who want this class.')

    countdictA[x] = countA
  print(" ")
  lowestA = min(countdictA, key=countdictA.get)

  for x in reduxchoicesB:
    countB = choicesB.count(x)
    print(f'Class id #{x} has {countB} people who want this class.')

    countdictB[x] = countB
  
  print(" ")
  lowestB = min(countdictB, key=countdictB.get)
  
  print(f"Lowest First choice class for block 1 is {lowestA} \nLowest First choice class for block 2 is {lowestB}")  


LibUpdate()
LeastPop()
#print(mydict)
