from connect import *

#Create table

cursor.execute(
'''
CREATE TABLE tblfilms (
	"filmID" INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"yearReleased" INT,
	"rating" TEXT,
    "duration" INT,
    "genre" TEXT,
    PRIMARY KEY("filmID" AUTOINCREMENT)
)'''
)

# Add titles

cursor.execute(
'''
INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
    VALUES ('In Fabric', '2018', '6', '118', 'Comedy horror'),('Flux Gourmet', '2022', '6', '111', 'Comedy horror'), ('Carol', '2015', '7' ,'118', 'Drama'),('Portrait of a Lady  on Fire','2019', '8', '122', 'Drama'),('Call Me by Your  Name', '2017', '8', '132', 'Drama'),('Little Women', '2019', '8', '135', 'Drama'),('Tar', '2022', '8', '158', 'Drama'),('The Devil Wears Prada', '2006', '7', '109', 'Comedy'),('9 to 5', '1980', '7', '109', 'Comedy'),('Fried Green Tomatoes', '1991', '8', '130', 'Drama'),('Beetlejuice','1988', '8', '92', 'Comedy'),('Edward Scissorhands', '1990', '8', '105', 'Fantasy')
'''
)
conn.commit()
