import sqlite3
import pandas as pd
from pandas import DataFrame

#Opens up database and cursor and closes when the user wants to end the program
conn = sqlite3.connect('./StudentDB.db') #establish my connection
mycursor = conn.cursor() #the cursor allows python to execute sql statements

#Function that displays all information from student table
def displayAll():
    mycursor.execute("SELECT * FROM Student;")
    students = mycursor.fetchall()
    #This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(students,
                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address', 'City',
                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
    print(df)



#Function that allows you to add a new student
def addNewStudent():
    firstName = input("Enter the student's first name: ")
    lastName = input("Enter the student's last name: ")
    gpa = input("Enter a GPA: ")
    #need to make sure gpa is numerical value
    while (gpa.isalpha() == True):
        gpa = input("Error. Please try again and enter a numerical value for GPA: ")
    gpa = float(gpa)
    major = input("Enter a major: ")
    facultyAdvisor = input("Enter the faculty advisor: ")
    address = input("Enter an address: ")
    city = input("Enter a city: ")
    state = input("Enter a state: ")
    zipCode = input("Enter a zipcode: ")
    #zip code should not have alpha characters so check for that
    while (zipCode.isalpha() == True):
        zipCode = input("Error. Please input digits only for the zipcode: ")
    phoneNumber = input("Enter a mobile phone number: ")
    mycursor.execute(
        "INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor, Address, City, State, ZipCode, MobilePhoneNumber) VALUES (?,?,?,?,?,?,?,?,?,?)", (firstName, lastName, gpa, major, facultyAdvisor, address, city, state, zipCode, phoneNumber))
    conn.commit()
    print("Successfully added the new student!")

#Function that updates a student's information
def updateStudent():
    status = False
    while (status == False):
        checkStudent = input("Enter the student ID for which student's info you would like to update: ")
        mycursor.execute("SELECT * FROM Student WHERE StudentId = ?", [checkStudent])
        data = mycursor.fetchall()
        #If the ID the user entered does not exsit in the table, then they need to keep trying again until they get it right
        if data == []:
            print("Student ID entered is invalid, please try again.")
            continue
        else:
            status = True
            major = input("Enter a new major for the student or enter the same if you don't want to change: ")
            advisor = input("Enter a new faculty advisor for the student or enter the same if you don't want to change: ")
            phone = input("Enter a new phone number for the student or enter the same if you don't want to change: ")
            mycursor.execute("UPDATE Student SET Major = ?, FacultyAdvisor = ?, MobilePhoneNumber = ? WHERE StudentId = ?", (major, advisor, phone, checkStudent))
            conn.commit()
            print("Successfully updated the student's information!")
            break

#Function that performs soft delete
def deleteStudent():
    status = False
    while (status == False):
        checkStudent = input("Enter the student ID for which the student you would like to delete: ")
        mycursor.execute("SELECT * FROM Student WHERE StudentId = ?", [checkStudent])
        data = mycursor.fetchall()
        #If the ID the user entered does not exsit in the table, then they need to keep trying again until they get it right
        if data == []:
            print("Student ID entered is invalid, please try again.")
            continue
        else:
            status = True
            mycursor.execute("UPDATE Student SET isDeleted = 1 WHERE StudentId = ?", [checkStudent])
            conn.commit()
            print("Successfully deleted the student!")
            break

