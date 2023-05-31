from connect import *
from time import sleep
from read import *

def delete():

    idField = input("Enter the ID of the film to be deleted: ")

    try:
        cursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")

        conn.commit()

        print(f"Record {idField} deleted from the film table")
        sleep(3) 
        read()
    except sql.OperationalError as e:
            conn.rollback()
            print(f"Record not found in database: {e}")
if __name__ == "__main__":
    delete()
