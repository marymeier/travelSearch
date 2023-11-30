import sqlite3
import csv

rows = []

def create_Country():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS COUNTRY')
    create_country_table = """CREATE TABLE Country (
                            govt_struct VARCHAR(20), 
                            language VARCHAR(20), 
                            most_common_religion VARCHAR(20), 
                            time_zone VARCHAR(30),
                            name VARCHAR(50) NOT NULL, 
                            PRIMARY KEY(name)
                            );
    """
    cursor.execute(create_country_table)
    file = open('Country_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Country (name, most_common_religion, language, govt_struct, time_zone) VALUES (?,?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM Country"
    rows = cursor.execute(select_all).fetchall()

    for r in rows:
        print(r)

    connection.commit()
    connection.close()
        
def create_capital_city():
    # Connect to sqlite and 
    # Connect to tableSearch database
    connection = sqlite3.connect('travelSearch.db')
    # Cursor object
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS CAPITAL_CITY')
    create_capital_city_table = """CREATE TABLE Capital_City (
                            capital_city VARCHAR(30) NOT NULL,
                            population INT,
                            capital_city_region VARCHAR(30),
                            country VARCHAR(50),
                            PRIMARY KEY(name),
                            FOREIGN KEY (country) REFERENCES Country(name)
                            );
    """
    cursor.execute(create_capital_city_table)
    file = open('Capital_City_table.csv')
    contents = csv.reader(file)

    insert_records = "INSERT INTO Capital_City (country,capital_city,population,capital_city_region) VALUES (?,?,?,?)"
        
    cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM Capital_City"
    rows = cursor.execute(select_all).fetchall()

    for r in rows:
        print(r)

    connection.commit()
    connection.close()

if __name__ == "__connect_travelSearch__":
    connect_travelSearch()