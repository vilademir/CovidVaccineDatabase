import mysql.connector
import pandas
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="vaccinations"
)

cursor = mydb.cursor(buffered=True)

states = '''
  CREATE TABLE States(
    Entity VARCHAR(150) PRIMARY KEY,
    Code VARCHAR(100),
    DateWeek VARCHAR(100),
    TotalVacci INT,
    Population INT
    );
'''

cursor.execute(states)
mydb.commit()

us = '''
  CREATE TABLE US(
    Location VARCHAR(150),
    Cases INT,
    Deaths INT,
    ConfirmedCases INT,
    FOREIGN KEY US(Location) REFERENCES States(Entity)
);

'''

cursor.execute(us)
mydb.commit()

pfizer = '''
  CREATE TABLE Pfizer(
    Jurisdiction VARCHAR(150) PRIMARY KEY,
    DATE VARCHAR(100),
    First INT,
    Second INT,
    isDeleted INTEGER,
    FOREIGN KEY Pfizer(Jurisdiction) REFERENCES States(Entity)

  );
'''

cursor.execute(pfizer)
mydb.commit()

moderna = '''
  CREATE TABLE Moderna(
    Jurisdiction VARCHAR(150),
    DATE VARCHAR(100),
    FirstDose INT,
    SecondDose INT,
    isDeleted INTEGER,
    FOREIGN KEY Moderna(Jurisdiction) REFERENCES States(Entity)
  );

'''
cursor.execute(moderna)
mydb.commit()
janssen = '''

CREATE TABLE Janssen(
  Jurisdiction VARCHAR(150),
  DATE VARCHAR(100),
  FirstD INT,
  isDeleted INTEGER,
  FOREIGN KEY Janssen(Jurisdiction) REFERENCES States(Entity)

);

'''
cursor.execute(janssen)
mydb.commit()

#https://www.dezyre.com/recipes/connect-mysql-python-and-import-csv-file-into-mysql-and-create-table

fileData2= pandas.read_csv("/Users/vilademir/PycharmProjects/FinalProject/us-total-covid-19-vaccine-doses-administered.csv" , index_col = False, delimiter= "," , engine = 'python')
fileData2 = fileData2.fillna(0)
fileData2.head()

for k, row2 in fileData2.iterrows():
  sql2 = """INSERT INTO States(Entity, Code, DateWeek, TotalVacci, Population) VALUES (%s, %s, %s, %s, %s);"""
  cursor.execute(sql2, tuple(row2))
  mydb.commit()

fileData3 = pandas.read_csv("/Users/vilademir/PycharmProjects/FinalProject/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Pfizer.csv" , index_col = False, delimiter= "," , engine = 'python')
fileData3 = fileData3.fillna(0)
fileData3.head()

for k, row3 in fileData3.iterrows():
  sql3 = """INSERT INTO Pfizer(Jurisdiction, DATE, First, Second) VALUES (%s, %s, %s, %s);"""
  cursor.execute(sql3, tuple(row3))
  mydb.commit()

fileData4 = pandas.read_csv("/Users/vilademir/PycharmProjects/FinalProject/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Moderna.csv" , index_col = False, delimiter= "," , engine = 'python')
fileData4 = fileData4.fillna(0)
fileData4.head()
for k, row4 in fileData4.iterrows():
  sql4 = """INSERT INTO Moderna(Jurisdiction, DATE, FirstDose, SecondDose) VALUES (%s, %s, %s, %s);"""
  cursor.execute(sql4, tuple(row4))
  mydb.commit()

fileData5 = pandas.read_csv("/Users/vilademir/PycharmProjects/FinalProject/COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Janssen.csv" , index_col = False, delimiter= "," , engine = 'python')
fileData5 = fileData5.fillna(0)
fileData5.head()
for k, row5 in fileData5.iterrows():
  sql5 = """INSERT INTO Janssen(Jurisdiction, DATE, FirstD) VALUES (%s, %s, %s);"""
  cursor.execute(sql5, tuple(row5))
  mydb.commit()

