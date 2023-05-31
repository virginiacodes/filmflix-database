from read import *
from addTitle import *
from updateFilm import *
from deleteTitle import *

import reports


def menuOptions():
    options = 0 
    while options not in ["1","2","3","4","5","6"]:
        print("Menu Options\n1. Add a record.\n2. Delete a record.\n3. Amend a record.\n4. Print all records.\n5. Reports.\n6. To Exit Menu")
     
        options = input("Enter an option from the Menu choices above: ") 

        if options not in ["1","2","3","4","5","6"]:
            print(f"{options} not a valid choice!")
    return options


def reportOptionsMenu():
    options = 0 
    while options not in ["1","2","3","4","5"]:
        print("Report Menu Options\nEnter to Print By:\n1. All.\n2. Genre.\n3. Release year.\n4. Rating.\n5. To Exit Reports Menu")

        options = input("Enter an option from the Report Menu choices above: ") 
        if options not in ["1","2","3","4","5"]:
            print(f"{options} not a valid choice!")
    return options


def films():

    "Main Program"
    mainProgram = True 

    while mainProgram:
        mainMenu = menuOptions()
        if mainMenu == "1":
            insertTitle() 
        elif mainMenu == "2":
            delete()
        elif mainMenu == "3":
            update()
        elif mainMenu == "4":
            read()
        elif mainMenu == "5":
            reportProgram = True
            while reportProgram:
                reportMenu = reportOptionsMenu()
                if reportMenu == "1":
                    reports.allrecords()
                elif reportMenu == "2":
                    reports.genre()
                elif reportMenu == "3":
                    reports.yearReleased()
                elif reportMenu == "4":
                    reports.rating()
                else:
                    reportProgram = False
                    input("Press enter to exit the Report Menu: ")
        else:
            mainProgram = False
    input("Press enter to exit the Main Menu: ")
    return mainProgram
    
if __name__== "__main__":
    films()