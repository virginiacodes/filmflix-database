from connect import *

def allrecords():
    cursor.execute("SELECT * FROM tblfilms")
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)

def title():
    filmTitle = input("Enter film title: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE title = '{filmTitle}' ") 
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)

def yearReleased():
    yearReleased = input("Enter release year: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased = '{yearReleased}' ") 
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)

def rating():
    filmRating = input("Enter film rating on IMDb: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{filmRating}' ") 
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)

def duration():
    duration = input("Enter film duration in minutes: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE duration BETWEEN '{duration}' - 20 AND '{duration}' + 20") 
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)

def genre():
    filmGenre = input("Enter Genre: ")
    cursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{filmGenre}' ") 
    row = cursor.fetchall() 
    for aRecord in row:
        print(aRecord)



if __name__ == "__main__":
    
    allrecords()
    title()
    yearReleased()
    rating()
    duration()
    genre()