fileData6 = pandas.read_csv("/Users/vilademir/PycharmProjects/FinalProject/unitedstates.csv - us-states.csv" , index_col = False, delimiter= "," , engine = 'python')
fileData6 = fileData6.fillna(0)
fileData6.head()
for k, row6 in fileData6.iterrows():
  sql6 = """INSERT INTO US(Location, Cases, Deaths, ConfirmedCases) VALUES (%s, %s, %s, %s);"""
  cursor.execute(sql6, tuple(row6))
  mydb.commit()

#https://datatofish.com/import-csv-sql-server-python/

def printData():
  print("""
  Which table would you like to print out?
  1: US Total Vaccination Stats
  2: US Moderna Allocation Stats
  3: US Pfizer Allocation Stats
  4: US Janssen Allocation Stats
  5: US COVID Cases Stats
  
  """)

  userInput = int(input("Which would you like to print: "))

  if userInput == 1:
    myQuery = ("Select * From States ;")
    cursor.execute(myQuery)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Entity', 'Code', 'DateWeek', 'TotalVacci', 'Population'])
    print(frame)
    mydb.commit()
  elif userInput == 2:
    myQueryTwo = ("Select * From Moderna ;")
    cursor.execute(myQueryTwo)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Jurisdiction', 'Date', 'FirstDose', 'SecondDose', 'isDeleted'])
    print(frame)
    mydb.commit()
  elif userInput == 3:
    myQueryThree = ("Select * From Pfizer ;")
    cursor.execute(myQueryThree)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Jurisdiction', 'Date', 'FirstDose', 'SecondDose', 'isDeleted'])
    print(frame)
    mydb.commit()
  elif userInput == 4:
    myQueryFour = ("Select * From Janssen ;")
    cursor.execute(myQueryFour)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Jurisdiction', 'Date', 'FirstDose', 'isDeleted'])
    print(frame)
    mydb.commit()
  elif userInput == 5:
    myQueryFive = ("Select * From US ;")
    cursor.execute(myQueryFive)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Location', 'Cases', 'Deaths', 'ConfirmedCases'])
    print(frame)
    mydb.commit()
  else:
    print("Invalid Entry. Please enter a number within range.")
    printData()

def createRecord():
  vacc = input("Which Vaccine Table would you like to create a new record? (Pfizer, Moderna, Janssen): ")
  while vacc.isalpha():
    if vacc.lower() == "pfizer":
      state = input("State: ")
      while not state.isalpha():
        if not state.isalpha():
          print("Invalid Entry.")
          state = input("State: ")
      date = input("Date [(x/x/x) format]: ")
      first = input("First Dose Total: ")
      while first.isalpha():
        if first.isalpha():
          print("Invalid Entry.")
          first = input("First Dose Total: ")
      second = input("Second Dose Total Allocation: ")
      while second.isalpha():
        if second.isalpha():
          print("Invalid Entry.")
          second = input("Second Dose Total Allocation: ")
      query = ("INSERT IGNORE INTO Pfizer(Jurisdiction, DATE, First, Second) VALUES (%s,%s,%s,%s);")
      mydb.commit()
      cursor.execute(query, (state, date, first, second))
      print("Thank you for using the Database.")
      mydb.commit()
      print("Table has been updated!")
      break
    if vacc.lower() == "moderna":
      state3 = input("State: ")
      while not state3.isalpha():
        if not state3.isalpha():
          print("Invalid Entry.")
          state3 = input("State: ")
      date3 = input("Date [(x/x/x) format]: ")
      first3 = input("First Dose Total: ")
      while first3.isalpha():
        if first3.isalpha():
          print("Invalid Entry.")
          first3 = input("First Dose Total: ")
      second3 = input("Second Dose Total Allocation: ")
      while second3.isalpha():
        if second3.isalpha():
          print("Invalid Entry.")
          second3 = input("Second Dose Total Allocation: ")
      query3 = ("INSERT IGNORE INTO Moderna(Jurisdiction, DATE, FirstDose, SecondDose) VALUES (%s,%s,%s,%s);")
      mydb.commit()
      cursor.execute(query3, (state3, date3, first3, second3))
      print("Thank you for using the Database.")
      mydb.commit()
      print("Table has been updated!")
      break
    elif vacc.lower() == "janssen":
      state2 = input("State: ")
      while not state2.isalpha():
        if not state2.isalpha():
          print("Invalid Entry.")
          state2 = input("State: ")
      date2 = input("Date [(x/x/x) format]: ")
      first2 = input("First Dose Total: ")
      while first2.isalpha():
        if first2.isalpha():
          print("Invalid Entry.")
          first2 = input("First Dose Total: ")
      query2 = ("INSERT IGNORE INTO Janssen(Jurisdiction, DATE, FirstD) VALUES (%s,%s,%s);")
      mydb.commit()
      cursor.execute(query2, (state2, date2, first2))
      print("Thank you for using the Database.")
      mydb.commit()
      print("Table has been updated!")
      break
    else:
      print("Invalid Entry.")
      createRecord()