#Function that lets you display by a specific field
def displayByField():
    check = True
    while (check):
        print("Which field would you like to display students by? ")
        print("Enter 1 for by major.")
        print("Enter 2 for by GPA.")
        print("Enter 3 for by city.")
        print("Enter 4 for by state.")
        print("Enter 5 for by faculty advisor.")
        option = input("Enter the option you would like: ")
        if (option == "1"):
            check = False
            mycursor = conn.execute("SELECT DISTINCT Major FROM Student")
            data = mycursor.fetchall()
            print("Majors: ", data)
            check1 = False
            while (check1 == False):
                major = input("Enter a major you would like to see records for: ")
                mycursor.execute("SELECT * FROM Student WHERE Major = ?", [major])
                recordsByMajor = mycursor.fetchall()
                #If the major the user entered does not exsit in the table, then they need to keep trying again until they get it right
                if recordsByMajor == []:
                    print("This major doesn't exist, please try again.")
                    continue
                else:
                    check1 = True
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    df = DataFrame(recordsByMajor,
                                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City',
                                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
                    print(df)
                    break
        elif (option ==  "2"):
            check = False
            mycursor = conn.execute("SELECT DISTINCT GPA FROM Student")
            data = mycursor.fetchall()
            print("Unique GPA's: ", data)
            check2 = False
            while (check2 == False):
                gpa = input("Enter a gpa you would like to see records for: ")
                mycursor.execute("SELECT * FROM Student WHERE GPA = ?", [gpa])
                recordsByGPA = mycursor.fetchall()
                #If the GPA the user entered does not exsit in the table, then they need to keep trying again until they get it right
                if recordsByGPA == []:
                    print("This gpa doesn't exist, please try again.")
                    continue
                else:
                    check2 = True
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    df = DataFrame(recordsByGPA,
                                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City',
                                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
                    print(df)
                    break
        elif (option ==  "3"):
            check = False
            mycursor = conn.execute("SELECT DISTINCT City FROM Student")
            data = mycursor.fetchall()
            print("Cities: ", data)
            check3 = False
            while (check3 == False):
                city = input("Enter a city you would like to see records for: ")
                mycursor.execute("SELECT * FROM Student WHERE City = ?", [city])
                recordsByCity = mycursor.fetchall()
                #If the city the user entered does not exsit in the table, then they need to keep trying again until they get it right
                if recordsByCity == []:
                    print("This city doesn't exist, please try again.")
                    continue
                else:
                    check3 = True
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    df = DataFrame(recordsByCity,
                                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City',
                                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
                    print(df)
                    break
        elif (option == "4"):
            check = False
            mycursor = conn.execute("SELECT DISTINCT State FROM Student")
            data = mycursor.fetchall()
            print("States: ", data)
            check4 = False
            while (check4 == False):
                state = input("Enter a state you would like to see records for: ")
                mycursor.execute("SELECT * FROM Student WHERE State = ?", [state])
                recordsByState = mycursor.fetchall()
                #If the state the user entered does not exsit in the table, then they need to keep trying again until they get it right
                if recordsByState == []:
                    print("This state doesn't exist, please try again.")
                    continue
                else:
                    check4 = True
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    df = DataFrame(recordsByState,
                                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City',
                                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
                    print(df)
                    break
        elif (option == "5"):
            check = False
            mycursor = conn.execute("SELECT DISTINCT FacultyAdvisor FROM Student")
            data = mycursor.fetchall()
            print("Faculty Advisors: ", data)
            check5 = False
            while (check5 == False):
                advisor = input("Enter an advisor you would like to see records for: ")
                mycursor.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", [advisor])
                recordsByAdvisor = mycursor.fetchall()
                #If the advisor the user entered does not exsit in the table, then they need to keep trying again until they get it right
                if recordsByAdvisor == []:
                    print("This advisor doesn't exist, please try again.")
                    continue
                else:
                    check5 = True
                    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
                    df = DataFrame(recordsByAdvisor,
                                   columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor',
                                            'Address', 'City',
                                            'State', 'ZipCode', 'MobilePhoneNumber', 'isDeleted'])
                    print(df)
                    break
        else:
            print("Invalid input, please try again.")

#Function that prints out menu during each iteration
def printMenu():
    print("Select what you would like to do: ")
    print("Enter 1 if you would like to display all students and their information.")
    print("Enter 2 if you would like to add a new student.")
    print("Enter 3 if you would like to update a student's information.")
    print("Enter 4 if you would like to delete a student.")
    print("Enter 5 if you would like to display students by a specific field.")
    print("Enter 6 if you want to exit the program.")


#Function that reads in the CSV file
def readInCSV():
    # import data from csv
    mycursor = conn.execute("SELECT * FROM Student")
    data = mycursor.fetchall()
    #Only import the csv if the table is empty otherwise it will repeat rows and values every time you run it
    if (data  == []):
        with open("./students.csv") as file:
            num_records = 0
            for row in file:
                if num_records != 0:
                    mycursor.execute(
                        "INSERT INTO Student(FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, Major, GPA) VALUES (?,?,?,?,?,?,?,?,?)",
                        row.split(","))
                    conn.commit()
                num_records += 1






