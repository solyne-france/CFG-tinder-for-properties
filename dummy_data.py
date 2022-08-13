import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Architektura2015",
    database="property"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE houses(name VARCHAR(50), price VARCHAR(50), address VARCHAR(50),city VARCHAR(50),postocde VARCHAR(50),bedroom INT)")

sqlFormula = "INSERT INTO houses (name, price, address, city, postcode, bedroom) VALUES (%S, %S, %S, %S, %S, %S)"

list = [ ("Terrace House", "£750,000", "Faversham Avenue", "London", "EN1", 4),
("Detached House", "£700,000", "St.Leonards Way", "London", "RM11", 3),
("5 Bedroom Property", "£950,000", "Roding Lane South", "London", "IG4", 5),
("End Terrace House", "£1,395,000", "Glebe Road", "London", "N8", 5),
("Flat on Hatley Road", "£650,000", "Hatley Road", "London", "N4", 2),
("Semi-detached bungalow", "£700,000", "Sunset Avenue", "London","E4",3),
("Bed flat for sale", "£135,000", "Palmerston Road", "London", "N22", 1),
("2 Bed Flat For same", "£475,000", "Walworth Road", "London", "SE1", 2),
("1 Bed Flat", "£575,000","Cranley gardens", "London", "SW7", 1),
("1 Bed Flat For Sale", "£750,000", "Principal Tower", "London", "E2",1),
("12 Semi-detached house", "£2,100,000", "Chatsworth Road", "London", "NW2",12)]

mycursor.executemany(sqlFormula, list)
db.commit()

for x in mycursor:
    print(x)