def softDelete():
  deletion = input("From which table would you like to delete? (Pfizer, Moderna, Janssen)")
  if deletion.lower() == "pfizer":
    stateAsk = input("which state would you like to delete (case-sensitive ex. Oregon): ")
    query6 = ("UPDATE Pfizer SET isDeleted = 1 WHERE Jurisdiction = '"+ stateAsk +"';")
    cursor.execute(query6)
    mydb.commit()
  if deletion.lower() == "moderna":
    stateAsk2 = input("which state would you like to delete (case-sensitive ex. Oregon): ")
    query7 = ("UPDATE Moderna SET isDeleted = 1 WHERE Jurisdiction = '"+ stateAsk2 +"';")
    cursor.execute(query7)
    mydb.commit()
  if deletion.lower() == "janssen":
    stateAsk3 = input("which state would you like to delete (case-sensitive ex. Oregon): ")
    query8 = ("UPDATE Janssen SET isDeleted = 1 WHERE Jurisdiction = '"+ stateAsk3 +"' ;")
    cursor.execute(query8)
    mydb.commit()

def search():
  user = input(""" Which table would you like to search?
  
  1: US Total Vaccination Stats
  2: US COVID Cases Stats
  
  Input: 
  """"")
  if user == "1":
    stateStat = input("Which state would you like to search")
    queryOne = ("SELECT * FROM States Where Entity = '"+ stateStat +"';")
    cursor.execute(queryOne)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Entity', 'Code', 'Date', 'TotalVacci', 'Population'])
    print(frame)
    mydb.commit()
  elif user == "2":
    stateStat2 = input("Which state would you like to search: ")
    queryTwo = ("SELECT * FROM US Where Location = '"+ stateStat2 +"';")
    cursor.execute(queryTwo)
    data = cursor.fetchall()
    frame = pd.DataFrame(data, columns=['Location', 'Cases', 'Deaths', 'ConfirmedCases'])
    print(frame)
    mydb.commit()
  else:
    print("Invalid Entry. Try Again.")
    search()

def exportData():
  print("""
    Which table would you like to export to a csv file?
    1: US State Vaccination Stats
    2: US Moderna Allocation Stats
    3: US Pfizer Allocation Stats
    4: US Janssen Allocation Stats
    5: US Population Data

    """)

  user = int(input("Which would you like to print: "))

  if user == 1:
    myQuery = ("Select * From States ;")

    cursor.execute(myQuery)
    data = cursor.fetchall()
    pd.DataFrame(data).to_csv("UsVaccitions.csv")
    mydb.commit()
  elif user == 2:
    myQuery = ("Select * From Moderna ;")

    cursor.execute(myQuery)
    data = cursor.fetchall()
    pd.DataFrame(data).to_csv("Moderna.csv")
    mydb.commit()
  elif user == 3:
    myQuery = ("Select * From Pfizer ;")

    cursor.execute(myQuery)
    data = cursor.fetchall()
    pd.DataFrame(data).to_csv("Pfizer.csv")
    mydb.commit()
  elif user == 4:
    myQuery = ("Select * From Janssen ;")

    cursor.execute(myQuery)
    data = cursor.fetchall()
    pd.DataFrame(data).to_csv("Janssen.csv")
    mydb.commit()
  elif user == 5:
    myQuery = ("Select * From US ;")

    cursor.execute(myQuery)
    data = cursor.fetchall()
    pd.DataFrame(data).to_csv("UsGeneral.csv")
    mydb.commit()
  else:
    print("Invalid Entry. Please Try Again.")
    exportData()

def yesNo():
  inputTwo = input("Would you like to do something else (Yes/No)? ")
  if inputTwo.lower() == 'yes':
    main()
  elif inputTwo.lower() == 'no':
    print("Thank you for using the data base! ")
    exit()
  else:
    print("Enter a valid entry.")
    yesNo()

