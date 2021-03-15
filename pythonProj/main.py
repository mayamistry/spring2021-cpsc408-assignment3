import data_ingestion as di

#Function that runs the main code of the program
def run_assign3():
    di.readInCSV()
    userInput = ""
    while (userInput != "6"):
        di.printMenu()
        userInput = input("Enter an option here: ")
        if (userInput == "1"):
            di.displayAll()
        elif (userInput == "2"):
            di.addNewStudent()
        elif (userInput == "3"):
            di.updateStudent()
        elif (userInput == "4"):
            di.deleteStudent()
        elif (userInput == "5"):
            di.displayByField()
        elif (userInput == "6"):
            di.conn.close()
            print("Exiting program. Thank you!")
            break
        else:
            print("Input invalid. Please try again. ")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_assign3()



