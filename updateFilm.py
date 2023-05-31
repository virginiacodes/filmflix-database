from connect import *
from time import sleep
from read import *

def update():

    filmID = input("Enter the ID of the film to be updated: ")
    fieldName = input("Enter the field name (title, yearReleased, rating, duration, genre): ").lower()

    newFieldValue = input(f"Enter the value for {fieldName} field: ")
    print(newFieldValue)
    newFieldValue = "'"+ newFieldValue+"'"
    print(newFieldValue)

    try:
        cursor.execute(f"UPDATE tblfilms SET {fieldName} = {newFieldValue} WHERE filmID = {filmID}")
        "method 2"

        conn.commit()

        print(f"Record for {filmID} updated in the table")

        sleep(3) 
        read() 
    except sql.OperationalError as e:
        conn.rollback()
        print(f"Title not Updated: {e}")
if __name__ == "__main__":
    update()

