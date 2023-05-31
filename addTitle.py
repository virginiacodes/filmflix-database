from connect import *
from time import sleep
from read import *

def insertTitle():
    titles = []

    title = input("Enter film title: ")
    yearReleased = input("Enter release year: ")
    rating = input("Enter IMDb rating: ")
    duration = input("Enter duration: ")
    genre = input("Enter genre: ")

    titles.append(title)
    titles.append(yearReleased)
    titles.append(rating)
    titles.append(duration)
    titles.append(genre)

    try:
        cursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)",
        titles)
        conn.commit()
        print(f"{title} added to the film table")
        sleep(3)
        read()
    except sql.OperationalError as e:
        conn.rollback()
        print(f"Record not added to database: {e}")

if __name__ == "__main__":
    insertTitle()