def update():
  update = input("Which state would you like to update? (ex. Oregon - case-sensitive): ")
  one = input("Total Cases: ")
  sqlOne = ("UPDATE US Set Cases = '" + one + "' WHERE Location = '" + update + "';")
  cursor.execute(sqlOne)
  mydb.commit()
  two = input("Total Deaths: ")
  sqlTwo = ("UPDATE US Set Deaths = '"+ two +"' WHERE Location = '"+ update +"';")
  cursor.execute(sqlTwo)
  mydb.commit()
  three = input("Confirmed: ")
  sqlThree = ("UPDATE US Set ConfirmedCases = '" + three + "' WHERE Location = '" + update + "';")
  cursor.execute(sqlThree)
  mydb.commit()

def compareGen():
  execQuer = (''' Select Entity, TotalVacci, US.Cases, Janssen.FirstD from States 
                  JOIN US ON States.Entity = US.Location
                  JOIN Janssen on States.Entity = Janssen.Jurisdiction
                  ORDER BY States.Entity ASC;
''')
  cursor.execute(execQuer)
  data = cursor.fetchall()
  frame = pd.DataFrame(data, columns=['Entity', 'TotalVacci', 'Cases', 'Janssen Dose'])
  print(frame)
  mydb.commit()

def sub():
  queryMaker = ('''Select * From US Where Location in
                (Select Location From US Where Deaths > 5000 and Cases > 10000);  
                ''')
  cursor.execute(queryMaker)
  data = cursor.fetchall()
  frame = pd.DataFrame(data, columns=['Location', 'Cases', 'Deaths', 'Confirmed Cases'])
  print(frame)
  mydb.commit()

def genTwo():
  execQuer = (''' Select Entity, TotalVacci, US.Cases, Pfizer.First, Pfizer.Second from States 
                    JOIN US ON States.Entity = US.Location
                    JOIN Pfizer on States.Entity = Pfizer.Jurisdiction
                    ORDER BY States.Entity ASC;
  ''')
  cursor.execute(execQuer)
  data = cursor.fetchall()
  frame = pd.DataFrame(data, columns=['Entity', 'TotalVacci', 'Cases', 'Pfizer 1st Dose' ,'Pfizer 2nd Dose'])
  print(frame)
  mydb.commit()

def genThree():
  execQuer = (''' Select Entity, TotalVacci, US.Cases, Moderna.FirstDose, Moderna.SecondDose from States 
                      JOIN US ON States.Entity = US.Location
                      JOIN Moderna on States.Entity = Moderna.Jurisdiction
                      ORDER BY States.Entity ASC;
    ''')
  cursor.execute(execQuer)
  data = cursor.fetchall()
  frame = pd.DataFrame(data, columns=['Entity', 'TotalVacci', 'Cases', 'Moderna 1st Dose', 'Moderna 2nd Dose'])
  print(frame)
  mydb.commit()

def main():
  print("""

  Welcome to the DataBase!
  What would you like to do?

  1: Print Data On Screen
  2: Export Existing Table Data to CSV file 
  3: Add New Data to US Vaccine Manufacturer
  4: Delete Record from US Vaccine
  5: Search US General Stats by State
  6: Update US Covid Totals
  7: Compare Janssen Stats to US States
  8: Compare Pfizer Stats to US States
  9: Compare Moderna Stats to US States
  10: Look at States with High Cases and High Deaths
  11: Exit Application
  
  """)

  userInput = int(input("Enter Choice Number: "))

  if userInput == 1:
    printData()
    yesNo()
  elif userInput == 2:
    exportData()
  elif userInput == 3:
    createRecord()
  elif userInput == 4:
    softDelete()
    yesNo()
  elif userInput == 5:
    search()
    yesNo()
  elif userInput == 6:
    update()
    yesNo()
  elif userInput == 7:
    compareGen()
    yesNo()
  elif userInput == 8:
    genTwo
    yesNo()
  elif userInput == 9:
    genThree()
    yesNo()
  elif userInput == 10:
    sub()
    yesNo()
  elif userInput == 11:
    exit()
  else:
    print("Invalid Entry. Try again")
    main()

if __name__ == "__main__":
    main()

cursor.close()
