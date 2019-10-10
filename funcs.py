import csv

# Global defining funcs
mydict = []

def LibUpdate():  # compiles csv file to dict
  reader = csv.DictReader(open('PF Prefs.csv', 'r'))
  for line in reader:
    mydict.append(line)

# Result.csv manipulation
class Result:
   
   def resultFormat():  # Formats results.csv

     csv_columns = ['Last Name','Email','Assignment']
     filename = "results.csv"
     with open(filename, 'w') as f:  
       f.truncate

       w = csv.DictWriter(f, fieldnames=csv_columns)
      
       w.writeheader()
       print("results.csv has been truncated")

   def resultInsert(email,assignment):  # Assigns class to student
     LibUpdate()
     filename = "results.csv"
     identifier = "@"

     try:
       email.index(identifier)

     except ValueError:
       error = "ValueError: email string incorrect"
       return error

     try:
       x = int(assignment)
    
     except ValueError:
       error = "ValueError: Class ID not int"
       return error
    
    
     else:
         for x in mydict:
            
             csv_columns = ['Last Name','Email','Assignment']
             insertdict = {}

             if x["Email Address"] == email:
                
                 insertdict["Last Name"] = x["What is your LAST name?"]
                 insertdict["Email"] = x["Email Address"]
                 insertdict["Assignment"] = assignment

                 with open(filename, 'a', newline = '') as f:  
                     w = csv.DictWriter(f, fieldnames=csv_columns)
                    
                     w.writerow(insertdict)

     print("Schedule added")

class analyze:
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
      print(f'Class id #{x} has {countA} people who want this class')

      countdictA[x] = countA
    print(" ")
    lowestA = min(countdictA, key=countdictA.get)

    for x in reduxchoicesB:
      countB = choicesB.count(x)
      print(f'Class id #{x} has {countB} people who want this class')

      countdictB[x] = countB
    
    print(" ")
    lowestB = min(countdictB, key=countdictB.get)
    
    print(f"Lowest First choice class for block 1 is {lowestA}. Lowest First choice class for block 2 is {lowestB}")  

